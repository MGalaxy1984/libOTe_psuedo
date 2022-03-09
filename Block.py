import Define


def get_all_0_block():
    tmp = 0
    return bytearray(tmp.to_bytes(length=16, byteorder='big'))


def get_block_from_number(number):
    assert isinstance(number, int)
    return bytearray(number.to_bytes(length=16, byteorder='big'))


def get_block_from_list(number_list):
    """
    Get a block from a list of numbers.
    :param number_list: A list of python int. The list is not necessarily to be length of 16,
    and it will fill the length with big endian order (for example, if input is [1, 2], the
    result will be [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2]). Each number in the list
    cannot exceed 255 (will keep the lowest 8 bits if exceed 255).
    :return: A block generated
    """
    list_length = len(number_list)
    assert list_length <= 16
    to_return = get_all_0_block()
    for i in range(list_length):
        assert isinstance(number_list[i], int)


class Block:
    # bytearray
    data = None

    def __init__(self, init=0):
        if isinstance(init, int):
            self.data = bytearray(init.to_bytes(length=16, byteorder=Define.byteorder))
        elif isinstance(init, bytes):
            assert len(init) == 16
            self.data = bytearray(init)
        elif isinstance(init, bytearray):
            assert len(init) == 16
            self.data = bytearray(init)
        elif isinstance(init, Block):
            self.data = init.data.copy()
        else:
            raise TypeError('Input not recognized')

    def init_0(self):
        self.data = bytearray(int(0).to_bytes(length=16, byteorder=Define.byteorder))

    def init_number(self, number):
        assert isinstance(number, int)
        self.data = bytearray(number.to_bytes(length=16, byteorder=Define.byteorder))

    def init_list(self, number_list):
        assert isinstance(number_list, list)
        self.data = bytearray(number_list)

    def init_string(self, string):
        assert isinstance(string, str)
        self.data = bytearray(string)

    def set(self, other):
        if isinstance(other, Block):
            self.data = other.data.copy()
        elif isinstance(other, int):
            self.data = bytearray(other.to_bytes(length=16, byteorder=Define.byteorder))
        elif isinstance(other, list):
            self.data = bytearray(other)
        elif isinstance(other, str):
            self.data = bytearray(other)
        elif isinstance(other, bytes):
            assert len(other) == 16
            self.data = bytearray(other)
        elif isinstance(other, bytearray):
            assert len(other) == 16
            self.data = bytearray(other)
        else:
            raise TypeError('Input not recognized')

    def __str__(self):
        return self.__hex__()

    def __hex__(self):
        return self.data.hex()

    def __xor__(self, other):
        assert len(self.data) == 16
        to_return = Block(0)
        if isinstance(other, Block):
            for i in range(16):
                to_return.data[i] = self.data[i] ^ other.data[i]
        elif isinstance(other, int):
            tmp = other.to_bytes(length=16, byteorder=Define.byteorder)
            for i in range(16):
                to_return.data[i] = self.data[i] ^ tmp[i]
        return to_return

    def __and__(self, other):
        assert len(self.data) == 16
        to_return = Block(0)
        if isinstance(other, Block):
            for i in range(16):
                to_return.data[i] = self.data[i] & other.data[i]
        elif isinstance(other, int):
            tmp = other.to_bytes(length=16, byteorder=Define.byteorder)
            for i in range(16):
                to_return.data[i] = self.data[i] & tmp[i]
        return to_return

    def __eq__(self, other):
        assert len(other.data) == 16
        for i in range(16):
            if self.data[i] != other.data[i]:
                return False
        return True

    def reverse(self):
        self.data.reverse()

    def to_int(self):
        return int.from_bytes(self.data, Define.byteorder)

    def to_int_list(self):
        return [int.from_bytes(self.data[8:16], Define.byteorder), int.from_bytes(self.data[0:8], Define.byteorder)]

    # def gf_128_mul(self, y, xy1=None, xy2=None):
    #     assert isinstance(y, Block)
    #     if xy1 is None:
    #         xy1 = Block()
    #     else:
    #         assert isinstance(xy1, Block)
    #     if xy2 is None:
    #         xy2 = Block()
    #     else:
    #         assert isinstance(xy2, Block)
    #     x = self
    #
    #     mod = 0b10000111
    #     shifted = x.to_int_list()
    #     result0 = xy1.to_int_list()
    #     result1 = xy2.to_int_list()
    #     yy = y.to_int_list()
    #     print(f'yy[0] = {hex(yy[0])}')
    #     print(f'yy[1] = {hex(yy[1])}')
    #     for i in range(2):
    #         for j in range(64):
    #             if yy[i] & (1 << j):
    #                 result0[0] ^= shifted[0]
    #                 result0[1] ^= shifted[1]
    #
    #             if shifted[1] & (1 << 63):
    #                 shifted[1] = (shifted[1] << 1) | (shifted[0] >> 63)
    #                 shifted[1] &= Define.max_int_64
    #                 shifted[0] = (shifted[0] << 1) ^ mod
    #                 shifted[0] &= Define.max_int_64
    #             else:
    #                 shifted[1] = (shifted[1] << 1) | (shifted[0] >> 63)
    #                 shifted[1] &= Define.max_int_64
    #                 shifted[0] = shifted[0] << 1
    #                 shifted[0] &= Define.max_int_64
    #     print(f'result[0] = {hex(result0[0])}')
    #     print(f'result[1] = {hex(result0[1])}')
    #     xy1.set((result0[1] << 64) + result0[0])
    #     xy2.set((result1[1] << 64) + result1[0])

    def gf_128_mul(self, y, xy1, xy2):
        assert isinstance(y, Block)
        assert isinstance(xy1, Block)
        assert isinstance(xy2, Block)
        x = self

        t1 = Define.mm_clmulepi64_si128(x, y, 0x00)
        t2 = Define.mm_clmulepi64_si128(x, y, 0x10)
        t3 = Define.mm_clmulepi64_si128(x, y, 0x01)
        t4 = Define.mm_clmulepi64_si128(x, y, 0x11)

        t2 = (t2 ^ t3)
        t3 = Define.mm_slli_si128(t2, 8)
        t2 = Define.mm_srli_si128(t2, 8)
        t1 = (t1 ^ t3)
        t4 = (t4 ^ t2)

        # print(f't1 = {t1}')
        # print(f't4 = {t4}')
        xy1.set(t1)
        xy2.set(t4)
        # print(f'result[0] = {hex(result0[0])}')
        # print(f'result[1] = {hex(result0[1])}')
        # xy1.set((result0[1] << 64) + result0[0])
        # xy2.set((result1[1] << 64) + result1[0])
        return xy1.gf_128_reduce(xy2)
        
    def gf_128_reduce(self, y):
        assert isinstance(y, Block)
        mul256_low = self
        mul256_high = y
        mod = 0b10000111
        modulus = Block(mod)
        tmp = Define.mm_clmulepi64_si128(mul256_high, modulus, 0x01)
        mul256_low = mul256_low ^ Define.mm_slli_si128(tmp, 8)
        mul256_high = mul256_high ^ Define.mm_srli_si128(tmp, 8)

        tmp = Define.mm_clmulepi64_si128(mul256_high, modulus, 0x00)
        mul256_low = mul256_low ^ tmp

        return mul256_low

