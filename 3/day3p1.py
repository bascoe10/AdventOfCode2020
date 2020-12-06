
def main() -> None:
    x = 0
    trees_encounter = 0
    with open('input.txt') as f:
        for line in f:
            if line[x] == '#':
                trees_encounter += 1
            x += 3
            x = x % (len(line) - 1)
    print(f'Tree encountered -- {trees_encounter}')


if __name__ == '__main__':
    main()
