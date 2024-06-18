#1
def converttime(x):
    extract1 = x[0:2]
    extract2 = x[3:5]
    hours = int(extract1)
    mins = int(extract2)
    if 23 >= hours >= 0 and 0 <= mins <= 59:
        if hours == 00:
            return str(hours) + ":" + x[3:5] + "AM"
        elif 1 <= hours < 12:
            return str(hours) + ":" + x[3:5] + "AM"
        elif hours == 12:
            return str(hours) + ":" + x[3:5] + "PM"
        elif 23 >= hours > 12.:
            ans = hours - 12
            return str(ans) + ":" + x[3:5] + "PM"
    else:
        return "Invalid time format"

converted_hours = converttime("13:54")
print(converted_hours)

#2
import turtle as t
    
def calendar_of_2023(x):
    
    day = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    month_end = [00,31,28,31,30,31,30,31,31,30,31,30,31]
    month_start = [00,6,2,2,5,0,3,5,1,4,6,2,4]
    month_list = ['blank :)','January 2023', 'February 2023', 'March 2023', 'April 2023', 'May 2023', 'June 2023', 'July 2023',
             'August 2023', 'September 2023', 'October 2023', 'November 2023', 'December 2023']
    month = month_list[x]
    
    #t.speed(10)
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

#3
def shoutnumber(n):
    sdigit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen","I don't know"]
    ddigit = ["s", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 <= n <= 999:
        if n == 0:
            return "zero"
        elif n < 20:
            return sdigit[n]
        elif n < 100:
            if n % 10 == 0:
                return ddigit[n // 10]
            else:
                return ddigit[n // 10] + "-" + sdigit[n % 10]
        elif n >= 100:
            if n % 100 == 0:
                return sdigit[n // 100] + " hundred"
            else:
                s = n % 100
                if s < 20:
                    return sdigit[n // 100] + " hundred and "+ sdigit[s]
                elif s < 100:
                    if s % 10 == 0:
                     return sdigit[n // 100] + " hundred and "+ ddigit[s // 10]
                    else:
                     return sdigit[n // 100] + " hundred and "+ ddigit[s // 10] + "-" + sdigit[s % 10]
    else:
        return sdigit[20]
    
amogus = shoutnumber(999)
print(amogus)

#4
def money(x):

    x1000 = x // 1000
    x500  = (x % 1000) // 500
    x100  = (x % 500) // 100
    x50   = (x % 100) // 50
    x20   = (x % 50) // 20 
    x10   = (x % 20) // 10
    x5    = (x % 10) // 5
    x2    = (x % 5) // 2
    x1    = x % 2

    return [x1000, x500, x100, x50, x20, x10, x5, x2, x1]
   


outing = money(1603)
print("1000-Baht notes:", outing[0] ,"\n",
      "500-Baht notes:", outing[1] ,"\n",
      "100-Baht notes:", outing[2] ,"\n",
      "50-Baht notes:", outing[3] ,"\n",
      "20-Baht notes:", outing[4] ,"\n",
      "10-Baht coins:", outing[5] ,"\n",
      "5-Baht coins:", outing[6] ,"\n",
      "2-Baht coins:", outing[7] ,"\n",
      "1-Baht coins:", outing[8] ,"\n")

#5
def reverse(x):
    xx = str(x)
    return xx[3] + xx[2] + xx[1] + xx[0]  

komp = reverse(3456)
print(komp)

def reverse2(x):
    xx = str(x)
    
    return xx[:: -1] 


komp = reverse(3456) , reverse2(3456)
print(komp)