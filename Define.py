from Block import Block

byteorder = 'big'

mSizePer = 0
mNumPartitions = 0

max_int_64 = 0xFFFFFFFFFFFFFFFF
max_int_128 = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF


def set_bit(value, bit_index, bit):
    assert isinstance(value, int)
    assert isinstance(bit_index, int)
    assert bit == 0 or bit == 1
    if bit == 1:
        return value | (1 << bit_index)
    else:
        return value & ~(1 << bit_index)


def get_bit(value, bit_index):
    return (value >> bit_index) & 1


def mm_clmulepi64_si128(a, b, imm8):
    """
    :param a: INPUT a block
    :param b: INPUT a block
    :param imm8: INPUT a int
    :return: OUTPUT a block
    IF (imm8[0] == 0)
	    TEMP1 := a[63:0]
    ELSE
	    TEMP1 := a[127:64]
    FI
    IF (imm8[4] == 0)
	    TEMP2 := b[63:0]
    ELSE
	    TEMP2 := b[127:64]
    FI
    FOR i := 0 to 63
	    TEMP[i] := (TEMP1[0] and TEMP2[i])
	    FOR j := 1 to i
		    TEMP[i] := TEMP[i] XOR (TEMP1[j] AND TEMP2[i-j])
	    ENDFOR
	    dst[i] := TEMP[i]
    ENDFOR
    FOR i := 64 to 127
	    TEMP[i] := 0
	    FOR j := (i - 63) to 63
		    TEMP[i] := TEMP[i] XOR (TEMP1[j] AND TEMP2[i-j])
	    ENDFOR
	    dst[i] := TEMP[i]
    ENDFOR
    dst[127] := 0
    """
    assert isinstance(a, Block)
    assert isinstance(b, Block)
    assert isinstance(imm8, int)
    dst = 0
    # temp1 = 0
    # temp2 = 0
    a_int_list = a.to_int_list()
    b_int_list = b.to_int_list()
    if (imm8 % 2) == 0:
        temp1 = a_int_list[0]
    else:
        temp1 = a_int_list[1]
    if (imm8 >> 4) % 2 == 0:
        temp2 = b_int_list[0]
    else:
        temp2 = b_int_list[1]

    temp = 0
    for i in range(64):
        temp = set_bit(temp, i, (get_bit(temp1, 0) & get_bit(temp2, i)))
        for j in range(1, i + 1):
            tmp_bit = get_bit(temp, i) ^ (get_bit(temp1, j) & get_bit(temp2, i - j))
            temp = set_bit(temp, i, tmp_bit)
        dst = set_bit(dst, i, get_bit(temp, i))
    # print(f'temp = {temp}')
    for i in range(64, 128):
        temp = set_bit(temp, i, 0);
        for j in range(i - 63, 64):
            tmp_bit = get_bit(temp, i) ^ (get_bit(temp1, j) & get_bit(temp2, i - j))
            temp = set_bit(temp, i, tmp_bit)
        dst = set_bit(dst, i, get_bit(temp, i))
    dst = set_bit(dst, 127, 0)

    # print(f'dst = {hex(dst)}')

    # if (imm8 % 2) == 0:
    #     tmp = (a_int_list[1] << 64 + temp1) & max_int_128
    #     a.set(tmp)
    # else:
    #     a.set(temp1 << 64 + a_int_list[0])
    # if (imm8 >> 4) % 2 == 0:
    #     b.set(b_int_list[1] << 64 + temp2)
    # else:
    #     b.set(temp2 << 64 + b_int_list[0])

    return Block(dst)


def mm_slli_si128(a, imm8):
    assert isinstance(a, Block)
    assert isinstance(imm8, int)
    tmp = imm8 & 0xFF
    if tmp > 15:
        tmp = 16
    dst = (a.to_int()) << (tmp * 8)
    dst &= max_int_128
    return Block(dst)


def mm_srli_si128(a, imm8):
    assert isinstance(a, Block)
    assert isinstance(imm8, int)
    tmp = imm8 & 0xFF
    if tmp > 15:
        tmp = 16
    dst = (a.to_int()) >> (tmp * 8)
    dst &= max_int_128
    return Block(dst)
