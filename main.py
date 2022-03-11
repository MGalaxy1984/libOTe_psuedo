import Define
import SenderFerretMalCheck
import SenderLdpcMult
from Block import Block
import SenderHash
from PseudoAES import PseudoAES


def ti(m: list[int]):
    m[0] = 15
    m[1] = 20


if __name__ == '__main__':
    # SenderFerretMalCheck.test()
    # SenderHash.test()
    # SenderLdpcMult.test()
    # SenderLdpcMult.l_test()
    # SenderLdpcMult.r_test()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ti(a[3:7])
    print(a)
