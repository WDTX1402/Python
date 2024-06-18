import turtle as t

list = [1,2,2,1,3,4,5,6,3,4,5,6,4,3,5,4,5,3,4,4,3,3,4,3,3,4,4,4]

def histogram(list):
    char_count = {}
    value = []
    chars = []

    for i in list:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    lencnt = len(char_count)

    for char, count in char_count.items():
        chars.append(char)
        value.append(count)

    t.speed(10)
    maxi = max(value)
    t.penup()
    t.goto(-20*lencnt,0)
    t.pendown()    
    t.left(90)
    t.fd(20 * maxi)
    t.left(90)
    t.fillcolor("black")
    t.begin_fill()
    t.fd(5)
    t.right(120)
    t.fd(10)
    t.right(120)
    t.fd(10)
    t.right(120)
    t.fd(10)
    t.end_fill()
    t.penup()
    t.goto(-20 * lencnt,0)
    t.pendown()

    t.right(180)
    t.fd((30 * lencnt)+ 30)
    t.left(90)
    t.fillcolor("black")
    t.begin_fill()
    t.fd(5)
    t.right(120)
    t.fd(10)
    t.right(120)
    t.fd(10)
    t.right(120)
    t.fd(10)
    t.end_fill()
    t.penup()
    t.goto(-20 * lencnt,0)
    t.pendown()
    t.right(90)
    t.fd(30)

    for i in range(lencnt):
        t.penup()
        pos1 = t.xcor()
        pos2 = t.ycor()
        t.goto(pos1 +5,pos2 -20)
        t.pendown()
        t.write(chars[i])
        t.penup()
        t.goto(pos1,pos2)
        t.pendown()
        t.left(90)
        t.fd(value[i] *20)
        t.right(90)
        t.fd(30)
        t.right(90)
        t.fd(value[i] *20)
        t.left(90)

    t.hideturtle()


    t.done()

histogram(list)