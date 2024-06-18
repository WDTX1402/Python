def my_sort(ls1):
	L = []
	while len(ls1) > 0:
		L.insert(0,max(ls1))
		ls1.remove(max(ls1))

	return L

print(my_sort([6, 4, 2, 1, 4]))