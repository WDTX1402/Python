str = "book,dog,drink,rain,pen"
output = ''

for i in str:
	if i == ",":
		print(output)
		output = ""
	else:
		output += i 

print(output)
