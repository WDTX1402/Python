inpus = input("Enter some text: ")
result = {}

for i in inpus:
	if i in result:
		result[i] += 1 
	else:
		result[i] = 1
	
for k, v in result.items():
	print(f"{k} : {((v/len(inpus))*100):.2f}%")