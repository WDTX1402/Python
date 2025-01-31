from tkinter import *
from tkinter import Tk, Label,messagebox,filedialog
from PIL import Image, ImageTk
from settings import Setting
import time 
import pickle
import abc

class MenuUI(object):
    def __init__(self, master, callback_map):
        self.menubar = Menu(master)
        
        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="New", command=callback_map["new_data"])
        self.file_menu.add_command(label="Save", command=callback_map["save_data_as"])
        self.file_menu.add_command(label="Load", command=callback_map["load_data"])
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        
        self.setting_menu = Menu(self.menubar, tearoff=0)
        self.setting_menu.add_command(label="Set Tables", command=lambda: callback_map["open_setting"]("tables"))
        self.setting_menu.add_command(label="Set Menus", command=lambda: callback_map["open_setting"]("menus"))
        self.menubar.add_cascade(label="Setting", menu=self.setting_menu)

        # self.member_menu = Menu(self.menubar, tearoff=0)
        # self.member_menu.add_command(label="Membership settings", command=callback_map["membership"])
        # self.menubar.add_cascade(label="Membership", menu=self.member_menu)

        self.help_menu = Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label="About", command=callback_map["about"])
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        master.config(menu=self.menubar)


class MenuManager:
    def __init__(self, window, middle_frame,tables_frame):
        self.window = window
        self.middle_frame = middle_frame
        self.num_tables = 0
        self.menu = {}

        self.table_manager = TableManager(self,middle_frame,tables_frame)
        self.order_manager = OrderManager(self, self.table_manager)

        # Create MENU
        self.menu_callbacks = {
            "new_data": self.new_data,
            "save_data_as": self.save_data_as,
            "load_data": self.load_data,
            "open_setting": self.open_setting,
            "about": self.about
        }

        self.menuUI = MenuUI(window, self.menu_callbacks)

    def open_setting(self, setting_type):
        setting_window = Toplevel(self.window)
        Setting(setting_window, self, setting_type)

    def save_data_as(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])
        if file_name:
            with open(file_name, 'wb') as f:
                pickle.dump(self.num_tables, f)
                pickle.dump(self.menu, f)
            print(f"Data saved to {file_name}.")
            self.current_file = file_name

        pass


    def load_data(self):
        file_name = filedialog.askopenfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])
       
        if file_name:
            try:
                self.menu = {}
                for widget in self.middle_frame.winfo_children():
                    widget.destroy()

                with open(file_name, 'rb') as f:
                    self.num_tables = pickle.load(f)
                    self.menu = pickle.load(f)
                self.table_manager.generate_tables() 
                print(f"Data loaded from {file_name}.")
                self.current_file = file_name
        
                return self.num_tables
            except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
                messagebox.showerror('Error', 'Data could not be loaded')
                print(f"Error loading data: {e}")

        pass

    def new_data(self):
        for widget in self.middle_frame.winfo_children():
            widget.destroy()
            
        self.menu = {}
        self.num_tables = 0
        self.table_manager.generate_tables() 
        self.current_file = None
        print("Started a new file.")

        pass

    def about(self):
        about_window = Toplevel(self.window)
        about_window.title("About")
        Label(about_window, text="Restaurant Manager\nVersion 1.0\nBy GE WDTX1402").pack(pady=20, padx=20)
        Button(about_window, text="Close", command=about_window.destroy).pack(pady=20)


