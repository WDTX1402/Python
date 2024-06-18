from tkinter import *
from tkinter import messagebox

class Phone:
    def __init__(self):
        window = Tk()
        window.title("PhoneThingy")
        window.geometry('350x450+700+200')

        self.inpus = Entry(window, state='readonly')
        self.inpus.grid(row=0, column=0, columnspan=3)

        buttons = {
            "1": self.add_char, 
            "2": self.add_char, 
            "3": self.add_char,
            "4": self.add_char, 
            "5": self.add_char, 
            "6": self.add_char,
            "7": self.add_char, 
            "8": self.add_char, 
            "9": self.add_char,
            "*": self.add_char, 
            "0": self.add_char, 
            "#": self.add_char,
        }

        row, col = 1, 0
        for btn_text in buttons:
            Button(window, text=btn_text, command=lambda t=btn_text: self.add_char(t)).grid(row=row, column=col, sticky='nsew')
            col += 1
            if col > 2:
                col = 0
                row += 1
        Button(window, text="Talk", command=self.dial_number).grid(row=5, column=0, columnspan=2, sticky='nsew')
        Button(window, text="<", command=self.delete_rightmost_char).grid(row=5, column=2, columnspan=1, sticky='nsew')

        window.columnconfigure((0, 1, 2), weight=1)
        window.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        window.mainloop()

    def add_char(self, char):
        self.inpus.config(state=NORMAL)
        self.inpus.insert(END, char)
        self.inpus.config(state="readonly")

    def dial_number(self):
        number = self.inpus.get()
        messagebox.showinfo("Dialing", f"Dialing {number}")

    def delete_rightmost_char(self):
        text = self.inpus.get()
        if text:
            self.inpus.config(state=NORMAL)
            self.inpus.delete(len(text) - 1)
            self.inpus.config(state="readonly")

Phone()

