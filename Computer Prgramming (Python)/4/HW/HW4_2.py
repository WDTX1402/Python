import turtle as t

x1 = int(input("Enter Rectangle #1 x coordinate:"))
y1 = int(input("Enter Rectangle #1 y coordinate:"))
w1 = int(input("Enter Rectangle #1 Width:"))
h1 = int(input("Enter Rectangle #1 Height:"))

x2 = int(input("Enter Rectangle #2 x coordinate:"))
y2 = int(input("Enter Rectangle #2 y coordinate:"))
w2 = int(input("Enter Rectangle #2 Width:"))
h2 = int(input("Enter Rectangle #2 Height:"))

if x1 - x2 >= 0:
    x_distance = x1 - x2
else:
    x_distance = x2 - x1

if y1 - y2 >= 0:
    y_distance = y1 - y2
else:
    y_distance = y2 - y1 

if x_distance <= (w1 - w2)/2 and y_distance <= (h1 - h2)/2:
    print("Rectangle #2 is inside Rectangle #1")
elif x_distance <= (w1 + w2)/2 and y_distance <= (h1 + h2)/2:
    print("Rectangle #2 overlaps Rectangle #1")
else:
    print("Rectangle #2 does not overlap Rectangle #1")

t.penup()
t.goto(x1, y1)
t.write("Rec #1" + "("+ str(x1) + "," + str(y1) +")")
t.goto(x1 - (w1 / 2) ,y1 + (h1 / 2))
t.pendown()
t.goto(x1 + (w1 / 2) ,y1 + (h1 / 2))
t.goto(x1 + (w1 / 2) ,y1 - (h1 / 2))
t.goto(x1 - (w1 / 2) ,y1 - (h1 / 2))
t.goto(x1 - (w1 / 2) ,y1 + (h1 / 2))

t.penup()

t.goto(x2, y2)
t.write("Rec #2" + "("+ str(x2) + "," + str(y2) +")")
t.goto(x2 - (w2 / 2) ,y2 + (h2 / 2))
t.pendown()
t.goto(x2 + (w2 / 2) ,y2 + (h2 / 2))
t.goto(x2 + (w2 / 2) ,y2 - (h2 / 2))
t.goto(x2 - (w2 / 2) ,y2 - (h2 / 2))
t.goto(x2 - (w2 / 2) ,y2 + (h2 / 2))
t.penup()
t.goto(x2 + w2, y2 + h2)
if x_distance <= (w1 - w2)/2 and y_distance <= (h1 - h2)/2:
    t.write("Rectangle #2 is inside Rectangle #1")
elif x_distance <= (w1 + w2)/2 and y_distance <= (h1 + h2)/2:
    t.write("Rectangle #2 overlaps Rectangle #1")
else:
    t.write("Rectangle #2 does not overlap Rectangle #1")
    
t.hideturtle()
t.done() 