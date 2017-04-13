# Given an array of integers, calculate which fraction of its elements are positive,
#  which fraction of its elements are negative, and which fraction of its elements are zeroes,
# respectively.
# Print the decimal value of each fraction on a new line.

positive = negative = zero = 0
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for num in arr:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    elif num == 0:
        zero += 1
print(positive/n)
print(negative/n)
print(zero/n)