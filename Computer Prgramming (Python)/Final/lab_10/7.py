def merge(ls1,ls2):
	comb = ls1 + ls2
	L = []
	while len(comb) > 0:
		L.insert(0,max(comb))
		comb.remove(max(comb))

	return L

l1 = [1, 5, 16, 61, 111]
l2 = [2, 4, 5, 6]
print(merge(l1, l2)) 