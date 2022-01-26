import copy
import numpy

from Cryptodome.Cipher import AES

import Define
from Block import Block


class PseudoAES:
    p_key = bytearray()

    aes_module = None

    def __init__(self, p_key_input):
        if isinstance(p_key_input, numpy.int):
            self.p_key = bytearray(p_key_input.to_bytes(16, byteorder=Define.byteorder))
        elif isinstance(p_key_input, bytes):
            self.p_key = bytearray(p_key_input)
        elif isinstance(p_key_input, bytearray):
            self.p_key = bytearray(p_key_input)
        # self.p_key.reverse()
        self.aes_module = AES.new(key=self.p_key, mode=AES.MODE_ECB)

    def encrypt_1_block(self, plaintext):
        assert isinstance(plaintext, Block)
        tmp_plaintext = bytearray(plaintext.data)
        # tmp_plaintext.reverse()
        ciphertext_bytes = self.aes_module.encrypt(tmp_plaintext)
        return Block(ciphertext_bytes)

    def encrypt_8_blocks(self, plaintext_array):
        assert len(plaintext_array) == 8
        ciphertext_array = []
        for i in range(8):
            plaintext = plaintext_array[i]
            ciphertext_array.append(self.encrypt_1_block(plaintext))

        return ciphertext_array

    def decrypt_1_block(self, ciphertext):
        assert isinstance(ciphertext, Block)
        plaintext = self.aes_module.decrypt(ciphertext.data)
        return Block(plaintext)

    def decrypt_8_block(self, ciphertext_array):
        assert len(ciphertext_array) == 8
        plaintext_array = []
        for i in range(8):
            ciphertext = ciphertext_array[i]
            plaintext_array.append(self.decrypt_1_block(ciphertext))
        return plaintext_array


fixed_key = 0x0000000002B3EA38FFFFFFFFF9D71ABA
# fixed_key = 0x0
fixed_aes = PseudoAES(fixed_key)
