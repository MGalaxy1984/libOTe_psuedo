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

    r[0] = Block(0x0465740beb71dab73922d0d9a0959df3)
    r[1] = Block(0x07a7ff4c0e58085154174d3bfd9dfbef)
    r[2] = Block(0x01a9e83918edfa32ed769122e9caff49)
    r[3] = Block(0x4f95165c9ee2405a3cc6ae0a99906f84)
    r[4] = Block(0x3348121824d557ba7229f83beec3aff0)
    r[5] = Block(0x2a77824df6c376113da9fdbe34e9fc1b)
    r[6] = Block(0x471f9bd9b94a186954f81567d6ce4b59)
    r[7] = Block(0xdc894ce7b47a4af7046a4bd1cbf78c11)
    r[8] = Block(0x9b19a8adefd2232e2bcc43fefa917d56)
    r[9] = Block(0x7b843edff6c420e94939e95a3d8c2bb7)
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

