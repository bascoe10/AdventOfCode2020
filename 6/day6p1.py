def main() -> None:
    with open('input') as f:
        groups = ""
        for line in f:
            groups += line[:-1] if line[:-1] != '' else ':'
        sum_of_counts = sum(map(lambda x: len(set(x)), groups.split(':')))
        print(f'Sum of counts --> {sum_of_counts}')


if __name__ == '__main__':
    main()
