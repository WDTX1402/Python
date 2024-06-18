sum = 0
number = 0

while number < 9:
    number += 1
    sum += number
    if sum >= 100:
        break
print("The number is ", number)
print("The sum is ", sum)