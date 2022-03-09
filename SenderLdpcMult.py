from Block import Block

mWeight = 5
main_end = 48

diagMtx_g16_w5_seed1_t36 = [
    [0, 4, 11, 15],
    [0, 8, 9, 10],
    [1, 2, 10, 14],
    [0, 5, 8, 15],
    [3, 13, 14, 15],
    [2, 4, 7, 8],
    [0, 9, 12, 15],
    [1, 6, 8, 14],
    [4, 5, 6, 14],
    [1, 3, 8, 13],
    [3, 4, 7, 8],
    [3, 5, 9, 13],
    [8, 11, 12, 14],
    [6, 10, 12, 13],
    [2, 7, 8, 13],
    [0, 6, 10, 15]
]

m_rows = 0
cols = 0

offset0 = 0
offset1 = 0


def r_component(x: list[Block]):
    global offset0, offset1, main_end, m_rows
    xi = m_rows - 1
    xx = xi - 16
    while xi > main_end:
        for j in range(16):
            col0 = diagMtx_g16_w5_seed1_t36[xi & 15][0]
            col1 = diagMtx_g16_w5_seed1_t36[xi & 15][1]
            col2 = diagMtx_g16_w5_seed1_t36[xi & 15][2]
            col3 = diagMtx_g16_w5_seed1_t36[xi & 15][3]

            # if xi >= m_rows - 17:
            print(f'xi value = {x[xi]}')

            print(f'col0 = {col0}')
            print(f'col1 = {col1}')
            print(f'col2 = {col2}')
            print(f'col3 = {col3}')

            print(f'xc0 = {xx + col0}')
            print(f'xc1 = {xx + col1}')
            print(f'xc2 = {xx + col2}')
            print(f'xc3 = {xx + col3}')

            print(f'xc0 value = {x[xx + col0]}')
            print(f'xc1 value = {x[xx + col1]}')
            print(f'xc2 value = {x[xx + col2]}')
            print(f'xc3 value = {x[xx + col3]}')

            print(f'offset0 = {offset0}')
            print(f'offset1 = {offset1}')

            x[xx + col0] ^= x[xi]
            x[xx + col1] ^= x[xi]
            x[xx + col2] ^= x[xi]
            x[xx + col3] ^= x[xi]

            if offset0 >= 0:
                x[offset0] ^= x[xi]
            if offset1 >= 0:
                x[offset1] ^= x[xi]

            print(f'i = {xi}')
            print(f'x[513] = {x[513]}')
            print(f'x[514] = {x[514]}')
            print(f'x[515] = {x[515]}')
            print(f'x[516] = {x[516]}')
            print(f'x[517] = {x[517]}')
            print(f'x[518] = {x[518]}')
            print(f'x[519] = {x[519]}')

            offset0 -= 1
            offset1 -= 1
            xx -= 1
            xi -= 1


def component(m: list[Block]):
    for i in range(cols):
        print("hi")


def r_test():
    global m_rows, offset0, offset1
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mrencoder_input.txt")
    m_rows = int(fi.readline().rstrip(), 10)
    # print(m_rows)
    offset0 = int(fi.readline().rstrip(), 10)
    # print(offset0)
    offset1 = int(fi.readline().rstrip(), 10)
    # print(offset1)
    m = []
    for i in range(m_rows):
        line = fi.readline()
        m.append(Block(int("0x" + line.rstrip(), 16)))
        # print(m[i])
    fi.close()
    m_after = []
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mrencoder_output.txt")
    for i in range(m_rows):
        line = fi.readline()
        m_after.append(Block(int("0x" + line.rstrip(), 16)))
    fi.close()
    # print(m[518])
    # print(m[519])
    r_component(m)
    to = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mrencoder_component_output.txt", "w")
    result = True
    for i in range(m_rows):
        to.write(f'{m[i]} {m_after[i]}\n')
        if m[i] != m_after[i]:
            result = False
    to.close()
    print(result)
