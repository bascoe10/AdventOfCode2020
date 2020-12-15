def mask_value(mask, value):
    value = ('0' * (len(mask) - len(value))) + value
    rt_value = ''
    for i in range(len(value) - 1, -1, -1):
        if mask[i] == 'X':
            rt_value = value[i] + rt_value
        else:
            rt_value = mask[i] + rt_value
    return rt_value


def main() -> None:
    with open('input') as f:
        mask = ''
        mem = {}
        for line in f:
            code, arg = line.strip('\n').split(' = ')
            if code == 'mask':
                mask = arg
            else:
                binary = bin(int(arg))[2:]
                mem[code[4:-1]] = int(mask_value(mask, binary), 2)

        sum = 0
        for entry in mem:
            sum += mem[entry]

        print(f'The sum of the memory is --> {sum}')


if __name__ == '__main__':
    main()
