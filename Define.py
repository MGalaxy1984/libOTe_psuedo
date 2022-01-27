import tkinter

from Block import Block

byteorder = 'big'

mSizePer = 0
mNumPartitions = 0

max_int_64 = 0xFFFFFFFFFFFFFFFF

def set_bit(value, bit_index, bit):
    assert isinstance(value, int)
    assert isinstance(bit_index, int)
    assert bit == 0 or bit == 1
    mask = 1 << bit_index

    return value | (1 << bit_index)

def _mm_clmulepi64_si128(a, b, imm8):
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
    temp1 = 0
    temp2 = 0
    if (imm8 % 2) == 0:
        temp1 = int.from_bytes(a.data[8:15], byteorder)
    else:
        temp1 = int.from_bytes(a.data[0:7], byteorder)
    if (imm8 >> 4) % 2 == 0:
        temp2 = int.from_bytes(b.data[8:15], byteorder)
    else:
        temp2 = int.from_bytes(b.data[0:7], byteorder)

    # for i in range(64):

