import sys


def sumOfArray(a, b):
    total = 0
    for num in b:
        total += num
    print(total)
    return total


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
sumOfArray(n, arr)