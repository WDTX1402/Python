# import random as r

# number1 = r.randint(0, 9)
# number2 = r.randint(0, 9)

# answer = int(input("What is " + str(number1) + "+" + str(number2) + "? "))

# print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)

number = input("Enter number: ")
format = str(number[::-1])
print(format)