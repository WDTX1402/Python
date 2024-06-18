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