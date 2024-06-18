list = {}

while True:
    
    inpus = input("Enter your command: ")

    if inpus == "+":
        new_contact = input("Enter name: ")
        num = int(input("Enter a number: "))
        list[new_contact] = num

    elif inpus == "-":
        contact = input("Enter name: ")
        try:
            list.pop(contact)
        except:
            print("No contact found")
    
    elif inpus == "f":
        contact = input("Enter name: ")
        try:
            print(list[contact])
        except:
            print("No contact found")

    elif inpus == "p":
        print(list)
    
    elif inpus == "q":
        break 
    