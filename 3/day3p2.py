
def compute_trees_encounters(x, y) -> int:
    step = 0
    skip = y
    trees_encounter = 0
    with open('input.txt') as f:
        for line in f:
            if skip != y:
                if skip == 1:
                    skip = y
                continue

            if line[step] == '#':
                trees_encounter += 1
            step += x
            step = step % (len(line) - 1)

            if skip > 1:
                skip -= 1
    return trees_encounter


def main() -> None:
    total = 1
    for arg in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        total *= compute_trees_encounters(*arg)
    print(f'Tree encountered -- {total}')


if __name__ == '__main__':
    main()
