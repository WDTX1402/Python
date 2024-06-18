def print_table(ls1):
	for i in ls1:
		for j in i:
			print(f"{j}\t", end = '')
		print("")

#print_table( [["X000000000000000000","Y"],[0,0],[10,10],[200,200]] ) 
print_table( [
 ["ID","Name","Surname"],
 ["001","Guido","van Rossum"],
 ["002","Donald","Knuth"],
 ["003","Gordon","Moore"] ] )