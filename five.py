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


def get_opcode(inst):
    inst = str(inst).rjust(5,'0')
    opcode = inst[-2:]
    ret_value = inst[2], inst[1], inst[0], opcode
    return [int(x) for x in ret_value]


class Computer:

    def __init__(self, prog):
        self.prog = [x for x in prog] # deep copy
        self.i = 0

    def run(self):
        while True:
            cur = self.prog[self.i]

            first, second, third, opcode = get_opcode(cur)

            if opcode == 99:
                return self.prog[0]

            elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
                increment = 4

                in1 = self.prog[i+1]
                in2 = self.prog[i+2]
                if first:
                    value1 = in1
                else:
                    value1 = self.prog[in1]
                if second:
                    value2 = in2
                else:
                    value2 = self.prog[in2]

                out = self.prog[self.i+3]

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
    