class TableManager:
    def __init__(self, menu_manager,middle_frame,tables_frame):
        self.menu_manager = menu_manager
        self.window = menu_manager.window
        self.table_frame = tables_frame
        self.middle_frame = middle_frame
        self.num_tables = menu_manager.num_tables
        self.menu = menu_manager.menu
        self.table_vars = {}
        self.reservationlist = {i: "Guest" for i in range(1, self.num_tables + 1)}
        self.reservationguest = {i: None for i in range(1, self.num_tables + 1)}
        self.current_file = None
        self.table_status = {i: "dormant" for i in range(1, self.num_tables + 1)}

        #Create Tables 
        self.create_tables()
                
        


    def generate_tables(self):
        for widget in self.inner_tables_frame.winfo_children(): 
            widget.destroy()

        for i in range(1, self.num_tables + 1):
            table = Button(self.inner_tables_frame, text=f"Table {i}", font=('Arial', 12, 'bold'), bg="white", width=17, height=2,  
                        command=lambda table_num=i: self.toggle_table_display(table_num))
            table.pack(pady=5)
        
        self.table_status = {i: "dormant" for i in range(1, self.num_tables + 1)}
        self.reservationlist = {i: "Guest" for i in range(1, self.num_tables + 1)}
        print(self.reservationlist)
        self.reservationguest = {i: None for i in range(1, self.num_tables + 1)}

    def toggle_table_display(self, table_num):
        if self.table_status[table_num] == "dormant":
            self.display_dormant_table(table_num)
        elif self.table_status[table_num] == "active":
            self.display_activated_table(table_num)
        elif self.table_status[table_num] == "reserved":
            self.display_reserved_table(table_num)


    def create_tables(self):
    
        scrollbar = Scrollbar(self.table_frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        canvas = Canvas(self.table_frame, width=180, yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=canvas.yview)
        self.inner_tables_frame = Frame(canvas)  
        canvas.create_window((0, 0), window=self.inner_tables_frame, anchor="nw") 
        self.inner_tables_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) 


    def display_dormant_table(self, table_number):
        self.table_status[int(table_number)] = "dormant"
        
        for widget in self.middle_frame.winfo_children():
            widget.destroy()

        table_label = Label(self.middle_frame, text=f"Table {table_number}", font=('Arial', 26, 'bold'))
        table_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        options_label = Label(self.middle_frame, text="Options:", font=('Arial', 24), bg="gray",height= 5)
        options_label.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        reserve_btn = Button(self.middle_frame, text="Reserve", font=('Arial', 20), bg="white",width= 22 ,height= 4,
                            command=lambda: self.reservation(table_number))
        reserve_btn.grid(row=2, column=0, pady=10, padx=10)

        activ_btn = Button(self.middle_frame, text="Activate", font=('Arial', 20), bg="green",width= 22 ,height= 4,
                        command=lambda: self.activate_table(table_number))
        activ_btn.grid(row=2, column=2, pady=10, padx=10)

        # clreserve_btn = Button(self.middle_frame, text=f" Cancel\nReservation ", font=('Arial', 20), bg="white", width=13, height=3)
        # clreserve_btn.grid(row = 4, column = 1, padx= 10)


    def reservation(self,table_num):
    
        self.reserve_window = Toplevel(self.window)
        self.reserve_window.title(f"Reservation Info Table #{table_num}")

        Label(self.reserve_window, text="Enter customer's name").pack(padx=10, pady=10)
        name_entry = Entry(self.reserve_window, bd=5, width=35)
        name_entry.pack(pady=10)
        Label(self.reserve_window, text="Enter number of guests").pack(padx=10, pady=10)
        seats = Entry(self.reserve_window, bd=5, width=35)
        seats.pack(pady=10)

        
        Button(self.reserve_window, text="save", command=lambda: self.save_reservation(table_num, name_entry,seats)).pack(pady=20)
        Button(self.reserve_window, text="Close", command=self.reserve_window.destroy).pack(pady=20)

   
        # reserve_window.update_idletasks()
        # width = reserve_window.winfo_width()
        # height = reserve_window.winfo_height()
        # x = (reserve_window.winfo_screenwidth() // 2) - (width // 2)
        # y = (reserve_window.winfo_screenheight() // 2) - (height // 2)
        # reserve_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def save_reservation(self, table_num, name_entry, guests):

        customer_name = name_entry.get()
        guestsnum = guests.get()

        if customer_name.strip() and guestsnum.strip():
            self.reservationlist[table_num] = customer_name
            self.reservationguest[table_num] = guestsnum
            print(self.reservationlist)
            self.table_status[table_num] = 'reserved'
            self.display_reserved_table(table_num)
            messagebox.showinfo("Success!", f"Table #{table_num} has been reserved for {customer_name} ({guestsnum} guests)")
            self.reserve_window.destroy()
        else:
            messagebox.showerror("Error", "All box must be filled!")

    def display_reserved_table(self, table_number):
        self.table_status[int(table_number)] = "reserved"
        
        for widget in self.middle_frame.winfo_children():
            widget.destroy()
            
        table_label = Label(self.middle_frame, text=f"Table {table_number}", font=('Arial', 26, 'bold'))
        table_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

        infobox = Label(self.middle_frame, 
                        text=f"This table has been reserved!\nTable {table_number} has been reserved for {self.reservationlist[table_number]} ({self.reservationguest[table_number]} guests)", 
                        font=('Arial', 18, 'bold'))
        infobox.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        options_label = Label(self.middle_frame, text="Options:", font=('Arial', 24), bg="gray")
        options_label.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

        activ_btn = Button(self.middle_frame, text="Activate", font=('Arial', 20), bg="green",width= 22 ,height= 4,
                        command=lambda: self.activate_table(table_number))
        activ_btn.grid(row=3, column=0, pady=10, padx=10)

        clreserve_btn = Button(self.middle_frame, text="Cancel\nReservation", font=('Arial', 20), bg="white",width= 22 ,height= 4,
                            command=lambda: self.cancel_reservation(table_number))
        clreserve_btn.grid(row=3, column=1, pady=10, padx=10)

        # for i in range(1, table_number+ 1):
        #     reserve_btn = Button(self.middle_frame, text=f" Reserve ", font=('Arial', 20), bg="white", width=13, height=3,
        #                         command=lambda i=i: self.reservation(i))
        #     reserve_btn.grid(row = 4, column = 0, padx= 10)

    def activate_table(self, table_num):
        self.display_activated_table(table_num)        
        self.table_status[table_num] = 'active'

    def cancel_reservation(self, table_num):
        self.display_dormant_table(table_num)
        self.reservationlist[table_num] = 'Guest'
        self.reservationguest[table_num] = None


    def display_activated_table(self, table_number):
        print(f"Received table number: {table_number} {self.reservationlist[table_number]} ({self.reservationguest[table_number]})")


        for widget in self.middle_frame.winfo_children():
            widget.destroy()

        table_label = Label(self.middle_frame, text=f"Table {table_number} {self.reservationlist[table_number]} ({self.reservationguest[table_number]} guests)",
                             font=('Arial', 20, 'bold'), )
        table_label.pack(pady=10)

        #create the order frame 
        order_frame = Frame(self.middle_frame, bg='white')
        order_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=10)

        #scrollbar inside order_frame
        scrollbar = Scrollbar(order_frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        #canvas inside order_frame
        self.menucanvas = Canvas(order_frame, yscrollcommand=scrollbar.set, bg='white', bd=2, relief='ridge')
        self.menucanvas.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.menucanvas.yview)

        #frame inside Canvas
        self.menu_frame = Frame(self.menucanvas, bg='white', pady=5)
        self.menucanvas.create_window((0, 0), window=self.menu_frame, anchor="nw")
        self.menu_frame.bind("<Configure>", lambda e: self.menucanvas.configure(scrollregion=self.menucanvas.bbox("all")))


        self.summary_frame = Frame(self.middle_frame, bg='lightgray')
        self.summary_frame.pack(side=RIGHT, fill=BOTH, padx=5, pady=10, expand=True)

        # Packing the Order Summary label at the top of the summary_frame
        order_summary_label = Label(self.summary_frame, text="Order Summary", font=('Arial', 14),bg='lightgray')
        order_summary_label.pack(pady=10)

        # Create a frame to hold the listbox and its scrollbar
        self.summarylist_frame = Frame(self.summary_frame)
        self.summarylist_frame.pack(fill=BOTH, expand=True)

        # Create the scrollbar inside summarylist_frame
        order_listbox_scrollbar = Scrollbar(self.summarylist_frame, orient=VERTICAL)
        order_listbox_scrollbar.pack(side=RIGHT, fill=Y)

        # Create the listbox associated with the scrollbar inside summarylist_frame
        self.order_listbox = Listbox(self.summarylist_frame, font=('Arial', 13), height=15, width=25, yscrollcommand=order_listbox_scrollbar.set)
        self.order_listbox.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=10)

        # Connect the scrollbar to the listbox
        order_listbox_scrollbar.config(command=self.order_listbox.yview)


        self.checkout_frame = Frame(self.summary_frame, bg = 'gray')
        self.checkout_frame.pack(side=BOTTOM, fill=BOTH, padx=5, pady=10, expand=True)

        self.total_cost_var = StringVar(value="Total: ฿0.00")
        self.total_cost_label = Label(self.checkout_frame, textvariable=self.total_cost_var, font=('Arial', 12))
        self.total_cost_label.pack(side = TOP,pady=20, anchor='s')

        if not hasattr(self, 'table_orders'):  
            self.table_orders = {}

        if table_number not in self.table_orders:
            self.table_orders[table_number] = {}

        # Clear the listbox for order summary:
        self.order_listbox.delete(0, END)

        for item, qty in self.table_orders[table_number].items():
            if qty > 0:
                price = self.menu[item]
                self.order_listbox.insert(END, f"{item} x{qty} - ฿{price * qty:.2f}")
 
        for menu_item , menu_price in self.menu.items():
            item_frame = Frame(self.menu_frame) 
            item_frame.pack(fill=X, pady=5)

            menu_label = Label(item_frame, text=menu_item,font=('Arial', 12), width=15, anchor=W)
            menu_label.pack(side=LEFT)

            price_label = Label(item_frame, text=f"฿ {menu_price}",font=('Arial', 12), width=15, anchor=W)
            price_label.pack(side=LEFT)

            qty_var = IntVar(value=self.table_orders[table_number].get(menu_item, 0))
            qty_label = Label(item_frame, textvariable=qty_var, width=5, relief="solid", bd=1)
            qty_label.pack(side=LEFT, padx=5)

            add_btn = Button(item_frame, text="+", command=lambda var=qty_var, item=menu_item: self.update_order(var, item, table_number, 1))
            add_btn.pack(side=LEFT)

            sub_btn = Button(item_frame, text="-", command=lambda var=qty_var, item=menu_item: self.update_order(var, item, table_number, -1))
            sub_btn.pack(side=LEFT, padx=5)

            self.table_vars[menu_item] = qty_var
            self.table_orders[table_number][menu_item] = qty_var.get()

            saved_qty = self.table_orders[table_number].get(menu_item, 0)
            qty_var.set(saved_qty)

        total_cost = self.compute_total_cost(table_number)
        self.total_cost_var.set(f"Total: ฿{total_cost:.2f}")

        save_btn = Button(self.middle_frame, text="Save Order",font=('Arial', 12), width=20, height=2, command=lambda: self.save_order(table_number))
        save_btn.pack(padx= 5,pady=30)
        
        delete_btn = Button(self.middle_frame, text="Delete Order",font=('Arial', 12), width=20, height=2, command=lambda: self.delete_order(table_number))
        delete_btn.pack(padx= 5,pady=30)

        deactiv_btn = Button(self.middle_frame, text="Deactivate Table", font=('Arial', 9, 'bold'), bg='red', width=20, height=2, 
                    command=lambda: self.deactivate_table(table_number))
        deactiv_btn.pack(padx=2, pady=100)

        checkout_btn = Button(self.checkout_frame, text="Check out",font=('Arial', 14), width=20, height=2, command=lambda: self.checkout(table_number))
        checkout_btn.pack(side = BOTTOM , pady= 10)
    
    def deactivate_table(self, table_num):
        self.display_dormant_table(table_num)
        self.table_status[table_num] = 'dormant'
        self.table_orders.pop(table_num, None)



