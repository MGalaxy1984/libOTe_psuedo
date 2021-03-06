import sys

SEED_SIZE = 16
GENERATOR = 223
MODULUS = 36389

FUNCTION_L = lambda x: x ** 2 - 2 * x + 1


def function_H(first_half, second_half):
    print(int(first_half, 2))
    mod_exp = bin(pow(GENERATOR, int(first_half, 2), MODULUS)).replace('0b', '').zfill(SEED_SIZE)
    hard_core_bit = 0
    for i in range(len(first_half)):
        hard_core_bit = (hard_core_bit ^ (int(first_half[i]) & int(second_half[i]))) % 2
    print(len(mod_exp))
    return mod_exp + second_half + str(hard_core_bit)


def function_G(initial_seed):
    binary_string = initial_seed
    result = ''
    for i in range(FUNCTION_L(SEED_SIZE)):
        first_half = binary_string[:len(binary_string) // 2]
        second_half = binary_string[len(binary_string) // 2:]
        binary_string = function_H(first_half, second_half)
        print(f'{binary_string} len = {len(binary_string)}')
        result += binary_string[-1]
        binary_string = binary_string[:-1]
    return result


def main():
    if len(sys.argv) >= 2:
        seed = str(sys.argv[1])
        if len(seed) > SEED_SIZE:
            print("Inital seed too long: change the seed or set a new SEED_SIZE")
            sys.exit(1)
        output = function_G(seed)
        print("The seed produced the following binary string: ")
        print(output)
        print("SIZE:", SEED_SIZE, "->", FUNCTION_L(SEED_SIZE))
        sys.exit(0)
    else:
        print("Insert one argument for initial seed.")
        sys.exit(1)


def function_h_test():
    h_in = "1001011011010011"
    result = function_H(h_in[:len(h_in) // 2], h_in[len(h_in) // 2:])
    print(result)


if __name__ == '__main__':
    main()
    # function_h_test()
