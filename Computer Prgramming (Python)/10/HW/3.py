def my_union(list1, list2):
    return list(set(list1) | set(list2))

def my_intersection(list1, list2):
    return list(set(list1) & set(list2))

def my_difference(list1, list2):
    return list(set(list1) - set(list2))


list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

out1 = (my_union(list1, list2)) 
print(out1)
out2 = my_intersection(list1, list2)
print(out2)
out3 = my_difference(list1, list2)
print(out3) 
