def main() -> None:
    displacement = {'E': 0, 'W': 0, 'N': 0, 'S': 0}
    bearing = {0: 'E', 90: 'N', 180: 'W', 270: 'S'}
    # bearing = {'E': 'east', 'N': 'north', 'W': 'west', : 'south'}
    current_direction = 'E'
    current_orientation = 0
    with open('input') as f:
        for instr in f:
            code_n_arg = list(instr.strip('\n'))
            code = code_n_arg[0]
            arg = int(''.join(code_n_arg[1:]))

            if code == 'R':
                current_orientation = (current_orientation - arg) % 360
                current_direction = bearing[current_orientation]
            elif code == 'L':
                current_orientation = (current_orientation + arg) % 360
                current_direction = bearing[current_orientation]
            else:
                direction = current_direction if code == 'F' else code
                displacement[direction] += arg
    east_west = displacement['E'] - displacement['W']
    east_west = east_west if east_west > 0 else (-1 * east_west)
    north_south = displacement['N'] - displacement['S']
    north_south = north_south if north_south > 0 else (-1 * north_south)

    print(f'The Manhattan distance is --> {east_west + north_south}')


if __name__ == '__main__':
    main()
