from tkinter import *
from tkinter import messagebox 

window = Tk()
window.title("KMITL Phone")

strr = ""

def o():
    label.insert(END, "1")
def tw():
    label.insert(END, "2")
def th():
    label.insert(END, "3")
def fo():
    label.insert(END, "4")
def fi():
    label.insert(END, "5")
def si():
    label.insert(END, "6")
def se():
    label.insert(END, "7")
def e():
    label.insert(END, "8")
def n():
    label.insert(END, "9")
def z():
    label.insert(END, "0")
def st():
    label.insert(END, "*")
def ht():
    label.insert(END, "#")
def t():
    show = label.get()
    messagebox.showinfo("Dialing", f"Dialing {show}")
def de():
    de = label.get()
    label.delete(len(de) - 1)
        

one = Button(window, text = "1", command = o).grid(row = 3, column = 5, columnspan = 3)
two = Button(window, text = "2", command = tw).grid(row = 3, column = 8, columnspan = 3)
three = Button(window, text = "3", command = th).grid(row = 3, column = 13, columnspan = 3)
four = Button(window, text = "4", command = fo).grid(row = 6, column = 5, columnspan = 3)
five = Button(window, text = "5", command = fi).grid(row = 6, column = 8, columnspan = 3)
six = Button(window, text = "6", command = si).grid(row = 6, column = 13, columnspan = 3)
sev = Button(window, text = "7", command = se).grid(row = 9, column = 5, columnspan= 3)
eight = Button(window, text = "8", command = e).grid(row = 9, column = 8, columnspan=3)
nine = Button(window, text = "9", command = n).grid(row = 9, column = 13, columnspan = 3)
zero = Button(window, text = "0", command = z).grid(row = 12, column = 8, columnspan = 3)
star = Button(window, text = "*", command = st).grid(row = 12, column = 5, columnspan = 3)
hashtag = Button(window, text = "#", command = ht).grid(row = 12, column = 13, columnspan = 3)
talk = Button(window, text = "Talk", command = t).grid(row = 15, column = 5, columnspan = 7)
delete = Button(window, text = "<", command = de).grid(row = 15, column = 8, columnspan = 7)
label = Entry(window, text = strr)
label.grid(row = 1, column = 1, columnspan = 9)

window.mainloop()