long = str(input("Enter long string: "))
shrt = str(input("Enter short string: "))


check = 0
for i in range(len(long)+1):
    if check == 1:
        break
    for j in range(i):
        if long[j:i] == shrt:
            check = 1

    
if check == 0:
    print("No match")
if check == 1:
    print("Match")
