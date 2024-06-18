from tkinter import *

class Setting(object):
    def __init__(self, master, mainapp, setting_type):
        self.master = master
        self.mainapp = mainapp
        self.master.title("Settings")

        if setting_type == "tables":
            self.ui_table_settings()
        elif setting_type == "menus":
            self.ui_menu_settings()

        self.save_btn = Button(self.master, text="Save Settings", command=self.save_setting)
        self.save_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=20)

    def ui_table_settings(self):
    
        self.label_tables = Label(self.master, text="Number of Tables:")
        self.label_tables.grid(row=0, column=0, padx=20, pady=10)

        self.num_tables_var = IntVar(value=self.mainapp.num_tables) 
        self.entry_tables = Entry(self.master, textvariable=self.num_tables_var)
        self.entry_tables.grid(row=0, column=1, padx=20, pady=10)

    def ui_menu_settings(self):
  
        self.label_menu = Label(self.master, text="Menu Item:")
        self.label_menu.grid(row=1, column=0, padx=20, pady=10)

        self.menu_name_var = StringVar()
        self.entry_menu = Entry(self.master, textvariable=self.menu_name_var)
        self.entry_menu.grid(row=1, column=1, padx=20, pady=10)

        self.label_price = Label(self.master, text="Price:")
        self.label_price.grid(row=2, column=0, padx=20, pady=10)

        self.menu_price_var = IntVar()
        self.entry_price = Entry(self.master, textvariable=self.menu_price_var)
        self.entry_price.grid(row=2, column=1, padx=20, pady=10)

        self.menu_listbox = Listbox(self.master)
        for menu_item, price in self.mainapp.menu.items():
            self.menu_listbox.insert(END, f"{menu_item}: ฿{price}")
        self.menu_listbox.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

        self.add_btn = Button(self.master, text="Add Menu Item", command=self.add_menu_item)
        self.remove_btn = Button(self.master, text="Remove Menu Item", command=self.remove_menu_item)
        self.add_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10)
        self.remove_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

   



    def add_menu_item(self):
        menu_name = self.menu_name_var.get().strip()
        menu_price = self.menu_price_var.get()
        
        if menu_name:
            self.mainapp.menu[menu_name] = menu_price
            self.menu_listbox.insert(END, f"{menu_name}: ฿{menu_price}")
            self.menu_name_var.set('')
            self.menu_price_var.set(0.0)

    def remove_menu_item(self):
    
        selected_index = self.menu_listbox.curselection() 
        if selected_index: 
            selected_text = self.menu_listbox.get(selected_index)
            menu_name = selected_text.split(":")[0].strip()
    
            if menu_name in self.mainapp.menu:
                del self.mainapp.menu[menu_name]

            self.menu_listbox.delete(selected_index)

    def save_setting(self):
        if hasattr(self, 'num_tables_var'):
            self.mainapp.num_tables = self.num_tables_var.get() 
            self.mainapp.generate_tables()
        self.master.destroy()
        