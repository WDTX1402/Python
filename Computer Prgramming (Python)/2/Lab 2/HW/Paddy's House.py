import turtle
turtle.showturtle

#right side
turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()
turtle.forward(405)
turtle.left(90)
turtle.forward(250)

#right side roof***
turtle.left(60)
turtle.forward(230)
turtle.left(60)
turtle.forward(230)
turtle.left(60)
turtle.forward(250)
turtle.left(90)


#left side
turtle.left(90)
turtle.forward(300)
turtle.left(45)
turtle.forward(200)
turtle.left(45)
turtle.left(45)
turtle.forward(200)
turtle.right(-45)
turtle.forward(300)
turtle.left(90)
turtle.forward(680)
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(397)

turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(284)

#door
turtle.penup()
turtle.goto(-270, -200)
turtle.pendown()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(100)

#right side roof fix***
turtle.penup()
turtle.goto(-157, 165)
turtle.pendown()
turtle.goto(105, 165)

turtle.done()