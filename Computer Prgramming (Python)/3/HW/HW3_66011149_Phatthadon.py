#Lab_3_HW_1

a1 = (input("Enter employee's name: "))
a2 = float(input("Enter number of hours worked in a week: "))
a3 = float(input("Enter hourly pay rate: "))
a4 = float(input("Enter federal tax withholding rate: "))
a5 = float(input("Enter state tax withholding rate: "))




c1 = a2 * a3
c2 = c1 * a4
c3 = c1 * a5
c4 = c2 + c3
c5 = c1 - c4



print("Employee Name: ", a1)
print("Hours Worked: ", a2)
print("Pay Rate: $", a3)
print("Gross Pay: $", c1)
print("Deductions:")
print("\tFederal Withholding", "(", format(a4, "4.1%"), "\b)", ": $", round(c2, 2))
print("\tState Withholding", "(", format(a5, "4.1%"), "\b)" ": $", round(c3, 2))
print("\tTotal Deduction: $", round(c4, 2))
print("Net Pay: $", round(c5, 2))



#Lab_3_HW_2

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


#Lab_3_HW_3

import turtle as t

length = int(input("Enter desired length:"))

t.speed(5)
t.forward(length)
t.right(144)
t.forward(length)
t.right(144)
t.forward(length)
t.right(144)
t.forward(length)
t.right(144)
t.forward(length)
t.right(144)
t.done()


#Lab_3_HW_4

import turtle as t

radius = int(input("Enter desired radius:"))
xcord = t.xcor()
t.speed(8)
t.pensize(8)

t.color("blue")
t.circle(radius)

t.penup()
t.forward(xcord + radius * 2.3)
t.pendown()

t.color("black")
t.circle(radius)

t.penup()
t.forward(xcord + radius * 2.3)
t.pendown()

t.color("red")
t.circle(radius)

t.penup()
t.goto(0,0)
t.goto(radius * 1.15 , -radius * 1.3)
t.pendown()

t.color("yellow")
t.circle(radius)

t.penup()
t.forward(xcord + radius * 2.3)
t.pendown()

t.color("green")
t.circle(radius)

t.done()


#Lab_3_HW_5

import turtle as t

x1 = int(input("Enter point #1 x coordinate:"))
y1 = int(input("Enter point #1 y coordinate:"))
x2 = int(input("Enter point #2 x coordinate:"))
y2 = int(input("Enter point #2 y coordinate:"))
x3 = int(input("Enter point #3 x coordinate:"))
y3 = int(input("Enter point #3 y coordinate:"))

area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))

t.penup()
t.goto(x1, y1)
t.pendown()

t.goto(x2, y2)
t.goto(x3, y3)
t.goto(x1, y1)

t.penup()
t.goto(0, min(y1, y2, y3) - 30) 
t.write("The area is " + str(area))
t.done()
