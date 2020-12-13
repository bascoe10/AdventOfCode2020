from copy import deepcopy

seat_layout = []


def look_diagonally(row, col):
    start_x = 0
    start_y = 0
    if row > col:
        start_y = row - col
    else:
        start_x = col - row

    while start_x < len(seat_layout[0]) and start_y < len(seat_layout):


def count_filled(row, col) -> str:
    p1, p2, p3, p4, p5, p6, p7, p8 = None
    for i in range(len(seat_layout)):
        offset = row - i
        if row == 0:
            p


    return filled


def rule_pass() -> bool:
    global seat_layout
    no_change = True
    temp_layout = []
    for row in range(len(seat_layout)):
        temp_layout.append([])
        for col in range(len(seat_layout[0])):
            seat = seat_layout[row][col]
            adj_seats = count_filled(row, col)
            if seat == 'L' and adj_seats == 0:
                no_change = False
                temp_layout[row].append('#')
            elif seat == '#' and adj_seats >= 4:
                no_change = False
                temp_layout[row].append('L')
            else:
                temp_layout[row].append(seat)
    seat_layout = deepcopy(temp_layout)
    return no_change


def main() -> None:
    global seat_layout
    with open('input') as f:
        seat_layout = list(map(lambda x: list(x[:-1]), f))
        passes = 0
        while not rule_pass():
            passes += 1

        print(passes)

        occupied = 0
        for row in seat_layout:
            for col in row:
                occupied += 1 if col == '#' else 0

        print(f'There are {occupied} occupied seats')


if __name__ == '__main__':
    main()
