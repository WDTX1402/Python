import turtle

def draw_pie_chart(list1):
    count_dict = {}
    
    for num in list1:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    counts = list(count_dict.values())
    total = sum(counts)

    pie_turtle = turtle.Turtle()
    pie_turtle.speed(10)  
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan']

    pie_turtle.penup()
    pie_turtle.goto(0, -150)
    pie_turtle.pendown()

    start_angle = 0
    for i, count in enumerate(counts):
        angle = (count/total) * 360
        pie_turtle.color(colors[i % len(colors)])
        pie_turtle.begin_fill()
        pie_turtle.setheading(start_angle)
        pie_turtle.forward(150)
        pie_turtle.left(90)
        pie_turtle.circle(150, angle)
        pie_turtle.left(90)
        pie_turtle.forward(150)
        pie_turtle.end_fill()
        start_angle += angle


data_list = [3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3]
draw_pie_chart(data_list)

turtle.done()


