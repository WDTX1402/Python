# import turtle as t

# def draw_square(n):
#     for i in range(4):
#         t.fd(n)
#         t.right(90)

# def draw_nested_squares(s,g):
#     while s >= 20:
#         draw_square(s)
#         t.penup()
#         t.right(90)
#         t.fd(g)
#         t.left(90)
#         t.fd(g)
#         t.pendown()
#         s = s-40

# draw_nested_squares(200,20)
# t.done()

# print(2 * (4 - 2) ** (2 + 3) * 5 - 3)

# import turtle as t 
# print("Hello, welcome to Turtle world!")
# while True:
    
#     x = input("turtle|>")

#     if x == "quit":
#         break
#     if x == "fd":
#         y = int(input("Please input its argument: "))
#         t.forward(y)
#     elif x == "back":
#         y = int(input("Please input its argument: "))
#         t.back(y)
#     elif x == "lt":
#         y = int(input("Please input its argument: "))
#         t.left(y)
#     elif x == "rd":
#         y = int(input("Please input its argument: "))
#         t.right(y)
#     elif x == "pu":
#         t.penup()
#     elif x == "pd":
#         t.pendown()
#     elif x == "reset":
#         t.reset()
#     else:
#         print("Wrong command, please try again.")

# t.done()

# import turtle as t
# print("Welcome")

# while True:
  
#     input1 = input("turtle |> ")
#     if input1 == "fd":
#         h = int(input("Input: "))
#         t.forward(h)
#     elif input1 == "back":
#         h = int(input("Input: "))
#         t.backward(h)
#     elif input1 == "lt":
#         angle = int(input("Input: "))
#         t.left(angle)
#     elif input1 == "rt":
#         angle = int(input("Input: "))
#         t.right(angle)
#     elif input1 == "pu":
#         t.penup()
#     elif input1 == "pd":
#         t.pendown()
#     elif input1 == "reset":
#         t.reset()
#     elif input1 == "quit":
#         break
#     else:
#         print("Invalid")
# t.done()
    
# print("Print enter a time in 24 hour format")

# h = int(input("Hours: "))
# m = int(input("Minutes: "))
# s = int(int(input("Seconds: ")))

# if  0 < h <= 24 or 0 <= m < 60 or 0<= s < 60:
#  if h > 12:
#     h1 = h-12
#     print(f"The time you just entered in 12 hour format is {h1:02d}:{m:02d}:{s:02d} PM")
#  elif h == 12:
#     print(f"The time you just entered in 12 hour format is {h:02d}:{m:02d}:{s:02d} PM")
#  elif h == 0:
#     h1 = h +12
#     print(f"The time you just entered in 12 hour format is {h1:02d}:{m:02d}:{s:02d} AM")
#  else:
#     print(f"The time you just entered in 12 hour format is {h:02d}:{m:02d}:{s:02d} AM")

# else:
#    print("Invalid input")  



# while True:

#  x = input("Enter: ")

 
#  y = len(x)

#  if y != 1:
#      continue
#  else:
#   x1 = ord(x)
#   if x1 != 0x2E:
#      if 0x30 <= x1 <= 0x39:
#          print("It's a numeric character")
#      elif 0x41 <= x1 <= 0x5A:
#          print("It's a Capital Letter")
#      elif 0x61 <= x1 <= 0x7A:
#          print("It's a Small-case Letter")
#      else:
#          print("It's a Special Character")

 
#   elif x1 == 0x2E:
#      print("Good Bye.")
#      break
  

#   x = int(input("How much do you want to withdraw: "))

# x1000 = x//1000
# x500 = (x % 1000) // 500
# x100 = (x % 500) // 100


# print("You get:", end = '' )
# if x1000 >= 1:
#     print(x1000, "notes" if x1000 > 1 else "note","of 1000 Baht")

# if x500 >= 1:
#     print("\t",x500, "notes" if x500 > 1 else "note","of 500 Baht")

# if x100 >= 1:
#     print("\t",x100, "notes" if x100 > 1 else "note","of 100 Baht")



# # for i in (50, 0, -1):
# #     if i % 3 == 0 or i % 5 == 0 or i % 6 == 0:
# #         continue
# #     elif i == 1:
# #         print("1.", end = '')
# #     else:
# #         print(i , ",", end = '')


# x = 5
# while x <= 32:
#     if x % 5 == 0 or x % 7 == 0:
#         x += 1  
#         continue
#     if x == 32:
#         print(x)
#     else:
#         print(x, end=', ')
#     x += 1

