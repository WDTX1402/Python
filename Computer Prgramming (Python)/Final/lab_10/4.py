def get_difference(ls1,ls2):
	new = []
	for i in ls1:
		chk = 0
		for j in ls2:
			if i == j:
				chk = 1
		if chk == 0:
			new.append(i)
	
	for i in ls2:
		chk = 0
		for j in ls1:
			if i == j:
				chk = 1
		if chk == 0:
			new.append(i)

	return new

x = get_difference([3,1,1,1,2,7],[4,1,1,2,2,5])
print(x)