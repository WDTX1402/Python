import tkinter as tk
from tkinter import messagebox

class InfoApp:
    def __init__(self, root):
    
        root.title('Information')

        self.lbl_name = tk.Label(root, text="Name:")
        self.lbl_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.ent_name = tk.Entry(root)
        self.ent_name.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_age = tk.Label(root, text="Age:")
        self.lbl_age.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.ent_age = tk.Entry(root)
        self.ent_age.grid(row=1, column=1, padx=10, pady=10)

        self.lbl_address = tk.Label(root, text="Address:")
        self.lbl_address.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.ent_address = tk.Entry(root, width=40)
        self.ent_address.grid(row=2, column=1, padx=10, pady=10)

        self.btn_submit = tk.Button(root, text="Submit", command=self.show_info)
        self.btn_submit.grid(row=3, column=0, columnspan=2, pady=20)

    def show_info(self):
        name = self.ent_name.get()
        age = self.ent_age.get()
        address = self.ent_address.get()

     
        messagebox.showinfo('Entered Information', f'Name: {name}\nAge: {age}\nAddress: {address}')

if __name__ == '__main__':
    root = tk.Tk()
    app = InfoApp(root)
    root.mainloop()
