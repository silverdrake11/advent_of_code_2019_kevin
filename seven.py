import pdb
from itertools import permutations


def get_opcode(inst):
    inst = str(inst).rjust(5,'0')
    opcode = inst[-2:]
    ret_value = inst[2], inst[1], inst[0], opcode
    return [int(x) for x in ret_value]


class Computer:


    def __init__(self, code):

        self.prog = [x for x in code]
        self.i = 0
        self.running = True


    def get_param(self, num, mode):
        assert num
        assert num < 4
        value = self.prog[self.i + num]
        if mode:
            param = value
        else:
            param = self.prog[value]
        return param


    def run(self):
        while self.running:
            self.step()


    def run_until(self, given):
        given = list(reversed(given))
        while self.running:
            out = self.step(given)
            if out is not None:
                return out


    def step(self, given=None):

        ret_value = None
        inst = self.prog[self.i]

        mode1, mode2, mode3, opcode = get_opcode(inst)

        if opcode == 99:
            self.running = False
            return

        elif opcode in (1,2,7,8):
            increment = 4

            v1 = self.get_param(1, mode1)
            v2 = self.get_param(2, mode2)
            v3 = self.prog[self.i + 3]

            if opcode == 1:
                ans = v1 + v2
            if opcode == 2:
                ans = v1 * v2
            if opcode == 7:
                if v1 < v2:
                    ans = 1
                else:
                    ans = 0
            if opcode == 8:
                if v1 == v2:
                    ans = 1
                else:
                    ans = 0

            self.prog[v3] = ans

        elif opcode in (5,6):

            increment = 3

            value1 = self.get_param(1, mode1)
            value2 = self.get_param(2, mode2)

            if opcode == 5:
                if value1:
                    self.i = value2
                    increment = 0
            else:
                assert opcode == 6
                if not value1:
                    self.i = value2
                    increment = 0

        elif opcode == 3 or opcode == 4:
            increment = 2

            in1 = self.prog[self.i+1]
            if opcode == 3:
                if given:
                    input_value = int(given.pop())
                else:
                    input_value = int(input())
                self.prog[in1] = input_value
            else:
                if mode1 == 1:
                    out = in1
                else:
                    out = self.prog[in1]
                ret_value = out
                print(out)

        else:
            raise Exception(opcode)

        self.i += increment

        return ret_value


def part1_try(values):
    out_value = 0
    for in_value in values:
        comp = Computer(CODE)
        out_value = comp.run_until([in_value, out_value])
    return out_value


def part2_try(in_values):
    amps = [Computer(CODE) for x in range(NUM_AMPS)]
    out_value = 0
    for i in range(NUM_AMPS):
        out_value = amps[i].run_until([in_values[i], out_value])
    prev_value = 0
    while True:
        for i in range(NUM_AMPS):
            out_value = amps[i].run_until([out_value])
            if out_value == None:
                return prev_value
            prev_value = out_value


with open('input.txt') as fh:
    text = fh.read().strip()

CODE = text.split(',')
CODE = [int(x) for x in CODE]
NUM_AMPS = 5


chars = list('01234')
list_of_values = []
for comb in permutations(chars):
    value = part1_try(comb)
    list_of_values.append(value)
print('Part 1: ', max(list_of_values))


chars = list('56789')
list_of_values = []
for comb in permutations(chars):
    value = part2_try(comb)
    list_of_values.append(value)
print('Part 2:', max(list_of_values))






