from Block import Block
from PseudoAES import fixed_aes

mask = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE


def component(r, m, delta):
    """
    :param delta: INPUT a block. Generated by PRNG in the silentSend() function
    :param r: INPUT an array of blocks. Containing the data of mB
    :param m: OUTPUT an array of array of 2 blocks. The pointer of message (placeholder)
    :return:
    """
    assert isinstance(r, list)
    assert isinstance(m, list)
    assert len(m[0]) == 2
    assert isinstance(delta, Block)

    n8 = (len(m) // 8) * 8

    d = delta & mask

    i = 0
    while i < n8:
        r[i + 0] = r[i + 0] & mask
        r[i + 1] = r[i + 1] & mask
        r[i + 2] = r[i + 2] & mask
        r[i + 3] = r[i + 3] & mask
        r[i + 4] = r[i + 4] & mask
        r[i + 5] = r[i + 5] & mask
        r[i + 6] = r[i + 6] & mask
        r[i + 7] = r[i + 7] & mask

        m[i + 0][0] = r[i + 0]
        m[i + 1][0] = r[i + 1]
        m[i + 2][0] = r[i + 2]
        m[i + 3][0] = r[i + 3]
        m[i + 4][0] = r[i + 4]
        m[i + 5][0] = r[i + 5]
        m[i + 6][0] = r[i + 6]
        m[i + 7][0] = r[i + 7]

        m[i + 0][1] = r[i + 0] ^ d
        m[i + 1][1] = r[i + 1] ^ d
        m[i + 2][1] = r[i + 2] ^ d
        m[i + 3][1] = r[i + 3] ^ d
        m[i + 4][1] = r[i + 4] ^ d
        m[i + 5][1] = r[i + 5] ^ d
        m[i + 6][1] = r[i + 6] ^ d
        m[i + 7][1] = r[i + 7] ^ d

        # for j in range(8):
        #     print(f'm[{j}][0] = {m[i + j][0]} m[{j}][1] = {m[i + j][1]}')
        # print()

        tmp = []
        for j in range(4):
            tmp.append(m[i + j][0])
            tmp.append(m[i + j][1])
        hash_buffer = fixed_aes.encrypt_8_blocks(tmp)

        # for j in range(8):
        #     print(f'tmp[{j}] = {tmp[j]} hashBuffer[{j}] = {hash_buffer[j]}')
        # print()

        # test_buffer = fixed_aes.decrypt_8_block(hash_buffer)
        # for j in range(8):
        #     print(f'test decrypted[{j}] = {test_buffer[j]}')

        m[i + 0][0] ^= hash_buffer[0]
        m[i + 0][1] ^= hash_buffer[1]
        m[i + 1][0] ^= hash_buffer[2]
        m[i + 1][1] ^= hash_buffer[3]
        m[i + 2][0] ^= hash_buffer[4]
        m[i + 2][1] ^= hash_buffer[5]
        m[i + 3][0] ^= hash_buffer[6]
        m[i + 3][1] ^= hash_buffer[7]

        # for j in range(8):
        #     print(f'm[{j}][0] = {m[j][0]} m[{j}][1] = {m[j][1]}')
        # print()

        tmp = []
        for j in range(4, 8):
            tmp.append(m[i + j][0])
            tmp.append(m[i + j][1])
        hash_buffer = fixed_aes.encrypt_8_blocks(tmp)

        # for j in range(8):
        #     print(f'tmp[{j}] = {tmp[j]} hashBuffer[{j}] = {hash_buffer[j]}')
        # print()

        m[i + 4][0] ^= hash_buffer[0]
        m[i + 4][1] ^= hash_buffer[1]
        m[i + 5][0] ^= hash_buffer[2]
        m[i + 5][1] ^= hash_buffer[3]
        m[i + 6][0] ^= hash_buffer[4]
        m[i + 6][1] ^= hash_buffer[5]
        m[i + 7][0] ^= hash_buffer[6]
        m[i + 7][1] ^= hash_buffer[7]

        # for j in range(8):
        #     print(f'm[{j}][0] = {m[j][0]} m[{j}][1] = {m[j][1]}')
        # print()

        i += 8

    while i < len(m):
        m[i][0] = r[i] & mask
        m[i][1] = (r[i] ^ d) & mask

        tmp = fixed_aes.encrypt_1_block(m[i][0])
        m[i][0] = m[i][0] ^ tmp

        tmp = fixed_aes.encrypt_1_block(m[i][1])
        m[i][1] = m[i][1] ^ tmp

        i += 1

def a_component(r, m, delta):
    n8 = (len(m) // 8) * 8

    d = delta & mask

    i = 0
    while i < n8:
        r[i + 0] = r[i + 0] & mask
        r[i + 1] = r[i + 1] & mask
        r[i + 2] = r[i + 2] & mask
        r[i + 3] = r[i + 3] & mask
        r[i + 4] = r[i + 4] & mask
        r[i + 5] = r[i + 5] & mask
        r[i + 6] = r[i + 6] & mask
        r[i + 7] = r[i + 7] & mask

        m[i + 0][0] = r[i + 0]
        m[i + 1][0] = r[i + 1]
        m[i + 2][0] = r[i + 2]
        m[i + 3][0] = r[i + 3]
        m[i + 4][0] = r[i + 4]
        m[i + 5][0] = r[i + 5]
        m[i + 6][0] = r[i + 6]
        m[i + 7][0] = r[i + 7]

        m[i + 0][1] = r[i + 0] ^ d
        m[i + 1][1] = r[i + 1] ^ d
        m[i + 2][1] = r[i + 2] ^ d
        m[i + 3][1] = r[i + 3] ^ d
        m[i + 4][1] = r[i + 4] ^ d
        m[i + 5][1] = r[i + 5] ^ d
        m[i + 6][1] = r[i + 6] ^ d
        m[i + 7][1] = r[i + 7] ^ d

        # for j in range(8):
        #     print(f'm[{j}][0] = {m[i + j][0]} m[{j}][1] = {m[i + j][1]}')
        # print()

        tmp = []
        for j in range(8):
            tmp.append(m[i + j][0])
        hash_buffer = fixed_aes.encrypt_8_blocks(tmp)

        # for j in range(8):
        #     print(f'tmp[{j}] = {tmp[j]} hashBuffer[{j}] = {hash_buffer[j]}')
        # print()

        # test_buffer = fixed_aes.decrypt_8_block(hash_buffer)
        # for j in range(8):
        #     print(f'test decrypted[{j}] = {test_buffer[j]}')

        for j in range(8):
            m[i + j][0] ^= hash_buffer[j]

        # for j in range(8):
        #     print(f'm[{j}][0] = {m[j][0]} m[{j}][1] = {m[j][1]}')
        # print()

        tmp = []
        for j in range(8):
            tmp.append(m[i + j][1])
        hash_buffer = fixed_aes.encrypt_8_blocks(tmp)

        # for j in range(8):
        #     print(f'tmp[{j}] = {tmp[j]} hashBuffer[{j}] = {hash_buffer[j]}')
        # print()

        for j in range(8):
            m[i + j][1] ^= hash_buffer[j]

        # for j in range(8):
        #     print(f'm[{j}][0] = {m[j][0]} m[{j}][1] = {m[j][1]}')
        # print()

        i += 8

def test():
    fi = open("/home/mgalaxy/workspace/libOTe_component_files/sender_hash_input.txt")
    delta = Block(int("0x" + fi.readline().rstrip(), 16))
    print(f"delta = {delta}")

    n = 0
    r = []
    while True:
        line = fi.readline()
        if not line:
            break
        r.append(Block(int("0x" + line.rstrip(), 16)))
        n += 1

    for i in range(n):
        print(f"r[{i}] = {r[i]}")
    print()

    fi.close()

    m = []
    for i in range(n):
        tmp = [Block(), Block()]
        m.append(tmp)

    component(r, m, delta)

    fo = open("/home/mgalaxy/workspace/libOTe_component_files/sender_hash_component_output.txt", "w")

    for i in range(n):
        fo.write(str(r[i]))
        fo.write('\n')
        print(f"r[{i}] = {r[i]}")
    print()

    for i in range(n):
        tmp = m[i]
        fo.write(str(tmp[0]) + " " + str(tmp[1]))
        fo.write('\n')
        print(f'm[{i}][0] = {tmp[0]} m[{i}][1] = {tmp[1]}')

    fo.close()
