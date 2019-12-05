file = open('input')

path = [[(x[0], int(x[1:])) for x in file.readline().split(',')],
        [(x[0], int(x[1:])) for x in file.readline().split(',')]]

hasPassed = (set(), set())


def traversePath(walker):
    x = 0
    y = 0
    for direction, step in path[walker]:
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


traversePath(0)
traversePath(1)
minDist = 1e9
for location in hasPassed[0]:
    if location in hasPassed[1]:
        minDist = min(minDist, (abs(location[0]) + abs(location[1])))

if minDist != 1e9:
    print('The manhattan distance from the central port to the closest ',
          'intersection is:', minDist)
else:
    print('No intersection found')
