import turtle as t

def triangle(s):
    for i in range(3):
        t.fd(s)
        t.left(120)

def smol(s,r):
    for i in range(r):
        triangle(s)
        if i < s-1:
            t.penup()
            t.forward(s/2)
            t.left(60)
            t.pendown()

        s = s/2

smol(160,3)
t.done()