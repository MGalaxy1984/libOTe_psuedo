from Block import Block

sum0 = Block(0)
sum1 = Block(1)


def component(m, x):
    """

    :param m: vector mB
    :param x: a block received from receiver side
    :return:
    """
    global sum0, sum1
    assert isinstance(m, list)
    assert isinstance(x, Block)
    for i in range(len(m)):
        low = Block(0x2e1f7bead0091ffea831e7d7a0a45f2e)
        high = Block(0x4cad407b310aac870d1d3eaafc588908)
        x.gf_128_mul_1(m[i], low, high)
        print(f'm[i] = {m[i]}')
        print(f'low = {low}')
        print(f'high = {high}')
        sum0 = sum0 ^ low
        sum1 = sum1 ^ high
        # x = x.gf_128_mul_1(x)


def test():
    m = [Block(0xca70abbe9b5b27d2181c226f0b025b09)]
    xx = Block(0x850e65a5333282444f185a3b38d5944a)
    component(m, xx)
