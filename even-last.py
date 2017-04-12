
#Given a list of numbers, sum all numbers at even indexes, and then times by last number of the array
def even_last(array):
    total = 0
    if len(array) < 1:
        return 0
    for num in array[::2]:
        total += num
    return total * array[-1]
