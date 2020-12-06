def valid_password(countr, letter, password):
    _min, _max = map(lambda x: int(x), countr.split('-'))
    letter = letter[:-1]
    lcount = password.count(letter)
    return True if _min <= lcount <= _max else False


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
