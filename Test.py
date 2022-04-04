from Block import Block
from PseudoAES import PseudoAES


def aes_test_1():
    a = PseudoAES(0)
    p = Block(135)
    for i in range(10):
        c = a.encrypt_1_block(p)
        print(c)
