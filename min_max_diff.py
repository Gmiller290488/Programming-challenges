# given an undeterminded amount of numbers
# find the difference between the smallest and largest numbers
import operator
def diff(*args):
    if args:
        maxNum = max(args)
        minNum = min(args)
        return (maxNum - minNum)
    else:
        return 0





diff((1, 2, 3), 2, 3)