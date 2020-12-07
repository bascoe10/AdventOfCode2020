import re


def rcount(rules, key) -> int:
    bags_contain = rules[key]
    if len(bags_contain) == 0 or (len(bags_contain) == 1 and bags_contain[0][0] == 'no'):
        return 0
    return sum(map(lambda x: int(x[0]) + (int(x[0]) * rcount(rules, x[1])), bags_contain))


def main() -> None:
    rules = {}
    with open('input') as f:
        for line in f:
            pline = re.sub(r'\ contain\ no\ other\ bags\.', '', line[:-1])
            pline = re.sub(r'contain', '', pline)
            pline = re.sub(r',', '', pline)
            pline = re.sub(r'bag(s*)(\.*)', 'bag', pline).split('bag')[:-1]

            rules[pline[0].strip()] = list(map(lambda x: x.strip().split(' ', 1), pline[1:]))

    total = rcount(rules, 'shiny gold')
    print(f'The total bags that can hold shiny gold ---> {total}')


if __name__ == '__main__':
    main()
