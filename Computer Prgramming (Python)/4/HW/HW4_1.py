import turtle as t

x0 = int(input("Enter Point #0 x coordinate:"))
y0 = int(input("Enter Point #0 y coordinate:"))
x1 = int(input("Enter Point #1 x coordinate:"))
y1 = int(input("Enter Point #1 y coordinate:"))
x2 = int(input("Enter Point #2 x coordinate:"))
y2 = int(input("Enter Point #2 y coordinate:"))

determine = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
write_ans = (x2 + 50, y2 - 50)

t.penup()
t.goto(x0, y0)
t.pendown()
t.write("p0")
t.goto(x1, y1)
t.write("p1")
t.penup()
t.goto(x2, y2)
t.pendown()
t.dot(5)
t.write("p2")
t.penup()
t.goto(write_ans)
t.pendown
if determine > 0 :
    t.write("p2 is on the left side of the line")
elif determine < 0:
    t.write("p2 is on the right side of the line")
elif determine == 0: 
    t.write("p2 is on the line")

t.hideturtle()
t.done()