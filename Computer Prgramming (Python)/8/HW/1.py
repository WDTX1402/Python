while True:
    inpus = input("Enter an integer: ")
    try:
        x = int(inpus)

    except ValueError:
        print("Invalid input")

    if x < 0:
        print("Only positive integers are allowed")
        break
    if x == 0:
        print("It is 0")
        break


    b =[]
    while(x>0):
        d = x%2
        b.append(d)
        x = x//2
    b.reverse()

    print("The binary equivalent of the number is ", end="")
    for i in b:
        print( i,end="")

    b.reverse()
    j = len(b)
    i = 0
    y = 0
    while i < j :
        y += 2**i * b[i]
        i += 1
    print("\n")
    print("Converted back to integer,",y,"\n")
