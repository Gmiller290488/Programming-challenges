import sys
# Given an int N
# And a square matrix of, N x N
# calculate the absolute difference between the sum of its diagonals

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sum_first_diagonal = sum(a[i][i] for i in range(n))
sum_second_diagonal = sum(a[i][n - i - 1] for i in range(n))
print(abs(sum_first_diagonal - sum_second_diagonal))
