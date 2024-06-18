from tkinter import *
from tkinter import messagebox

class convert:
    def __init__(self):
        window = Tk()
        window.title("USD -> THB")

        self.inpus = Entry(window)
        self.inpus.grid(row = 1, columnspan= 10)
        Button(window, text = "USD -> THB", command= self.toTHB).grid(row = 2,columnspan= 5)
        Button(window, text = "THB -> USD", command= self.toUSD).grid(row = 3,columnspan= 5)
    

        window.mainloop()

    def toUSD(self):
        result = int(self.inpus.get()) / 30
        messagebox.showinfo("THB -> USD", result)

    def toTHB(self):
        result = int(self.inpus.get()) * 30
        messagebox.showinfo("USD -> THB", result)
    

convert()