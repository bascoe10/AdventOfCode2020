def valid_password(positions, letter, password):
    first, second = map(lambda x: int(x) - 1, positions.split('-'))
    letter = letter[:-1]
    p1 = password[first] == letter
    p2 = password[second] == letter

    if p1 == p2:
        return False
    return True


def main():
    valid = 0
    with open('input.txt') as f:
        lines = map(lambda x: x.split(' '), f.readlines())
        for line in lines:
            if valid_password(*line):
                valid += 1

    print(f'Valid Password Count {valid}')


if __name__ == '__main__':
    main()
