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