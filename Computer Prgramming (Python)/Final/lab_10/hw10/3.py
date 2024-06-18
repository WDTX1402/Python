def my_union(ls1, ls2):
	union_list = ls1.copy()
	for elem in ls2:
		if elem not in union_list:
			union_list.append(elem)
	return union_list

list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]
print(my_union(list1, list2))

def my_intersection(ls1, ls2):
	intersect = []
	long = max(ls1, ls2)
	short = min(ls1, ls2)
	for i in long:
		if i in short:
			intersect.append(i)
	return intersect

print(my_intersection(list1, list2))

def my_difference(ls1, ls2):
	diff = []
	long = max(ls1, ls2)
	short = min(ls1, ls2)
	for i in long:
		if i not in short:
			diff.append(i)
	return diff

print(my_difference(list1, list2))