def valid_input(preamble, inpt) -> bool:
    found = False
    for i in range(len(preamble)):
        if found:
            break
        for j in range(i+1, len(preamble)):
            if preamble[i] + preamble[j] == inpt:
                found = True
                break
    return found


def main() -> None:
    with open('input') as f:
        input_stream = list(map(lambda x: int(x[:-1]), f))

    preamble_length = 25
    current_index = preamble_length
    for inpt in input_stream[preamble_length:]:
        preamble = input_stream[current_index-preamble_length:current_index]
        if not valid_input(preamble, inpt):
            print(f'Wrong input --> {inpt}')
            break
        current_index += 1


if __name__ == '__main__':
    main()
