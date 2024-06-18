from tkinter import *
master = Tk()

canvas = Canvas(master, width=600, height=300, bg='white')
canvas.pack(padx=20, pady=20)


def move(move_event):
    global prev
    prev = move_event


def drag(move_event):
    global prev
    canvas.create_line(prev.x, prev.y, move_event.x, move_event.y, width=10)
    prev = move_event

def clear():
    canvas.delete('all')
    

canvas.bind('<Button-1>', move)
canvas.bind('<B1-Motion>', drag)
clearr = Button(master, text = "Clear men shampoo", command = clear)
clearr.pack(padx=20, pady=310)


