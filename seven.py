import pdb


with open('input.txt') as fh:
    text = fh.read().strip()

prog = text.split(',')
prog = [int(x) for x in prog]


def get_params(inst):
    inst = str(inst).rjust(5,'0')
    opcode = inst[-2:]
    ret_value = inst[2], inst[1], inst[0], opcode
    return [int(x) for x in ret_value]


def program(prog, start=0, given=[]):
    #prog = [x for x in prog] # deep copy
    i = start
    #print('pointer', i)
    given = list(reversed(given))
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
                if given:
                    input_value = int(given.pop())
                    #pdb.set_trace()
                    #print(input_value)
                else:
                    input_value = int(input())
                prog[in1] = input_value
            else:
                #return prog[in1]
                return(i + increment, prog[in1])

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


'''def try_values(prog, values):
    out_value = 0
    for in_value in values:
        prog = [x for x in prog]
        out_value = program(prog, 0, [in_value, out_value])
    return out_value


import itertools
myStr = "01234"
chars = list(myStr)
list_of_values = []
for comb in itertools.permutations(chars):
    value = try_values(prog, comb)
    if value == 38834:
        print(comb)
    list_of_values.append(value)
print('Part 1: ', max(list_of_values))'''


def new_function_program(prog, seq):
    prog1 = [x for x in prog]
    prog2 = [x for x in prog]
    prog3 = [x for x in prog]
    prog4 = [x for x in prog]
    prog5 = [x for x in prog]

    save1, result1 = program(prog1,0,[seq[0],0])
    #print(result1)
    save2, result2 = program(prog2,0,[seq[1],result1])
    #print(result2)
    save3, result3 = program(prog3,0,[seq[2],result2])
    #print(result3)
    save4, result4 = program(prog4,0,[seq[3],result3])
    #print(result4)
    save5, result5 = program(prog5,0,[seq[4],result4])
    #print(result5)

    state = {1:[prog1, save1, result1], 
    2:[prog2, save2, result2], 
    3:[prog3, save3, result3], 
    4:[prog4, save4, result4], 
    5:[prog5, save5, result5]}

    #print(state)
    #pdb.set_trace()

    i = 1
    answers = []
    while True:
        if i == 6:
            i = 1
        if i == 1:
            prev_index = 5
        else:
            prev_index = i-1
        prog_prev, save_prev, result_prev = state[prev_index]
        prog, save, result = state[i]
        try:
            one, two = program(prog, save, [result_prev])
        except:
            return answers[-1]
        #print(i, two)
        #pdb.set_trace()
        state[i] = [prog, one, two]
        #print(i)
        answers.append(two)
        i += 1

    '''
    for x,y in combinations:
        prog[1] = x
        prog[2] = y
        ans = program(prog)
        if ans == 19690720:
            print(100 * x + y)
            break'''


import itertools
myStr = "56789"
chars = list(myStr)
list_of_values = []
for comb in itertools.permutations(chars):
    value = new_function_program(prog, comb)
    #if value == 38834:
    #    print(comb)
    list_of_values.append(value)
print('Part 2:', max(list_of_values))

#print(new_function_program(prog, (9,7,8,5,6)))
    






