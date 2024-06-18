import turtle as t 

def draw_sq (n):
    t.penup()
    t.left(90)
    t.fd(n/2)
    t.right(90)
    t.back(n/2)
    t.pendown()
    for i in range(4):
        t.fd(n)
        t.right(90)
    t.penup()
    t.fd(n/2)
    t.right(90)
    t.fd(n/2)
    t.left(90)
    t.pendown()

def shrink(s,g):
    while s > 20:
        draw_sq(s)
        s = s-(g*2)


def draw(s):
    for i in range(4):
        t.fd(s)
        t.right(90)
def shrink(s,g):
    while s > 20:
        draw(s)
        t.penup()
        t.fd(g)
        t.right(90)
        t.fd(g)
        t.left(90)
        t.pendown()
        s = s-(g*2)
shrink(200,20)