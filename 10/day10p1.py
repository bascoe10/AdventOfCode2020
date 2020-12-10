def main() -> None:
    with open('input') as f:
        adapters = list(map(lambda x: int(x.strip('\n')), f))
        adapters.append(0)
        adapters.sort()
        adapters.append(adapters[-1]+3)
        count_1 = 0
        count_3 = 0
        for i in range(len(adapters)-1):
            diff = adapters[i+1] - adapters[i]
            if diff == 1:
                count_1 += 1
            elif diff == 3:
                count_3 += 1
        print(f'There are {count_1} differences of 1 jolt and {count_3} differences of 3 jolts --> {count_1 * count_3}')


if __name__ == '__main__':
    main()
