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

rows = 0
r_cols = 0
l_cols = 0
v = []

offset0 = 0
offset1 = 0


def r_component(x: list[Block]):
    global offset0, offset1, main_end, rows
    xi = rows - 1
    xx = xi - 16
    while xi > main_end:
        for j in range(16):
            col0 = diagMtx_g16_w5_seed1_t36[xi & 15][0]
            col1 = diagMtx_g16_w5_seed1_t36[xi & 15][1]
            col2 = diagMtx_g16_w5_seed1_t36[xi & 15][2]
            col3 = diagMtx_g16_w5_seed1_t36[xi & 15][3]

            # print(f'xi value = {x[xi]}')
            #
            # print(f'col0 = {col0}')
            # print(f'col1 = {col1}')
            # print(f'col2 = {col2}')
            # print(f'col3 = {col3}')
            #
            # print(f'xc0 = {xx + col0}')
            # print(f'xc1 = {xx + col1}')
            # print(f'xc2 = {xx + col2}')
            # print(f'xc3 = {xx + col3}')
            #
            # print(f'xc0 value = {x[xx + col0]}')
            # print(f'xc1 value = {x[xx + col1]}')
            # print(f'xc2 value = {x[xx + col2]}')
            # print(f'xc3 value = {x[xx + col3]}')
            #
            # print(f'offset0 = {offset0}')
            # print(f'offset1 = {offset1}')

            x[xx + col0] ^= x[xi]
            x[xx + col1] ^= x[xi]
            x[xx + col2] ^= x[xi]
            x[xx + col3] ^= x[xi]

            if offset0 >= 0:
                x[offset0] ^= x[xi]
            if offset1 >= 0:
                x[offset1] ^= x[xi]

            # print(f'i = {xi}')
            # print(f'x[513] = {x[513]}')
            # print(f'x[514] = {x[514]}')
            # print(f'x[515] = {x[515]}')
            # print(f'x[516] = {x[516]}')
            # print(f'x[517] = {x[517]}')
            # print(f'x[518] = {x[518]}')
            # print(f'x[519] = {x[519]}')

            offset0 -= 1
            offset1 -= 1
            xx -= 1
            xi -= 1

    while xi >= 0:
        # print(xi)
        # print(f'xi = {xi}')
        for j in range(4):
            col = diagMtx_g16_w5_seed1_t36[xi & 15][j] + xi - 16
            if col >= 0:
                # print(f'col = {col}')
                x[col] ^= x[xi]
        if offset0 >= 0:
            x[offset0] ^= x[xi]
            offset0 -= 1
        if offset1 >= 0:
            x[offset1] ^= x[xi]
            offset1 -= 1
        xi -= 1


def l_component(ppp: list[Block], mm: list[Block]):
    global l_cols, rows, v
    i = 0
    # print(f'cols = {cols}')
    while i < l_cols:
        end = l_cols
        for j in range(5):
            if v[j] == rows:
                v[j] = 0
            j_end = l_cols - v[j] + i
            end = min(end, j_end)
        # print(f'v0 = {v[0]}')
        # print(f'v1 = {v[1]}')
        # print(f'v2 = {v[2]}')
        # print(f'v3 = {v[3]}')
        # print(f'v4 = {v[4]}')
        tmp_i = i
        m0 = v[0]
        m1 = v[1]
        m2 = v[2]
        m3 = v[3]
        m4 = v[4]
        v[0] += end - i
        v[1] += end - i
        v[2] += end - i
        v[3] += end - i
        v[4] += end - i
        i = end
        while tmp_i != end:
            # print(f'tmp_i = {tmp_i}')
            # print(f'm0 = {m0}')
            # print(f'm1 = {m1}')
            # print(f'm2 = {m2}')
            # print(f'm3 = {m3}')
            # print(f'm4 = {m4}')
            ppp[tmp_i] = ppp[tmp_i] ^ mm[m0] ^ mm[m1] ^ mm[m2] ^ mm[m3] ^ mm[m4]
            m0 += 1
            m1 += 1
            m2 += 1
            m3 += 1
            m4 += 1
            tmp_i += 1


