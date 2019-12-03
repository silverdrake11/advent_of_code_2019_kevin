with open('input.txt') as fh:
    lines = fh.read().splitlines()

def get_fuel(line):
    fuel = int(math.floor(int(line) / 3) - 2)
    if fuel < 0:
        return 0
    else:
        return fuel + get_fuel(fuel)

import math
total = 0
for line in lines:
    #line = 1969
    #print(get_fuel(line))
    total += get_fuel(line)
print(total)

