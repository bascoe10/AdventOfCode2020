def main() -> None:
    with open('input') as f:
        rulesi, yticketi, nticketsi = f.read().split('\n\n')
        rules = {}
        for r in rulesi.split('\n'):
            name, _rule = r.split(': ')
            rules[name] = _rule.strip('\n')

        ntickets = list(map(lambda x: int(x), nticketsi.split('\n', 1)[1].strip('\n').replace('\n', ',').split(',')))
        invalid_list = []
        for x in ntickets:
            valid = False
            for r in rules:
                rule1, rule2 = rules[r].split(' or ')
                rule1 = list(map(lambda x: int(x), rule1.split('-')))
                rule2 = list(map(lambda x: int(x), rule2.split('-')))
                if (rule1[0] <= x <= rule1[1]) or (rule2[0] <= x <= rule2[1]):
                    valid = True
                    break
            if not valid:
                invalid_list.append(x)
        print(f'The ticket scanning error rate ---> {sum(invalid_list)}')
        pass


if __name__ == '__main__':
    main()
