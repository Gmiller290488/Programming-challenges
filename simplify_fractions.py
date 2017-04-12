import math


# This function takes two ints, a is the numerator, b is the denominator
# The challenge is to find the most simplified form of the fraction

def simplify_fraction(a, b):
    a_list = []
    b_list = []
    biggest_num = 0
    for num in range(1, a):
        if a % num == 0:
            a_list.append(num)
            a_list.append(a // num)
    for num in range(1, b):
        if b % num == 0:
            b_list.append(num)
            b_list.append(b // num)
    for num in a_list:
        if num in b_list:
            if num > biggest_num:
                biggest_num = num
    print(a / biggest_num), (b / biggest_num)


simplify_fraction(4, 8)
simplify_fraction(1536, 78360)
simplify_fraction(51478, 5536)
simplify_fraction(46410, 119340)
simplify_fraction(7673, 4729)
simplify_fraction(4096, 1024)
