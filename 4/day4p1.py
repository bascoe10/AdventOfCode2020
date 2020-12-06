
def validate_passport(passport_str) -> bool:
    valid = True
    for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        valid = valid and (field in passport_str)
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
