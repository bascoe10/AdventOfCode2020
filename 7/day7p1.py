import re


def main() -> None:
    rules = {}
    with open('input') as f:
        for line in f:
            pline = line[:-1].replace(' contain no other bags.', '')
            pline = re.sub(r'contain\ [0-9]', '', pline)
            pline = re.sub(r',\ [0-9]', '', pline)
            pline = re.sub(r'bag(s*)(\.*)', 'bag', pline).split('bag')[:-1]
            for bag in pline[1:]:
                if bag.strip() in rules:
                    if pline[0].strip() not in rules[bag.strip()]:
                        rules[bag.strip()].add(pline[0].strip())
                else:
                    rules[bag.strip()] = set([pline[0].strip()])

    all_list = []
    x = set(['shiny gold'])
    while len(x) > 0:
        current = x.pop()
        if current not in rules:
            continue
        all_list += rules[current]
        if len(rules[current]) > 0:
            x = x.union(rules[current])
    print(f'The total bags that can hold shiny gold ---> {len(set(all_list))}')


if __name__ == '__main__':
    main()
