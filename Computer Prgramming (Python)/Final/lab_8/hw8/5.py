i = (input("Enter ISBN: "))

x = (int(i[0])*1 + int(i[1])*2 + int(i[2])*3 + int(i[3])*4 + int(i[4])*5 + int(i[5])*6 + int(i[6])*7 + int(i[7])*8 + int(i[8])*9)% 11

if x == 10:
	print(str(i) + "X")
else:
	print(str(i) + str(x))
