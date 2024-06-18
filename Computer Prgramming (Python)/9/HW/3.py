from tkinter import *
from tkinter import messagebox

class CircleThingy:
    def __init__(self):
        self.window = Tk()
        self.window.title("CircleThingy")
        self.canvas = Canvas(self.window, width=500, height=300, bg='white')
        self.canvas.pack(padx=0, pady=0)

        self.prev = None 

  
        self.canvas.bind('<Button-1>', self.draw)
        self.canvas.bind('<Button-3>', self.dele)

        self.window.mainloop() 

    def draw(self, move_event):
        self.canvas.create_oval(move_event.x + 10, move_event.y + 10, move_event.x - 10, move_event.y - 10, width=1, fill='white')
        self.prev = move_event

    def dele(self, move_event):
        item = self.canvas.find_closest(move_event.x, move_event.y)
        x1, y1, x2, y2 = self.canvas.coords(item)
        
        if x1 <= move_event.x <= x2 and y1 <= move_event.y <= y2:
            self.canvas.delete(item)

        self.prev = move_event


CircleThingy()
