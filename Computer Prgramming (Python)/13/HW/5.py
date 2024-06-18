import turtle as t

t.left(90)
t.tracer(0)

def tree(input):
    if input < 10:
        return
    else:
        t.fd(input)
        t.left(30)
        tree((3*input)/4)
        t.right(60)
        tree((3*input)/4)
        t.left(30)
        t.back(input)

tree(75)
t.done()