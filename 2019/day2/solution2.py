file = open('input')

orig_opcodes = [int(x) for x in file.read().split(',')]

INPUT_RANGE = 100

for noun in range(INPUT_RANGE):
    for verb in range(INPUT_RANGE):
        opcodes = orig_opcodes.copy()
        opcodes[1] = noun
        opcodes[2] = verb
        for i in range(0, len(opcodes), 4):
            opcode = opcodes[i]
            if opcode == 99:
                if opcodes[0] == 19690720:
                    print('The answer is:', (100*noun + verb))
                    exit()
                break

            # The three integers immediately after the opcode tell you three
            # positions, the first two indicate the positions from which you
            # should read the input values, and the third indicates the
            # position at which the output should be stored.
            pos1 = opcodes[i+1]
            pos2 = opcodes[i+2]
            pos3 = opcodes[i+3]
            if opcode == 1:
                # Opcode 1 adds together numbers read from two positions and
                # stores the result in a third position.
                opcodes[pos3] = opcodes[pos1] + opcodes[pos2]
            elif opcode == 2:
                # Opcode 2 works exactly like opcode 1, except it multiplies
                # the two inputs instead of adding them.
                opcodes[pos3] = opcodes[pos1] * opcodes[pos2]
            else:
                print('Oh no, something went wrong, got opcode', opcode)
                exit()

print('Oh no, something must have gone wrong, ',
      'the program never reached opcode 99!..')