# import turtle as t
# def square(n):
#     for i in range(4):
#         t.fd(100/n)
#         t.right(90)

# def squareb(n):
#     for i in range(4):
#         t.fillcolor("black")
#         t.begin_fill()
#         t.fd(100/n)
#         t.right(90)
#         t.end_fill()

# def square_brd(n):
#     for i in range(n):
#         for a in range(n):
#             if a % 2 != 0:
#                 t.fillcolor("white")
#                 t.begin_fill()
#                 square(n)
#                 t.end_fill()
#                 t.fd((100/n))
#             else:
#                 t.fillcolor("black")
#                 t.begin_fill()
#                 squareb(n)
#                 t.end_fill()
#                 t.fd((100/n))
           
#         t.penup()
#         t.right(90)
#         t.fd(100/n)
#         t.left(90)
#         t.back(100)
#         t.pendown()

# square_brd(8)

# t.done()

# import turtle as t

# def draw_sq(n):
#     for i in range(4):
#         t.pendown()
#         t.forward(100/n)
#         t.right(90)
#         t.penup()


# def chess(n):

#     for i in range(n):
#         t.penup()
#         t.left(90)
#         t.backward(100/n)
#         t.right(90)
#         t.backward((100/n)*n)

#         for j in range(n):
#             if (i+j)%2 == 0:
#                 color = "white"
#             else: 
#                 color = "black"
#             t.fillcolor(color)
#             t.begin_fill()
#             draw_sq(n)
#             t.end_fill()
#             t.pendown()
#             t.forward(100/n)

#     t.done()

# import turtle as t 

# def tri(n):
#     for i in range(3):
#         t.fd(n)
#         t.left(120)

# def spin(n):
#     while n > 5:
#         tri(n)
#         t.penup()
#         t.fd(n/9)
#         t.left(90)
#         t.fd(n/15)
#         t.right(90)
#         t.pendown()
#         t.left(4)
#         n = n * 0.70

# spin(100)
# t.done()

# import turtle

# N = int(input("Enter the frequent of the table: "))

# t = turtle
# fb = 100 / N
# def square(N):
#     for i in range(N):
#         t.fd(fb)
#         t.right(90)

# for a in range(N):
#     for i in range(N):
#          if (a % 2 == 0 and i % 2 == 0) or (a % 2 == 1 and i % 2 == 1):
#             t.fillcolor("Black")
#             t.begin_fill()
#             for j in range(4):
#                 square(N)
#          else:
#               for j in range(4):
#                 square(N)
#          t.end_fill()
#          t.fd(fb)
#     t.left(90)
#     t.fd(fb)
#     t.left(90)
#     t.fd(100)
#     t.right(180)
# import turtle as t 

# def draw_sq (n):
#     t.penup()
#     t.left(90)
#     t.fd(n/2)
#     t.right(90)
#     t.back(n/2)
#     t.pendown()
#     for i in range(4):
#         t.fd(n)
#         t.right(90)
#     t.penup()
#     t.fd(n/2)
#     t.right(90)
#     t.fd(n/2)
#     t.left(90)
#     t.pendown()

# def shrink(s,g):
#     while s > 20:
#         draw_sq(s)
#         s = s-(g*2)


# def draw(s):
#     for i in range(4):
#         t.fd(s)
#         t.right(90)
# def shrink(s,g):
#     while s > 20:
#         draw(s)
#         t.penup()
#         t.fd(g)
#         t.right(90)
#         t.fd(g)
#         t.left(90)
#         t.pendown()
#         s = s-(g*2)
# shrink(200,20)

# import turtle as t
# def circle(n):
#     t.circle(n)
#     t.penup()

# def shrink(n):
#     while n > 5:
#         circle(n)
#         t.penup()
#         t.left(90)
#         t.fd(n - (n* 0.75))
#         t.right(90)
#         t.pendown()
#         n = n * 0.75

# shrink(150)
# t.done()

# import turtle as t

# x = int(input("Hi"))


# def square(n):
#     for i in range(5):
#         if i == 4:
#             t.fd(n)
#         else:
#             t.fd(n)
#             t.right(90)
        
      


# def chess(x):
#     n = 100/x
#     for i in range (x):
#         for j in range (x):
#             square(n)
            
#         t.penup()
#         t.right(90)
#         t.fd(n)
#         t.left(90)
#         t.back(100)
#         t.pendown()

# chess(5)

# t.done()

# import turtle as t

# def star (n):
#     for i in range(5):
#         t.fd(n)
#         t.right(144)
# def shrink(n):
#     star(200)
#     t.done()
