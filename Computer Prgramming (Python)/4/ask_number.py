score = eval(input("Enter a real number: "))

if isinstance(score, float):
    print("Type 0 for floating point ") 
    print("Type 1 for scientific format")
    yee = int(input("Do you want to display the number in floating point of scientific format"))   
    if yee == 0 :
        print(score)
    elif yee == 1 :
        print(format(score, "10.2e"))

elif isinstance(score, int):
    print("Type 0 for binary format") 
    print("Type 1 for octal formant") 
    print("Type 2 for hexadecimal format") 
    print("Type 3 for decimal format")
    yaa = int(input("Do you want to display the number in in binary, octal, hexadecimal or decimal format"))
    if yaa == 0 :
        print(bin(score))
    elif yaa == 1 :
        print(oct(score))
    elif yaa == 2 :
        print(hex(score))
    elif yaa == 3 :
        print(format(score, ".5f"))
else :
    print("Your input is not a real number")

     