# # for i in (50, 0, -1):
# #     if i % 3 == 0 or i % 5 == 0 or i % 6 == 0:
# #         continue
# #     elif i == 1:
# #         print("1.", end = '')
# #     else:
# #         print(i , ",", end = '')


x = int(input("How much do you want to withdraw: "))

x1000 = x//1000
x500 = (x % 1000) // 500
x100 = (x % 500) // 100


print("You get:", end = '' )
if x1000 >= 1:
    print(x1000, "notes" if x1000 > 1 else "note","of 1000 Baht")

if x500 >= 1:
    print("\t",x500, "notes" if x500 > 1 else "note","of 500 Baht")

if x100 >= 1:
    print("\t",x100, "notes" if x100 > 1 else "note","of 100 Baht")




while True:

 x = input("Enter: ")

 
 y = len(x)

 if y != 1:
     continue
 else:
  x1 = ord(x)
  if x1 != 0x2E:
     if 0x30 <= x1 <= 0x39:
         print("It's a numeric character")
     elif 0x41 <= x1 <= 0x5A:
         print("It's a Capital Letter")
     elif 0x61 <= x1 <= 0x7A:
         print("It's a Small-case Letter")
     else:
         print("It's a Special Character")

 
  elif x1 == 0x2E:
     print("Good Bye.")
     break

print("Please enter a time in 24 hour format.")
h = int(input("Hours: "))
m = format(int(input("Minutes: ") ), '02d')
s = format(int(input("Seconds: ")), '02d')

m1 = str(m)
s1 = str(s)

if h == 12:
   h1 = format(h, '02d')
   print("The time you entered in 12 hours is ",end = '')
   print(str(h1) +':'+ m1 +':' + s1 , end = '')
   print(" AM")
  
  
elif h == 0:
   h0 = h - 12
   h1 = format(h0, '02d')
   print("The time you entered in 12 hours is ",end = '')
   print(str(h1) +':'+ m1 +':' + s1 , end = '')
   print(" PM")

elif 0 < h <= 12:
   h1 = format(h, '02d')
   print("The time you entered in 12 hours is ",end = '')
   print(str(h1) +':'+ m1 +':' + s1 , end = '')
   print(" AM")

elif 12 < h <= 24:
   h0 = h - 12
   h1 = format(h0, '02d')
   print("The time you entered in 12 hours is ",end = '')
   print(str(h1) +':'+ m1 +':' + s1 , end = '')
   print(" PM")






   
# # import turtle as t
# # t.speed(1)
# # def square(size):
# #     t.penup()
# #     t.back(size/2)
# #     t.left(90)
# #     t.fd(size/2)
# #     t.right(90)
# #     t.pendown()
# #     for _ in range(4):
# #         t.fd(size)
# #         t.right(90)
# #     t.penup()
# #     t.fd(size/2)
# #     t.right(90)
# #     t.fd(size/2)
# #     t.left(90)

# # def spiral_sq(size):
# #     while size >= 5:
# #         square(size)
# #         t.left(10)
# #         size *= 0.75

# # spiral_sq(150)
# # t.done()
   
print("Please enter a time in 24 format")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

if hours > 12:
   print(f"The time your just entered in 12 hour format is {hours - 12:02}:{minutes:02}:{seconds:02} PM")
elif hours == 12:
   print(f"The time your just entered in 12 hour format is {hours:02}:{minutes:02}:{seconds:02} PM")
else:
   print(f"The time your just entered in 12 hour format is {hours:02}:{minutes:02}:{seconds:02} AM")

   