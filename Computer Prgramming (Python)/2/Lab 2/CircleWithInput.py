center_x = int(input("Input center x ="))
center_y = int(input("Input center y ="))
radius = int(input("Input radius =")) 

area = 3.14159 * radius * radius

import turtle
turtle.showturtle
turtle.penup()
turtle.goto(center_x, center_y)
turtle.right(90)
turtle.forward(radius)
turtle.left(90)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(center_x, center_y)
turtle.pendown()
turtle.write(area)
turtle.done()

 