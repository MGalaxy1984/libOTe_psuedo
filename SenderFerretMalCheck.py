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
    low = Block(0xe8f5639ab50affe9234f3c9ef8ca0391)
    high = Block(0x0da7a5d09839a464fecd0ca06df279e4)
    for i in range(len(m)):
        print(f'xx = {xx}')
        print(f'm[i] = {m[i]}')
        print(f'low = {low}')
        print(f'high = {high}')
        xx.gf_128_mul(m[i], low, high)
        print(f'low1 = {low}')
        print(f'high1 = {high}')
        sum0 = sum0 ^ low
        sum1 = sum1 ^ high
        print(f'xx1 = {xx}')
        print(f'X = {X}')
        xx = xx.gf_128_mul(X, Block(), Block())
        print(f'xx2 = {xx}')


def test():
    pre_component()

    m = [Block(0xf54c69324966dd79558149f508e228b5), Block(0xe861fa3f9ac373619ba0113f8c739fe0)]
    xx = Block(0xb942a4af19fcf2f7ce56aa8f52595323)
    component(m, xx)
