import pdb


def is_increasing(str_num):
    prev = 0
    for num in str_num:
        num = int(num)
        if num < prev:
            return False
        prev = num
    return True


def adj_digits(str_num):
    prev = 'a' # sentinel
    for char in str_num:
        if char == prev:
            return True
        prev = char
    return False


def two_only(str_num):
    str_num = 'a' + str_num + 'a'
    prev = 'b'
    in_a_row = 1
    spotted = False
    for char in str_num:
        if char == prev:
            in_a_row += 1
        else:
            if in_a_row == 2:
                return True
            in_a_row = 1
        prev = char
    return False


pswds = 0
for num in range(372037, 905157+1):
    str_num = str(num)
    if is_increasing(str_num):
        #if adj_digits(str_num): # Part 1
        if two_only(str_num): # Part 2
            pswds += 1


print(pswds)





