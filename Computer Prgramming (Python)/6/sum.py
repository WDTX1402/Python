def sum_of_digits(i):
    stringy = str(i)
    sum = 0
    for x in stringy:
        sum += int(x)
    return sum


print("The sum of the digits are", sum_of_digits(987))
