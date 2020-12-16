from collections import OrderedDict

def main() -> None:
    # starting = {9: [], 19: [], 1: [], 6: [], 0: [], 5: [], 4: [], }
    #starting = OrderedDict({1: [1], 3: [2], 2: [3]})
    starting = OrderedDict({0: [1], 3: [2], 6: [3]})
    numbers_spoken = starting.keys()[:]
    last_number = None
    for _ in range(2020):
        last_number = starting.keys()[-1]
        if len(starting[last_number] == 1):
            numbers_spoken.append(0)
            starting[last_number].append(len(numbers_spoken))
        else:
            ult, pult = starting[last_number]



if __name__ == '__main__':
    main()
