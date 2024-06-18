import turtle as t

def draw_polygon(p1 ,p2 , p3= 4, p4 =100):
    t.penup()
    t.goto(p1, p2)
    t.pendown()
    for i in range (p3):
       t.forward(p4)
       t.left(360/p3)



draw_polygon(0, 0)
t.done()
