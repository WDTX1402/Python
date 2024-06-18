#Q1
while True:
    inpus = input("Enter an integer: ")
    try:
        x = int(inpus)

    except ValueError:
        print("Invalid input")

    if x < 0:
        print("Only positive integers are allowed")
        break
    if x == 0:
        print("It is 0")
        break


    b =[]
    while(x>0):
        d = x%2
        b.append(d)
        x = x//2
    b.reverse()

    print("The binary equivalent of the number is ")
    for i in b:
        print(i,end="")

    b.reverse()
    j = len(b)
    i = 0
    y = 0
    while i < j :
        y += 2**i * b[i]
        i += 1
    print("\n")
    print("Converted back to integer,",y,"\n")



#Q2
x = input("Enter some text: ")

len = len(x)

char_count = {}

for i in x:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

print("-- Character Frequency Table --")

for char, count in char_count.items():
    percent= (count / len) * 100
    print(f"{char} = {percent:.2f}%")


#Q3
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


#Q4
x = (input("Enter the first 9 digits of an ISBN-10 as a string:"))

if len(x) >= 10 or len(x) < 9:
    print("Invalid input")

checksum = (int(x[0]) * 1 + int(x[1]) * 2 + int(x[2]) * 3 + int(x[3]) * 4 + int(x[4]) * 5 + int(x[5]) * 6 + int(x[6]) * 7 + int(x[7]) * 8 + int(x[8]) * 9) % 11


if checksum == 10:
    print(f"Your ISBN-10 number is {x}X")
else:
    print(f"Your ISBN-10 number is {x}{checksum}")
