from collections import defaultdict

def find_total_steps(steps_list):
    hello = {}
    for step in reversed(steps_list): # Reversed because it's first occurance not last to overwrite with
        hello[step[0]] = step[1]
    return sum(hello.values())

def get_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def print_grid(o, g):
    size = 2000
    x,y = o
    x -= size
    y -= size
    for i in range(size*2):
        for j in range(size*2):
            #print(y+i, x+j)
            print(grid[y+i][x+j], end='')
        print()


with open('input3.txt') as fh:
    wires = fh.read().splitlines()


size = 20000
grid = []
for i in range(size):
    grid.append(list(size * '.'))

origin = (int(size/2), int(size/2))
x, y = origin
grid[y][x] = 'o'
exes = []
which_wire = {}
steps = defaultdict(list)
for label, wire in enumerate(wires):
    wire = wire.split(',')
    x, y = origin
    num_steps = 0
    for path in wire:
        letter = path[0]
        num = int(path[1:])

        for i in range(num):
            num_steps += 1
            if letter == 'R':
                x += 1
                mark = '-'
            elif letter == 'U':
                y -= 1
                mark = '|'
            elif letter == 'D':
                y += 1
                mark = '|'
            elif letter == 'L':
                x -= 1
                mark = '-'
            current_square = (y,x)
            if grid[y][x] != '.':
                if which_wire[current_square] != label:
                    mark = 'X'
                    exes.append(current_square)
            which_wire[current_square] = label
            steps[current_square].append((label, num_steps))
            grid[y][x] = mark

        grid[y][x] = '+'
        #print_grid(origin, grid)
        #import pdb
        #pdb.set_trace()
        #print(letter,num)
    #grid[y][x] = mark
#print_grid(origin, grid)
print(sorted([get_distance(origin, ex) for ex in exes]))

min_steps = 9999999999999
for ex in exes:
    distance = get_distance(origin, ex)
    total_steps = find_total_steps(steps[ex])
    if total_steps < min_steps:
        min_steps = total_steps
    print(ex, distance, steps[ex], total_steps)
print(min_steps)

   
    






