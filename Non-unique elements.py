#You are given a non-empty list of integers (X). For this task,
#you should return a list consisting of only the non-unique elements in this list.
#To do so you will need to remove all unique elements
#(elements which are contained in a given list only once).
#When solving this task, do not change the order of the list.
#Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].


#my Solution
def remove_unique(list):
    repeat_list = []
    final_list = []
    count = 1
    for num in list:
        if num not in repeat_list:
            for temp in list[count:]:
                if num == temp:
                    repeat_list.append(num)
                    break
            count += 1
        else:
            count += 1
    for item in list:
        for num in repeat_list:
            if item == num:
                final_list.append(num)
    print(final_list)


remove_unique([10, 9, 10, 10, 9, 8])

# Other better solution
def remove_unique(list):
    return [x for x in list if list.count(x)>1]