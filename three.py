ORIGIN = (0,0)


def get_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def get_wire_points(moves):

    y, x = ORIGIN
    points = []

    for move in moves:
        way = move[0]
        steps = int(move[1:])

        for i in range(steps):

            if way == 'R':
                x += 1
            elif way == 'U':
                y -= 1
            elif way == 'D':
                y += 1
            elif way == 'L':
                x -= 1
            else:
                raise Exception(way)

            points.append((y,x))

    return points


def get_wires(file_lines):
    wires = []
    for moves in file_lines:
        moves = moves.split(',')
        wire = get_wire_points(moves)
        wires.append(wire)
    return wires


def get_exes(wires):
    exes = []
    seen = set()
    for wire in wires:
        for point in set(wire): # Making sure it doesnt intersect with itself
            if point in seen:
                exes.append(point)
            else:
                seen.add(point)
    return exes


def find_step(ex, wire):
    for num, point in enumerate(wire, start=1):
        if ex == point:
            return num
    return 0


def find_steps(ex, wires):
    steps = 0
    for wire in wires:
        if ex in wire: # Ineffecient, should use set here
            steps += find_step(ex, wire)
    return steps


with open('input.txt') as fh:
    lines = fh.read().splitlines()

wires = get_wires(lines)
exes = get_exes(wires)

print('Part 1')
print(min([get_distance(ex, ORIGIN) for ex in exes]))

print('\nPart 2')
print(min([find_steps(ex, wires) for ex in exes]))
    






