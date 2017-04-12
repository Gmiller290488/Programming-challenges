# You are given an array with positive numbers and a number N. You should find the N-th power
# of the element in the array with the index N. If N is outside of the array, then return -1.
# Don't forget that the first element has the index 0.

def index_power(array, n):
    if n > (len(array)-1):
        return print(-1)
    else:
        return print(array[n]**n)

index_power([1, 3, 10, 100], 3)