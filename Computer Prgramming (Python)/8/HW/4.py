x = (input("Enter the first 9 digits of an ISBN-10 as a string:"))

if len(x) >= 10 or len(x) < 9:
    print("Invalid input")

checksum = (int(x[0]) * 1 + int(x[1]) * 2 + int(x[2]) * 3 + int(x[3]) * 4 + int(x[4]) * 5 + int(x[5]) * 6 + int(x[6]) * 7 + int(x[7]) * 8 + int(x[8]) * 9) % 11


if checksum == 10:
    print(f"Your ISBN-10 number is {x}X")
else:
    print(f"Your ISBN-10 number is {x}{checksum}")
