import pdb
from pprint import pprint

with open('input.txt') as fh:
    text = fh.read().strip()

prog = text.split(',')

prog = [int(x) for x in prog]


combinations = []
for x in range(100):
    for y in range(100):
        combinations.append((x,y))


def get_params(inst):
    inst = str(inst)
    opcode = inst[-2:]

    if len(inst) == 5:
        ret_value = inst[2], inst[1], inst[0], opcode

    elif len(inst) == 4:
        ret_value = inst[1], inst[0], 0, opcode

    elif len(inst) == 3:
        ret_value = inst[0], 0, 0, opcode

    elif len(inst) == 2 or len(inst) == 1:
        ret_value = 0, 0, 0, opcode

    return [int(x) for x in ret_value]


def program(prog):
    prog = [x for x in prog] # deep copy
    i = 0
    while True:
        cur = prog[i]

        first, second, third, opcode = get_params(cur)

        if opcode == 99:
            return prog[0]

        elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            increment = 4

            in1 = prog[i+1]
            in2 = prog[i+2]
            if first:
                value1 = in1
            else:
                value1 = prog[in1]
            if second:
                value2 = in2
            else:
                value2 = prog[in2]

            out = prog[i+3]

            if opcode == 1:
                prog[out] = value1 + value2
            if opcode == 2:
                prog[out] = value1 * value2
            if opcode == 7:
                if value1 < value2:
                    prog[out] = 1
                else:
                    prog[out] = 0
            if opcode == 8:
                if value1 == value2:
                    prog[out] = 1
                else:
                    prog[out] = 0

        elif opcode == 3 or opcode == 4:
            increment = 2

            in1 = prog[i+1]

            if opcode == 3:
                input_value = int(input())
                prog[in1] = input_value
            else:
                print(prog[in1])

        elif opcode == 5 or opcode == 6:
            increment = 3

            in1 = prog[i+1]
            in2 = prog[i+2]
            if first:
                value1 = in1
            else:
                value1 = prog[in1]
            if second:
                value2 = in2
            else:
                value2 = prog[in2]

            if opcode == 5:
                if value1:
                    i = value2
                    increment = 0
            else:
                assert opcode == 6
                if not value1:
                    i = value2
                    increment = 0

        else:
            raise Exception(opcode)

        i = i + increment


#prog[1] = 12
#prog[2] = 2
program(prog)
#print(program(prog))


'''
for x,y in combinations:
    prog[1] = x
    prog[2] = y
    ans = program(prog)
    if ans == 19690720:
        print(100 * x + y)
        break'''
    






