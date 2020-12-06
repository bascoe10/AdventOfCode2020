
def compute_number(line) -> int:
    _line = list(line)
    _line.reverse()
    _sum = sum(map(lambda i: (2 ** i) if _line[i] in ['R', 'B'] else (-2 ** i), range(len(line))))
    return int((2**len(line) + _sum)/2)


def main() -> None:
    with open('input.txt') as f:
        seat_ids = map(lambda line: compute_number(line[:-4]) * 8 + compute_number(line[-4:-1]), f)
        slist = list(seat_ids)
        slist.sort()
        for i in range(len(slist) - 1):
            if slist[i+1] != slist[i]+1:
                print(f'Seat found --> {slist[i]+1}')


if __name__ == '__main__':
    main()
