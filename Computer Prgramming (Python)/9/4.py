from tkinter import *
from tkinter import messagebox
from random import *
window = Tk()

canvas = Canvas(window, width = 500, height = 300 ,bg = 'white')

canvas.create_rectangle(0,0,350,200)
canvas.pack(padx=0, pady=0)

def move(move_event):
    global prev
    prev = move_event


def drag(move_event):
    global prev
    randum = randint(1,5)
    if randum == 1:
        colo = 'white'
    elif randum == 2:
        colo = 'red'
    elif randum == 3:
        colo = 'yellow'
    elif randum == 4:
        colo = 'green'
    elif randum == 5:
        colo = 'blue'
    if not(move_event.x <= 350 and move_event.y <= 200):
        messagebox.showwarning("showwarning", "Warning")
    else:
        canvas.create_oval(move_event.x +5, move_event.y +5, move_event.x, move_event.y, width=1, fill = colo)
        prev = move_event

     
         
canvas.bind('<Button-1>', drag)


mainloop()