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

    # r[0] = Block(0x0465740beb71dab73922d0d9a0959df3)
    # r[1] = Block(0x07a7ff4c0e58085154174d3bfd9dfbef)
    # r[2] = Block(0x01a9e83918edfa32ed769122e9caff49)
    # r[3] = Block(0x4f95165c9ee2405a3cc6ae0a99906f84)
    # r[4] = Block(0x3348121824d557ba7229f83beec3aff0)
    # r[5] = Block(0x2a77824df6c376113da9fdbe34e9fc1b)
    # r[6] = Block(0x471f9bd9b94a186954f81567d6ce4b59)
    # r[7] = Block(0xdc894ce7b47a4af7046a4bd1cbf78c11)
    # r[8] = Block(0x9b19a8adefd2232e2bcc43fefa917d56)
    # r[9] = Block(0x7b843edff6c420e94939e95a3d8c2bb7)
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
    # r[0] = Block(0x90b594e654250bb14687ce878ca4971d)
    # r[1] = Block(0x10f4f9582502b2fec298e487daef05cb)
    # r[2] = Block(0xc26ba0d12a8fd674de7cc00d0a43b371)
    # r[3] = Block(0x3126811351f2b26d78ae799c4b989072)
    # r[4] = Block(0x80d211383d0011c3298f9140885b44f8)
    # r[5] = Block(0x8cd3d30a50d367666d0112d77a1d1518)
    # r[6] = Block(0x92d298c6629c7832dcff4576c9f54f45)
    # r[7] = Block(0xf2c60a35095783aa9e346b2668fbd54f)
    # r[8] = Block(0xbb67f4457f11e5c860bdd14b40354824)
    # r[9] = Block(0x063ec72e0084f885c91b43706d5771ae)



    delta = Block(0x2e2b34ca59fa4c883b2c8aefd44be966)
    delta = Block(0x924b386ad40e07a50f94cb208ccf82a5)

    for i in range(n):
        tmp = r[i]
        print(f'r[{i}] = {tmp}')

    SenderHash.component(r, m, delta)

    for i in range(n):
        tmp = m[i]
        print(f'm[{i}][0] = {tmp[0]} m[{i}][1] = {tmp[1]}')

