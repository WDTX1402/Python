inpus = (input("Please enter a character:"))
x1 = len(inpus)

#a = (format(i, "04x"))
uppercase = inpus.upper()
lowercase = inpus.lower()

if x1 == 1:
    i = ord(inpus)
    if 48 <= i <= 57:
      print(inpus, "is a numeric character.")
    elif 97 <= i <= 123:
        print(inpus, "is a small-case letter and its capital is", uppercase)
    elif 65 <= i <= 88:
        print(inpus, "is a capital letter and its capital is", lowercase)
    else:
        print("Input is a special character")
else:
    print("input outside of the scope of this program")





