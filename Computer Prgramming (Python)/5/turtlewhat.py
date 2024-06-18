import turtle as t
N = int(input("Enter an integer: "))
x = 100 / N
t.speed(10)
w = N

def draw_square(x):
    for i in range(4):
        t.forward(x)
        t.right(90)

for i in range(N):
     for j in range(w):
         if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
             t.begin_fill()
             draw_square(x)
             t.end_fill()
             t.forward(x)
         else:
            draw_square(x)
            t.forward(x)
     t.penup()
     t.goto(0, -x * (i + 1))
     t.pendown()


t.done()