class OrderManager:
    def __init__(self, menu_manager, table_manager):
        self.menu_manager = menu_manager
        self.table_manager = table_manager
        self.window = menu_manager.window


    def update_order(self, var, item, table_number, add):
        """Helper method to update the order quantity when buttons are pressed."""
        new_value = max(0, var.get() + add)  # Ensures the value never goes negative
        var.set(new_value)
        self.table_orders[table_number][item] = new_value


    def save_order(self, table_number):
        self.order_listbox.delete(0, END)  
        total_cost = 0.0

        for menu_item, qty_var in self.table_vars.items():
            try:
                qty = int(qty_var.get())
                self.table_orders[table_number][menu_item] = qty
                item_cost = self.menu.get(menu_item, 0)
                menu_item_total = qty * item_cost
                total_cost += menu_item_total
            
                if qty > 0:
                    self.order_listbox.insert(END, f"{menu_item} x{qty} - ฿{menu_item_total:.2f}")

            except ValueError:
                self.table_orders[table_number][menu_item] = 0

        self.total_cost_var.set(f"Total: ฿{total_cost:.2f}")


    def delete_order(self, table_number):
        selected_index = self.order_listbox.curselection()  # get the currently selected item's index
        if selected_index:  # Check if something is selected
            selected_item = self.order_listbox.get(selected_index)
            
            menu_name = selected_item.split(" x")[0]

            # Update the table_orders dictionary
            if table_number in self.table_orders and menu_name in self.table_orders[table_number]:
                del self.table_orders[table_number][menu_name]

            self.order_listbox.delete(selected_index)

            total_cost = self.compute_total_cost(table_number)
            self.total_cost_var.set(f"Total: ฿{total_cost:.2f}")


    def compute_total_cost(self, table_number):
        total = 0.0
        for menu_item, qty in self.table_orders[table_number].items():
            item_cost = self.menu.get(menu_item, 0)
            total += item_cost * qty
        return total

    


