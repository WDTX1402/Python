# sum = 0
# i = 5
# while i > 0 :
#     inpus = int(input("Please enter an interger:"))
#     if (sum >= 0 and inpus >= 0) or (sum < 0 and inpus < 0):
#        sum += inpus
#     else:
#        sum = inpus
#     print("Current sum: ", sum)
#     i -= 1
# import turtle as t
# def star(n):
#    for i in range(5):
#       t.fd(n)
#       t.right(144)
# star(150)
# t.done()


import turtle as t
def draw_sth(sides):
    for i in range(sides):
        t.forward(50)
        t.left(360/sides)

draw_sth(6)
t.done()

