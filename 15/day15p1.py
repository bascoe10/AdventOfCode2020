def main() -> None:
    starting = {9: [1], 19: [2], 1: [3], 6: [4], 0: [5], 5: [6], 4: [7]}
    numbers_spoken = [9, 19, 1, 6, 0, 5, 4]

    last_number = numbers_spoken[-1]
    sn = 2020 - len(numbers_spoken)

    for _ in range(sn):
        if len(starting[last_number]) == 1:
            last_number = 0
        else:
            pult, ult = starting[last_number][-2:]
            last_number = ult - pult
        numbers_spoken.append(last_number)
        if last_number in starting:
            starting[last_number].append(len(numbers_spoken))
        else:
            starting[last_number] = [len(numbers_spoken)]

    print(f'The 2020th entry is --> {last_number}')


if __name__ == '__main__':
    main()
