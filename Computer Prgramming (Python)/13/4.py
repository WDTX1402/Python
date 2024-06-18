import turtle

def draw_cross(length, depth):
    if depth == 0:
        return
 
    # Draw the vertical part of the cross with dots at the ends
    turtle.left(90)
    turtle.forward(length/2)
    turtle.dot(5)
    draw_cross(length/2, depth-1)
    turtle.backward(length)
    turtle.dot(5)
    draw_cross(length/2, depth-1)
    turtle.forward(length/2)
    turtle.right(90)
    
    # Draw the horizontal part of the cross with dots at the ends
    turtle.forward(length/2)
    turtle.dot(5)
    draw_cross(length/2, depth-1)
    turtle.backward(length)
    turtle.dot(5)
    draw_cross(length/2, depth-1)
    turtle.forward(length/2)

turtle.tracer(0)  


# Draw the cross with length 100 and depth 4
draw_cross(200, 4)

turtle.done()
# import turtle as t
# t.speed(0)

# def cross(size, level):
#     if level > 0:
#         for i in range(4):
#             t.fd(size)
#             cross(size / 2, level - 1)
#             t.bk(size)
#             t.rt(90)
#     else:
#         t.dot(4)

# cross(100, 5)

# t.ht()
# t.done()