class Mainui(object):
    def __init__(self, window):
        self.window = window
        img = PhotoImage(file='C:/Users/phatt/Desktop/Code Files/Python/Computer Prgramming (Python)/Projekt/images/Rlogo.png')
        self.window.iconphoto(False, img)
        self.window.title("Restaurant Manager")
        self.window.geometry('1280x720')

        self.tables_frame = Frame(self.window, width=180, height=720, bg="lightgray")
        self.tables_frame.pack(side=LEFT, fill=Y, padx=5, pady=10)


        #Create Middle Frame
        self.middle_frame = Frame(self.window,height=720, bg="gray")
        self.middle_frame.pack_propagate(0)
        self.middle_frame.pack(side=LEFT, fill=BOTH,expand=True, padx=5, pady=10)

        self.menu_manager = MenuManager(self.window, self.middle_frame, self.tables_frame)
        self.table_manager = TableManager(self.menu_manager,self.middle_frame,self.tables_frame)
        self.menu_ui = MenuUI(self.window, self.menu_manager.menu_callbacks)
        self.order_manager = OrderManager(self,self.table_manager)

        self.right_frame = Frame(self.window, width=280,height=720, bg="lightgray")
        self.middle_frame.pack_propagate(0)
        self.right_frame.pack(side= RIGHT, fill=Y, expand=False, padx=5, pady=10)
        self.display_image()
        self.display_time()


    def display_image(self):
        image_path = 'C:/Users/phatt/Desktop/Code Files/Python/Computer Prgramming (Python)/Projekt/images/logo.png'
        original_image = Image.open(image_path)

        desired_width = 250  
        aspect_ratio = original_image.height / original_image.width
        desired_height = int(desired_width * aspect_ratio)
        resized_image = original_image.resize((desired_width, desired_height))

        img = ImageTk.PhotoImage(resized_image)

        img_label = Label(self.right_frame, image=img ,bg= 'lightgray')
        img_label.image = img 
        img_label.grid(row=0, pady=10)

    def display_time(self):        
        self.time_label = Label(self.right_frame, font=('Times', 20, 'bold'), background='purple', foreground='white')
        self.time_label.grid(row=1)
        self.update_time()

    def update_time(self):
        current_time = time.strftime('%H:%M:%S %p')
        self.time_label.config(text=f" Time: {current_time} ")
        self.window.after(1000, self.update_time)


if __name__ == '__main__':
    window = Tk()
    app = Mainui(window)
    window.mainloop()