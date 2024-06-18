import turtle as t

t.speed(500)

def draw_square(x):
    for i in range(4):
        t.forward(x)
        t.right(90)
    
def govern(x):
    for e in range(1,5):
     for i in range(1,5):
        draw_square(i * x)
     t.left(90)


govern(40)

t.done()




