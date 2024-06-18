def name_list():
	list = []
	i = 1
	while True:
		x = input(f"Enter name {i}: ")
		if x == '':
			break
		else:
			list.append(x)
			i += 1
	
	return list

print(name_list())