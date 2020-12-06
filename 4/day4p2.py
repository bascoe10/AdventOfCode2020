
def validate_passport(passport_str) -> bool:
    passport_str = passport_str.strip(' ')
    passport = dict(map(lambda x: x.split(':'), passport_str.split(' ')))

    valid = True
    for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        valid = valid and (field in passport)
        if not valid:
            break
        if field == 'byr':
            valid = valid and (1920 <= int(passport[field]) <= 2002)
        elif field == 'iyr':
            valid = valid and (2010 <= int(passport[field]) <= 2020)
        elif field == 'eyr':
            valid = valid and (2020 <= int(passport[field]) <= 2030)
        elif field == 'hgt':
            if 'cm' in passport[field]:
                valid = valid and (150 <= int(passport[field].rstrip('cm')) <= 193)
            elif 'in' in passport[field]:
                valid = valid and (59 <= int(passport[field].rstrip('in')) <= 76)
            else:
                valid = False
        elif field == 'hcl':
            valid = valid and passport[field].startswith('#')
            try:
                int(passport[field][1:], 16)
            except ValueError:
                valid = False

        elif field == 'ecl':
            valid = valid and (passport[field] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'))
        elif field == 'pid':
            valid = valid and (len(passport[field]) == 9)

    return valid


def main() -> None:
    valid = 0
    passport_str = ""
    with open('input.txt') as f:
        for line in f:
            if line[:-1] == "":
                if validate_passport(passport_str):
                    valid += 1
                passport_str = ""
            else:
                passport_str += " " + line[:-1]
        if validate_passport(passport_str):
            valid += 1
    print(f'There are {valid} passports')


if __name__ == '__main__':
    main()
