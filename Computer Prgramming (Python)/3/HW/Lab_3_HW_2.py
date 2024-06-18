num = int(input("Enter a four-digit number: "))
num1 = num % 10
num = num // 10
num2 = num % 10
num = num // 10
num3 = num % 10
num = num // 10
num4 = num
print("The Reversed number is:", num1, end='')
print(num2, end='')
print(num3, end='')
print(num4)