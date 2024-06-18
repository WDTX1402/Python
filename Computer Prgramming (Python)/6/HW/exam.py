# x = int(input("Enter:"))

# x1000 = x//1000
# x500 = (x%1000) //500
# x100 = (x%500) //100


# print("You get:")
# if x1000 >= 1:
#  print("\t",x1000, if x1000 == 1: {"note"} else {"notes"}, "if 1000 Baht")
# else:
#     ()

# if x500 >=1:
#     print("\t", x500, "notes of 500 baht")
# else:
#     ()

# if x100 >= 1:
#     print("\t", x100, "notes of 100 baht")
# else:
#     ()
# while True:
#  i = int(input("enter:"))
#  if i == 3:
#     break
    
#  for i in range(49,0,-1):
#     if i % 3 == 0:
#         continue
#     elif i % 3 != 0:
#         if i == 1:
#             print("1." ,end = '')
#         else:
#             print(i,end = ',')

import turtle as t
# n = int(input("square size: "))
n = 150

t.speed(5)

def draw_sq(n):
    for i in range(5):
        t.forward(n)
        t.right(90)

def spiral_sq(n):
        j = 0
        for i in range(n): 
            if n >= 5:
               
                
                draw_sq(n)
            
                n = n* 0.75
                
                t.left(90)
                t.back(n)
                
                t.pos()
                pos1 = t.xcor()
                pos2 = t.ycor()
                t.penup()
                t.goto()
                t.pendown()
          
                t.left(10)

                j += 1
                
            else:
                 break

     

spiral_sq(150)
t.done()


import turtle as t
t.speed(5)
def square(size):
    t.penup()
    t.back(size/2)
    t.left(90)
    t.fd(size/2)
    t.right(90)
    t.pendown()
    for _ in range(4):
        t.fd(size)
        t.right(90)
    t.penup()
    t.fd(size/2)
    t.right(90)
    t.fd(size/2)
    t.left(90)

def spiral_sq(size):
    while size >= 5:
        square(size)
        t.left(10)
        size *= 0.75

spiral_sq(150)
t.done()