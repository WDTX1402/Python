def remove_thirds(lst):
	new_list = []
	for i in range(len(lst)):
		if (i + 1) % 3 != 0:
			new_list.append(lst[i])
	
	return new_list

list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
print(remove_thirds(list1))
