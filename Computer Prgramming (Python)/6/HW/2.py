import turtle as t

def calendar_of_2023(x):
    
    day = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    month_end = [00,31,28,31,30,31,30,31,31,30,31,30,31]
    month_start = [00,6,2,2,5,0,3,5,1,4,6,2,4]
    month_list = ['blank :)','January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023', 'July 2023',
             'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023']
    month = month_list[x]
    
    #t.speed(5)
    t.tracer(0)

    t.penup()
    t.setpos(-200,200)
    t.pendown()
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(50,165)
    t.pendown()

    t.write(month, align="center", font=("Verdana", 15, "normal"))

    t.penup()
    t.goto(-200,150)
    t.right(90)
    t.pendown()

    for i in range(7):
        t.forward(500/7)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(500/7)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(500/7)
        end = t.pos()
        center_x = t.xcor() - (500 / 14)
        center_y = t.ycor() - 35
    
        t.penup()
        t.goto(center_x, center_y)
        t.pendown()
        t.write(day[i], align="center", font=("Verdana", 15, "normal"))
        t.penup()
        t.goto(end)
        t.pendown()
    
    t.penup()
    t.goto(-200,100)
    t.pendown()
    
    days = 2

    if x == 1 or x == 7 or x == 10:
        f = 6
    else:
        f = 5
    for a in range(f):
        for i in range(7):
            t.forward(500/7)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500/7)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(500/7)
            end = t.pos()
            cenx = t.xcor() - (500 / 14)
            ceny = t.ycor() - 35
    
            t.penup()
            t.goto(cenx, ceny)
            t.pendown()
            
            if a == 0:
                if i < month_start[x]:
                    ()
                elif i == month_start[x]:
                    t.write(1, align="center", font=("Verdana", 15, "normal"))
                elif i > month_start[x]:
                    t.write(days, align="center", font=("Verdana", 15, "normal"))               
                    days += 1
            else:
                if days <= month_end[x]:
                    t.write(days, align="center", font=("Verdana", 15, "normal"))               
                    days += 1
                else:
                    ()
            t.penup()
            t.goto(end)
            t.pendown()       
              
        t.penup()
        t.goto(-200,t.ycor()-50)
        t.pendown()

    t.done()

calendar_of_2023(8)