n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
total = 0
for num in arr:
    total += num

print(total)

# Others solution using map:

print(sum(map(int, input().split())))