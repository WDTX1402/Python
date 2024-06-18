
while True :
     inpus = (input("Please enter a character:"))
     x1 = len(inpus)
     if x1 != 1:
         continue
     x = ord(inpus)
     uppercase = inpus.upper()
     lowercase = inpus.lower()
        
     if x != 9:
      
        i = ord(inpus)
        if 48 <= i <= 57:
            print(inpus, "is a numeric character.")
        elif 97 <= i <= 123:
            print(inpus, "is a small-case letter and its capital is", uppercase)
        elif 65 <= i <= 88:
            print(inpus, "is a capital letter and its small-case letter is", lowercase)
        else:
            print("Input is a special character")
    
     elif x == 9:
         break
     else:
        print("input outside of the scope of this program")
    
   

print("Good bye, see you tomorrow")






