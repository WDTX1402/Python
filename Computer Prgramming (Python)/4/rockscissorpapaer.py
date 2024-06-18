import random as r
print("0 = scissor")
print("1 = rock")
print("2 = paper")

number1 = r.randint(0, 3)
number2 = int(input("Enter a number: "))

if number1 == 0 :
    x1 = ("scissor")
elif number1 == 1:
    x1 = ("rock")
elif number1 == 2:
    x1 = ("paper")

if number2 == 0 :
    x2 = ("scissor")
elif number2 == 1:
    x2 = ("rock")
elif number2 == 2:
    x2 = ("paper")
else :
    x2 = ("wrong")

if number1 == number2 and number2 <=2 and number2 >= 0 :
    print("The computer is", x1, ".", "You are", x2, ".", "It's a draw.")
elif number2 >= number1 and number2 <=2 and number2 >= 0:
    print("The computer is", x1, ".", "You are", x2, ".", "You won.")
elif number1 >= number2 and number2 <=2 and number2 >= 0 :
    print("The computer is", x1, ".", "You are", x2, ".", "The computer won.")
else :
    print("wrong input")
