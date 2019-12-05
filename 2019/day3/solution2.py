file = open('input')

path = [[(x[0], int(x[1:])) for x in file.readline().split(',')],
        [(x[0], int(x[1:])) for x in file.readline().split(',')]]

stepsTakenTo = ({}, {})


def traversePath(walker):
    x = 0
    y = 0
    stepsTaken = 0
    for direction, step in path[walker]:
        if direction == 'R':
            for i in range(step):
                stepsTaken += 1
                x += 1
                if (x, y) not in stepsTakenTo[walker]:
                    stepsTakenTo[walker][(x, y)] = stepsTaken
        elif direction == 'L':
            for i in range(step):
                stepsTaken += 1
                x -= 1
                if (x, y) not in stepsTakenTo[walker]:
                    stepsTakenTo[walker][(x, y)] = stepsTaken
        elif direction == 'U':
            for i in range(step):
                stepsTaken += 1
                y += 1
                if (x, y) not in stepsTakenTo[walker]:
                    stepsTakenTo[walker][(x, y)] = stepsTaken
        elif direction == 'D':
            for i in range(step):
                stepsTaken += 1
                y -= 1
                if (x, y) not in stepsTakenTo[walker]:
                    stepsTakenTo[walker][(x, y)] = stepsTaken
        else:
            print('Error error, bipetibof, turning off')
            exit()


traversePath(0)
traversePath(1)
minSteps = 1e9
for location in stepsTakenTo[0].keys():
    if location in stepsTakenTo[1]:
        minSteps = min(minSteps,
                       stepsTakenTo[0][location] + stepsTakenTo[1][location])

if minSteps != 1e9:
    print('The fewest combined steps the wires must take to reach an',
          'intersection is:', minSteps)
else:
    print('No intersection found')
