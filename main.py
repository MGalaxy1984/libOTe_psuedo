import Define
from Block import Block
import SenderHash
from PseudoAES import PseudoAES

if __name__ == '__main__':
    n = 10
    m = []
    for i in range(n):
        tmp = [Block(), Block()]
        m.append(tmp)

    r = []
    for i in range(n):
        tmp = Block(i * 10)
        r.append(tmp)

    r[0] = Block(0xad55289111636a8c3658faf5d18d4e6a)
    r[1] = Block(0x1db9c25098ae71bee1fd8eb98eaf275e)
    r[2] = Block(0x3aea19a900b0672561c3c5049bafda9d)
    r[3] = Block(0xe09eae7f1a91d334832df7c7be3fdee1)
    r[4] = Block(0xde0bcb5a5b3df85cf2ac9aec73a036ac)
    r[5] = Block(0x4c520d36b94a8fb2a30e01fee095a465)
    r[6] = Block(0x75ed521a491e6bc135d26908897de3d9)
    r[7] = Block(0xbff33c2bc86b89eb1c16f105c3355128)
    r[8] = Block(0x38c9157032adf2ea8059e02cdc07bcce)
    r[9] = Block(0xe49e43c1805feda6c397855bd4c12b55)
    # r[0] = Block(0x0488b59ef0aca81b1f1b6a8a1ace7ee5)
    # r[1] = Block(0x3c9238cb351188460fa22208ebd2b45e)
    # r[2] = Block(0x40044cfd7c85e57b5dc1d097bd017ea5)
    # r[3] = Block(0xc5a057973e335d121412825c171fa557)
    # r[4] = Block(0x2704cce8af5565c7d1c0ad64f38ca64f)
    # r[5] = Block(0xe68de624bf7fd24e1c0b9ff32a9bbd27)
    # r[6] = Block(0xa3c07f1377bc5b2847e1fdfff9ca12c9)
    # r[7] = Block(0xa078e4bbfead8e45fdb6cbeb15f90e9b)
    # r[8] = Block(0xd687763b4f24aec65486da4c488cdb20)
    # r[9] = Block(0x3e431b5e9e7e5aa11088ba22b51374bc)

    delta = Block(0x2e2b34ca59fa4c883b2c8aefd44be966)

    for i in range(n):
        tmp = r[i]
        print(f'r[{i}] = {tmp}')

    SenderHash.component(r, m, delta)

    for i in range(n):
        tmp = m[i]
        print(f'm[{i}][0] = {tmp[0]} m[{i}][1] = {tmp[1]}')

