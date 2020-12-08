
INSTRUCTIONS = []


def instructions_loop():
    instruction_pointer = 0
    accumulator = 0
    instructions_executed = []

    while instruction_pointer not in instructions_executed and instruction_pointer < len(INSTRUCTIONS):
        instruction, arg = INSTRUCTIONS[instruction_pointer]
        instructions_executed.append(instruction_pointer)

        if instruction == 'acc':
            accumulator += int(arg[1:]) if arg[0] == '+' else (int(arg[1:]) * -1)
        elif instruction == 'jmp':
            instruction_pointer += int(arg[1:]) if arg[0] == '+' else (int(arg[1:]) * -1)
            continue

        instruction_pointer += 1
    return accumulator if instruction_pointer == len(INSTRUCTIONS) else -1


def main() -> None:
    global INSTRUCTIONS
    with open('input') as f:
        INSTRUCTIONS += list(map(lambda x: x.strip('\n').split(' '), f.readlines()))
        accumulator = 0
        for instr in INSTRUCTIONS:
            if instr[0] == 'jmp':
                res = instructions_loop()
                if res != -1:
                    accumulator = res
                    break

                instr[0] = 'nop'
                res = instructions_loop()
                instr[0] = 'jmp'
                if res != -1:
                    accumulator = res
                    break
            elif instr[0] == 'nop':
                res = instructions_loop()
                if res != -1:
                    accumulator = res
                    break

                instr[0] = 'jmp'
                res = instructions_loop()
                instr[0] = 'nop'
                if res != -1:
                    accumulator = res
                    break

        print(f'The value of the accumulator is --> {accumulator}')


if __name__ == '__main__':
    main()
