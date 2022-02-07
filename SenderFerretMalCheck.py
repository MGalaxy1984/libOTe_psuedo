from Block import Block

sum0 = Block(0)
sum1 = Block(0)

X = Block(0)


def pre_component():
    global X
    X = Block(0x924b386ad40e07a50f94cb208ccf82a5)


def component(m, xx):
    """
    :param m: vector mB
    :param xx: a block received from receiver side
    :return:
    """
    global sum0, sum1
    assert isinstance(m, list)
    assert isinstance(xx, Block)
    to = open("/home/mgalaxy/workspace/libOTe_component_files/sender_ferretMalCheck_component_middle.txt", "w")
    for i in range(len(m)):
        low = Block(0)
        high = Block(0)
        # print(f'xx = {xx}')
        # print(f'm[i] = {m[i]}')
        # print(f'low = {low}')
        # print(f'high = {high}')
        to.write(f'xx = {xx}\n')
        to.write(f'm[i] = {m[i]}\n')
        to.write(f'low = {low}\n')
        to.write(f'high = {high}\n')
        xx.gf_128_mul(m[i], low, high)
        # print(f'low1 = {low}')
        # print(f'high1 = {high}')
        to.write(f'low1 = {low}\n')
        to.write(f'high1 = {high}\n')
        sum0 = sum0 ^ low
        sum1 = sum1 ^ high
        # print(f'xx1 = {xx}')
        # print(f'X = {X}')
        to.write(f'xx1 = {xx}\n')
        to.write(f'X = {X}\n')
        xx = xx.gf_128_mul(X, Block(), Block())
        # print(f'xx2 = {xx}')
        to.write(f'xx2 = {xx}\n')
    to.close()


def after_component():
    my_sum = sum0.gf_128_reduce(sum1)
    print(f"my_sum = {my_sum}")


def test():
    fi = open("/home/mgalaxy/workspace/libOTe_component_files/sender_ferretMalCheck_input.txt")
    xx = Block(int("0x" + fi.readline().rstrip(), 16))
    global X
    X = Block(xx)
    n = 0
    m = []
    while True:
        line = fi.readline()
        if not line:
            break
        m.append(Block(int("0x" + line.rstrip(), 16)))
        n += 1

    print(f"n = {n}")

    component(m, xx)

    print(f"sum0 = {sum0}")
    print(f"sum1 = {sum1}")

    after_component()
