def main() -> None:
    with open('input') as f:
        groups = ""
        for line in f:
            groups += ';' + line[:-1] if line[:-1] != '' else ':'

        grand_total = 0
        for group in groups.split(':'):
            persons_count = len(group.split(';')) - 1
            group_questions = set(group.replace(';', ''))
            group_total = sum(map(lambda x: 1 if group.count(x) == persons_count else 0, group_questions))
            grand_total += group_total

        print(f'Sum of counts --> {grand_total}')


if __name__ == '__main__':
    main()
