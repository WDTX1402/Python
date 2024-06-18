import turtle as t


x = input("Enter some text: ")

len1 = len(x)

char_count = {}
value = []
chars = []

for i in x:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

lencnt = len(char_count)

for char, count in char_count.items():
    chars.append(char)
    value.append(count)
    
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


for i in range(lencnt):
    t.fd(20)
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
    t.fd(10)
    t.right(90)
    t.fd(value[i] *20)
    t.left(90)

t.hideturtle()


t.done()