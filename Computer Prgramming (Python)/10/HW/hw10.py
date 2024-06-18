#Q1
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


#Q2
def bubble_sort(listin):
    length = len(listin)
    
    for i in range(length):
        swaps = 0
        for i in range(0, length - 1):
            if listin[i] > listin[i + 1]:
                listin[i], listin[i + 1] = listin[i + 1], listin[i]
                swaps += 1
        if swaps == 0:
            break
        length -= 1

    return listin

list = [3,2,9,7,8]
out = bubble_sort(list)
print(out)



#Q3
def my_union(list1, list2):
    return list(set(list1) | set(list2))

def my_intersection(list1, list2):
    return list(set(list1) & set(list2))

def my_difference(list1, list2):
    return list(set(list1) - set(list2))


list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

out1 = (my_union(list1, list2)) 
print(out1)
out2 = my_intersection(list1, list2)
print(out2)
out3 = my_difference(list1, list2)
print(out3) 



#Q4
def print_table(table):
    if not table:
        print("Table is empty")
        return

    column_width = []
    for col in range(len(table[0])):
        max_width = 0
        for row in table:
            cell_width = len(str(row[col]))
            if cell_width > max_width:
                max_width = cell_width
        column_width.append(max_width)


    for i, header in enumerate(table[0]):
        print(header.ljust(column_width[i]), end=" ")
    print()
    for row in table[1:]:
        for i, cell in enumerate(row):
            print(str(cell).ljust(column_width[i]), end=" ")
        print()

table_data1 = [['x', 'y'], [0, 0], [10, 10], [200, 200]]
print_table(table_data1)
print()
table_data2 = [['ID', 'Name', 'Surname'], ['001', 'John', 'Cena'], ['002', 'Vladimir', 'Zelensky'], ['003', 'Joe', 'Mama']]
print_table(table_data2)



#Q5
def isAnagram(string1, string2):
    count1 = {}
    for char in string1:
        count1[char] = count1.get(char, 0) + 1
    
    count2 = {}
    for char in string2:
        count2[char] = count2.get(char, 0) + 1

    if count1 == count2:
        return "True"
    else:
        return "False"

word1 = "listen"
word2 = "silent"
out1 = isAnagram(word1, word2)
print(out1)

word1 = "hello"
word2 = "helnaw"
out2 = isAnagram(word1, word2)
print(out2)
