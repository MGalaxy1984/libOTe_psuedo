import Define
import PRNG2
import SenderExpand
import SenderFerretMalCheck
import SenderLdpcMult
import Test
from Block import Block
import SenderHash
from PseudoAES import PseudoAES


if __name__ == '__main__':
    # SenderFerretMalCheck.test()
    # SenderHash.test()
    # SenderLdpcMult.test()
    # SenderLdpcMult.l_test()
    # SenderLdpcMult.r_test()
    # SenderExpand.test()
    # SenderExpand.d_test()
    # SenderExpand.e_test()
    SenderExpand.ee_test()
    # Test.aes_test_1()
    # PRNG2.test()
    # for i in range(8):
    #     print(f'$display("PRNG result [{i}] = %h", ei_mB_ram[{i}]);')
