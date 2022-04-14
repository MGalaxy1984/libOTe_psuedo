from Cryptodome.Cipher import AES

from Block import Block
from PseudoAES import PseudoAES


class PRNG2:
    key = None

    aes_ctr = None

    counter = 0

    nonce = int.to_bytes(0x777BD5E1B71BFDFE, 8, byteorder='big')

    def __init__(self, key_input: Block):
        self.counter = 0
        self.key = key_input.data
        self.aes_ctr = AES.new(self.key, mode=AES.MODE_ECB)

    def get(self):
        counter_bytes = int.to_bytes(self.counter, 8, byteorder='big')
        tmp = self.nonce + counter_bytes
        assert (len(tmp) == 16)
        b_out = self.aes_ctr.encrypt(tmp)
        self.counter += 1
        return Block(b_out)


def test():
    key = Block(0)
    p1 = PRNG2(key)
    p2 = PRNG2(key)
    for i in range(16):
        tmp1 = p1.get()
        tmp2 = p2.get()
        print(f'{tmp1} {tmp2}')
