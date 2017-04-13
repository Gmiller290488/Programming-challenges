# My solution

a_total = 0
b_total = 0
a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
# Write Your Code Here

if a0 > b0:
    a_total += 1
elif b0 > a0:
    b_total += 1
if a1 > b1:
    a_total += 1
elif b1 > a1:
    b_total += 1
if a2 > b2:
    a_total += 1
elif b2 > a2:
    b_total += 1

print(a_total, b_total)

# better solution

a0,a1,a2 = raw_input().strip().split(' ')
A = a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
B = b0,b1,b2 = [int(b0),int(b1),int(b2)]
alice = bob = 0
for x,y in zip(A,B):
    if x>y: alice += 1
    if x<y: bob += 1
print(alice,bob)