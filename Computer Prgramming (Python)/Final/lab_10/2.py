def mycount(list):
	count = 0
	for i in list:
		if i >= 0:
			count += 1
		else:
			count
	return count

t = mycount([-3,2,0,1,-5])
print(t)