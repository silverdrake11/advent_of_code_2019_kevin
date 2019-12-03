with open('input2.txt') as fh:
    text = fh.read().strip()

prog = text.split(',')

prog = [int(x) for x in prog]


combinations = []
for x in range(100):
    for y in range(100):
        combinations.append((x,y))



def program(prog):
    prog = [x for x in prog] # deep copy
    i = 0
    while True:
        cur = prog[i]

        if cur == 99:
            return prog[0]

        in1 = prog[i+1]
        in2 = prog[i+2]
        out = prog[i+3]

        value1 = prog[in1]
        value2 = prog[in2]
        if cur == 1:
            prog[out] = value1 + value2
        if cur == 2:
            prog[out] = value1 * value2
        i = i + 4


prog[1] = 12
prog[2] = 2
print(program(prog))
print(program(prog))



for x,y in combinations:
    prog[1] = x
    prog[2] = y
    ans = program(prog)
    if ans == 19690720:
        print(100 * x + y)
        break
    






