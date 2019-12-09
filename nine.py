import pdb


class Computer:


    def __init__(self, code):

        self.prog = {}
        for i, x in enumerate(code):
            self.prog[i] = x
        self.i = 0
        self.running = True
        self.base = 0


    def get_param(self, num, mode):
        assert num
        assert num < 4
        value = self.prog[self.i + num] # CHANGE?
        if mode == 1:
            param = value
        elif mode == 2:
            param = self.read_prog(self.base + value)
        else:
            param = self.read_prog(value)
        return param


    def read_prog(self, idx):
        if idx in self.prog:
            return self.prog[idx]
        else:
            return 0


    def run(self):
        while self.running:
            self.step()


    def step(self):

        inst = self.prog[self.i] # CHANGE?

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

            # HERE
            if mode3 == 2:
                self.prog[self.base + v3] = ans
            else:
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
                input_value = int(input())
                if mode1 == 2:
                    self.prog[self.base + in1] = input_value
                else:
                    self.prog[in1] = input_value #HERE
            else:
                if mode1 == 2:
                    print(self.read_prog(self.base + in1))
                elif mode1 == 1:
                    print(in1)
                else:
                    print(self.read_prog(in1)) #HERE

        elif opcode == 9:
            increment = 2
            value1 = self.get_param(1, mode1)
            self.base += value1

        else:
            raise Exception(opcode)

        self.i += increment


with open('input.txt') as fh:
    text = fh.read().strip()

code = text.split(',')
code = [int(x) for x in code]

comp = Computer(code)
comp.run()