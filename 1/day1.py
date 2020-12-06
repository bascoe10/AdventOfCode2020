

def main() -> None:
    with open('input.txt') as f:
        lines = list(map(lambda x: int(x), f.readlines()))
        for line in lines:
            for oline in lines[lines.index(line)+1:]:
                if (line + oline) == 2020:
                    print(f'Possible Candidate {line}, {oline} --> {line * oline}')


if __name__ == '__main__':
    main()
