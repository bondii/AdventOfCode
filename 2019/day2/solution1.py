file = open('input')

opcodes = [int(x) for x in file.read().split(',')]
opcodes[1] = 12
opcodes[2] = 2

for i in range(0, len(opcodes), 4):
    opcode = opcodes[i]
    if opcode == 99:
        print('Value at postition 0:', opcodes[0])
        exit()

    # The three integers immediately after the opcode tell you three positions,
    # the first two indicate the positions from which you should read the input
    # values, and the third indicates the position at which the output should
    # be stored.
    pos1 = opcodes[i+1]
    pos2 = opcodes[i+2]
    pos3 = opcodes[i+3]
    if opcode == 1:
        # Opcode 1 adds together numbers read from two positions and stores the
        # result in a third position.
        opcodes[pos3] = opcodes[pos1] + opcodes[pos2]
    elif opcode == 2:
        # Opcode 2 works exactly like opcode 1, except it multiplies the two
        # inputs instead of adding them.
        opcodes[pos3] = opcodes[pos1] * opcodes[pos2]
    else:
        print('Oh no, something must have gone wrong, got opcode', opcode)
        exit()

print('Oh no, something must have gone wrong, ',
      'the program never reached opcode 99!..')
