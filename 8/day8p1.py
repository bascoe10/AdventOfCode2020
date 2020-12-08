def main() -> None:
    with open('input') as f:
        instructions = list(map(lambda x: x.strip('\n').split(' '), f.readlines()))
        instruction_pointer = 0
        accumulator = 0
        instructions_executed = []

        while instruction_pointer not in instructions_executed:
            instruction, arg = instructions[instruction_pointer]
            instructions_executed.append(instruction_pointer)

            if instruction == 'acc':
                accumulator += int(arg[1:]) if arg[0] == '+' else (int(arg[1:]) * -1)
            elif instruction == 'jmp':
                instruction_pointer += int(arg[1:]) if arg[0] == '+' else (int(arg[1:]) * -1)
                continue

            instruction_pointer += 1

        print(f'The value of the accumulator is --> {accumulator}')


if __name__ == '__main__':
    main()
