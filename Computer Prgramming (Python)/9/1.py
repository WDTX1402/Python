from tkinter import *

def plus():
        numdis["text"] += 1
def minus():
        numdis["text"] -= 1
def resetto():
        numdis ["text"] = 0

window = Tk()
window.title("Spinner")
num = 0

numdis = Label(window, text = num)
numdis.grid(row = 2, column = 1)
        
plusbutt = Button(window, text = "+", command= plus).grid(row = 1, column = 2,columnspan= 5)
minusbutt =Button(window, text = "-", command= minus).grid(row = 2, column = 2,columnspan= 5)
reset = Button(window, text = "Reset", command= resetto).grid(row = 3, column = 2,columnspan= 5)

        # plusbutt.pack()
        # minusbutt.pack()
        # reset.pack()
window.mainloop()
