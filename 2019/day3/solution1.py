file = open('input')

path1 = [(x[0], int(x[1:])) for x in file.readline().split(',')]
path2 = [(x[0], int(x[1:])) for x in file.readline().split(',')]

hasPassed = [set((0, 0)), set((0, 0))]


def traversePath(walker):
    x = 0
    y = 0
    for direction, step in path1:
        if direction == 'R':
            for i in range(step):
                x += 1
                hasPassed[walker].add((x, y))
        elif direction == 'L':
            for i in range(step):
                x -= 1
                hasPassed[walker].add((x, y))
        elif direction == 'U':
            for i in range(step):
                y += 1
                hasPassed[walker].add((x, y))
        elif direction == 'D':
            for i in range(step):
                y -= 1
                hasPassed[walker].add((x, y))
        else:
            print('Error error, bipetibof, turning off')
            exit()


