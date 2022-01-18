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
        low = Block()
        high = Block()
        x.gf_128_mul(m[i], low, high)
        sum0 = sum0 ^ low
        sum1 = sum1 ^ high
        x = x.gf_128_mul_1(x)