def component(m: list[Block]):
    ppp = m[0: r_cols - rows]
    mm = m[r_cols - rows: r_cols]
    r_component(mm)
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_encoder_middle.txt")
    m_middle = []
    for i in range(r_cols):
        line = fi.readline()
        m_middle.append(Block(int("0x" + line.rstrip(), 16)))
    m_comp_middle = ppp + mm
    middle_result = True
    for i in range(r_cols):
        if m_comp_middle[i] != m_middle[i]:
            middle_result = False
            print(f'after right encoder, index {i} is different')
    print(f'middle_result = {middle_result}')
    l_component(ppp, mm)
    return ppp + mm


def test():
    global rows, r_cols, l_cols, v, offset0, offset1
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_encoder_input.txt")
    r_cols = int(fi.readline().rstrip(), 10)
    print(r_cols)
    rows = int(fi.readline().rstrip(), 10)
    print(rows)
    m = []
    for i in range(r_cols):
        line = fi.readline()
        m.append(Block(int("0x" + line.rstrip(), 16)))
    fi.close()
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_encoder_r_input.txt")
    offset0 = int(fi.readline().rstrip(), 10)
    offset1 = int(fi.readline().rstrip(), 10)
    fi.close()
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_encoder_l_input.txt")
    v_size = int(fi.readline().rstrip(), 10)
    for i in range(v_size):
        v.append(int(fi.readline().rstrip(), 10))
        # print(v[i])
    l_cols = int(fi.readline().rstrip(), 10)
    fi.close()
    m_after = []
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_encoder_output.txt")
    for i in range(r_cols):
        line = fi.readline()
        m_after.append(Block(int("0x" + line.rstrip(), 16)))
    fi.close()

    m = component(m)

    result = True
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_encoder_component_output.txt", "w")
    for i in range(r_cols):
        if m[i] != m_after[i]:
            result = False
            print(f'index {i} is different')
        fi.write(f'{m[i]} {m_after[i]}\n')
    print(result)


def l_test():
    global rows, r_cols, v
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mlencoder_input.txt")
    v_size = int(fi.readline().rstrip(), 10)
    for i in range(v_size):
        v.append(int(fi.readline().rstrip(), 10))
    ppp = []
    mm = []
    rows = int(fi.readline().rstrip(), 10)
    r_cols = int(fi.readline().rstrip(), 10)
    for i in range(rows):
        line = fi.readline()
        ppp.append(Block(int("0x" + line.rstrip(), 16)))
    for i in range(r_cols):
        line = fi.readline()
        mm.append(Block(int("0x" + line.rstrip(), 16)))

    l_component(ppp, mm)

    ppp_after = []
    mm_after = []
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mlencoder_output.txt")
    for i in range(rows):
        line = fi.readline()
        ppp_after.append(Block(int("0x" + line.rstrip(), 16)))
    for i in range(r_cols):
        line = fi.readline()
        mm_after.append(Block(int("0x" + line.rstrip(), 16)))
    fi.close()

    to = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mlencoder_component_output.txt", "w")
    result = True
    for i in range(rows):
        to.write(f'{ppp[i]}\n')
        if ppp[i] != ppp_after[i]:
            result = False
    for i in range(r_cols):
        to.write(f'{mm[i]}\n')
        if mm[i] != mm_after[i]:
            result = False
    to.close()
    print(result)


def r_test():
    global rows, offset0, offset1
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mrencoder_input.txt")
    rows = int(fi.readline().rstrip(), 10)
    # print(m_rows)
    offset0 = int(fi.readline().rstrip(), 10)
    # print(offset0)
    offset1 = int(fi.readline().rstrip(), 10)
    # print(offset1)
    m = []
    for i in range(rows):
        line = fi.readline()
        m.append(Block(int("0x" + line.rstrip(), 16)))
        # print(m[i])
    fi.close()
    m_after = []
    fi = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mrencoder_output.txt")
    for i in range(rows):
        line = fi.readline()
        m_after.append(Block(int("0x" + line.rstrip(), 16)))
    fi.close()
    # print(m[518])
    # print(m[519])
    r_component(m)
    to = open("E:\PycharmProjects\libOTe_psuedo\DataFiles\sender_mrencoder_component_output.txt", "w")
    result = True
    for i in range(rows):
        to.write(f'{m[i]} {m_after[i]}\n')
        if m[i] != m_after[i]:
            result = False
    to.close()
    print(result)
