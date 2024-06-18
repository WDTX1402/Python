from tkinter import*
from tkinter import messagebox, font
from abc import ABC, abstractmethod
from tkinter import filedialog
from promptpay import qrcode
from PIL import Image, ImageTk

import matplotlib.pyplot as plt
import datetime
import os
import json
import pickle

class Prompt:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Menu")
        self.root.geometry("500x150")

        Label(self.root, text="Enter the name of your company to start your day, or click Analysis to enter statistic mode").pack(padx=10, pady=10)
        self.prompt = Entry(self.root, bd=5, width=35)
        self.prompt.pack()
        Button(self.root, text="Submit", command=self.setName, pady=5, padx=5).pack(pady=2, padx=2, side=RIGHT)
        Button(self.root, text="Analysis", command=self.enterAnalyse, pady=5, padx=5).pack(pady=2, padx=2, side=RIGHT)
        Button(self.root, text="Exit", command=self.root.quit, pady=5, padx=5).pack(pady=2, padx=2, side=RIGHT)
        
        self.root.mainloop()

    def enterAnalyse(self):
        self.root.destroy()
        Analysis()
            
    def setName(self):
        self.name = (self.prompt.get())
        try:
            self.root.destroy()
        except:
            self.anaWin.destroy()
        Main(self.name)

class Main:
    
    def __init__(self, name):
        self.mainWin = Tk()
        self.bg = '#f5f5f5'
        self.fg = '#424242'
        self.sec = '#eeeeee'
        self.mainWin.configure(bg=self.bg)
        self.mainWin.state('zoomed')
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Calibri")
        
        self.name = name
        
        self.currentDate = str(datetime.datetime.now().year)+str(datetime.datetime.now().month).zfill(2)+str(datetime.datetime.now().day).zfill(2)
        
        self.qrID = None
        self.taxRate = 1.0
        self.serRate = 1.0
        self.memberList = []
        self.memberOrder = 1
        self.productList = {}
        self.orderList = []
        self.memberVal = {"sil" : 1.0, "gold" : 1.0, "plat" : 1.0}
        self.mainWin.title(f"{self.name} Management System")
        self.mainWin.geometry("1280x720")
        self.loadSettings()
        self.loadMembership()
                
        self.mainMenu()

        self.welPad = Label(self.mainWin, text="\t\t\t\t\t\t\t\t\t", bg=self.bg, fg=self.fg,)
        self.welPad.grid(row=0, column=0, padx=2, pady=2)
        self.displayDate = Label(self.mainWin, text=datetime.date.today().strftime("%d/%m/%Y"), bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).grid(row=0, column=1, padx=2, pady=2, sticky=E)
        self.welFrame = LabelFrame(self.mainWin, text=f"Welcome to {self.name}", bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD))
        self.welFrame.grid(row=1, column=1, padx=2, pady=2, sticky=N)
        
        Label(self.welFrame, text="\n\tClick ""Order"" to start your day\t\t", bg=self.bg, fg=self.fg, font=("Calibri", 15, font.BOLD)).pack(pady=5)
        Label(self.welFrame, text="\tChoose the option in the menu bar for adjustment.\t\t", bg=self.bg, fg=self.fg, font=("Calibri", 15, font.BOLD)).pack(pady=5)
        Button(self.welFrame, text="Order", command=self.orderWin, padx=10, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).pack(pady=25, padx=2, side=RIGHT)
        self.mainWin.mainloop()

    def loadSettings(self):
        if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}\setting.json"):
            with open(f"{os.path.dirname(os.path.abspath(__file__))}\setting.json", 'r') as f:
                settingsLoad = json.loads(f.read())
                self.qrID = settingsLoad["qrID"]
                self.taxRate = settingsLoad["taxRate"]
                self.serRate = settingsLoad["serRate"]
                self.memberVal = settingsLoad["memberVal"]
                self.productList = settingsLoad["productList"]
        else:
            self.updateSettings()
    
    def loadMembership(self):
        if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}\member.pickle"):
            with open(f"{os.path.dirname(os.path.abspath(__file__))}\member.pickle", 'rb') as f:
                self.memberList = pickle.load(f)
                    
                if len(self.memberList) > 0:
                    if self.memberList[-1].id[:8] == self.currentDate:
                        self.memberOrder = int(self.memberList[-1].id[9:]) + 1
        else:
            self.updateSettings()
            
    def updateSettings(self):
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\member.pickle", 'wb') as f:
            pickle.dump(self.memberList, f)
        
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\setting.json", 'w') as f:
            settingInit = {
                "qrID" : self.qrID,
                "taxRate" : self.taxRate,
                "serRate" : self.serRate,
                "memberVal" : self.memberVal,
                "productList" : self.productList
            }
            f.write(json.dumps(settingInit))
    
    def mainMenu(self):
        menubar = Menu(self.mainWin)
        self.mainWin.config(menu=menubar)

        option_menu = Menu(menubar,tearoff=0)
        option_menu.add_command(label='QR Payment settings', command=self.qrPayment)
        option_menu.add_command(label='Product Adjustment', command=self.adjustProduct)
        option_menu.add_command(label='Tax/Service Charge Rate', command=self.tsRate)
        option_menu.add_command(label='Membership', command=self.memberManage)
        option_menu.add_separator()
        option_menu.add_command(label='Exit',command=self.mainWin.destroy)
        menubar.add_cascade(label="Options",menu=option_menu)

        help_menu = Menu(menubar,tearoff=0)
        help_menu.add_command(label='Income Summary', command=lambda:self.incomeSum(f"{os.path.dirname(os.path.abspath(__file__))}\{self.currentDate}.pickle"))
        help_menu.add_command(label='Membership Analysis', command=lambda:self.membershipUsage(f"{os.path.dirname(os.path.abspath(__file__))}\{self.currentDate}.pickle"))
        help_menu.add_command(label='Ordering Statistic', command=lambda:self.preferredDish(f"{os.path.dirname(os.path.abspath(__file__))}\{self.currentDate}.pickle"))
        help_menu.add_command(label='Peak Time Analysis', command=lambda:self.peakTime(f"{os.path.dirname(os.path.abspath(__file__))}\{self.currentDate}.pickle"))
        menubar.add_cascade(label="More...",menu=help_menu)
    
    #QR Payments
    def qrPayment(self):
        self.qrWin = Toplevel(self.mainWin)
        self.qrWin.configure(bg=self.bg)
        self.qrWin.title("QR Payment settings")
        
        Label(self.qrWin, text="Enter your registered id or phone number : ", bg=self.bg, fg=self.fg, font=("Calibri", 12)).pack(padx=5, pady=5)
        self.qrIdE = Entry(self.qrWin, bd=5, width=35)
        self.qrIdE.pack(padx=2, pady=2)
        
        Button(self.qrWin, text="Confirm", command=self.setQR, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).pack(padx=3, pady=3)
    
    def setQR(self):
        self.qrID = self.qrIdE.get()
        self.updateSettings()
        self.qrWin.destroy()

    #Tax/Service Window
    def tsRate(self):
        self.tsRateWin = Toplevel(self.mainWin)
        self.tsRateWin.configure(bg=self.bg)
        self.tsRateWin.title("Tax & Service Charge Rate")

        frame1 = LabelFrame(self.tsRateWin, text="Enter Tax rate in %", padx=10, pady=10, bg=self.bg, fg=self.fg, font=("Calibri", 12))
        frame1.pack(padx=10, pady=10)
        self.taxE = Entry(frame1, bd=5, width=35)
        self.taxE.pack()

        frame2 = LabelFrame(self.tsRateWin, text="Enter Service Charge rate in %", padx=10, pady=10, bg=self.bg, fg=self.fg, font=("Calibri", 12))
        frame2.pack(padx=10, pady=10)
        self.serE = Entry(frame2, bd=5, width=35)
        self.serE.pack()

        Button(self.tsRateWin, text="Submit", command=self.setTSRate, padx=10, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).pack(pady=10, padx=2, side=RIGHT)
        
    def setTSRate(self):
        try:
            if self.taxE.get() == '':
                raise Exception
            self.taxRate = (float(self.taxE.get()) / 100) + 1
        except ValueError as e:
            messagebox.showerror("Invalid Value", "Enter the percentage for tax: \n" + str(e))
        except Exception:
            pass
            
        try:
            if self.serE.get() == '':
                raise Exception
            self.serRate = (float(self.serE.get()) / 100) + 1
        except ValueError as e:
            messagebox.showerror("Invalid Value", "Enter the percentage for service charge: \n" + str(e))
        except Exception:
            pass
            
        self.updateSettings()
        
    
    #Product Window
    def adjustProduct(self):
        self.adjustP = Toplevel(self.mainWin)
        self.adjustP.configure(bg=self.bg)
        self.adjustP.title("Product Adjustment")
        
        Label(self.adjustP, text="Product Adjustment\n", bg=self.bg, fg=self.fg, font=("Calibri", 12)).grid(row=0, column=0)
        
        self.adjPscrollbar = Scrollbar(self.adjustP)
        self.adjPscrollbar.grid(row=1, column=1, sticky=NS)
        self.displayList = Listbox(self.adjustP, yscrollcommand=self.adjPscrollbar.set, height=12)
        self.displayProductListbox()
        
        adjPFrame = LabelFrame(self.adjustP, text="Product Info", padx=10, pady=10, bg=self.bg, fg=self.fg, font=("Calibri", 12))
        adjPFrame.grid(row=1, column=2, padx=3, pady=3, sticky=N)
        Label(adjPFrame, text="Name", bg=self.bg, fg=self.fg, font=("Calibri", 12)).grid(row=3, column=1, sticky=W)
        self.pName = Entry(adjPFrame, bd=5, width=40)
        self.pName.grid(row=4, column=1, columnspan=3)
        Label(adjPFrame, text="Price", bg=self.bg, fg=self.fg, font=("Calibri", 12)).grid(row=5, column=1, sticky=W)
        self.pPrice = Entry(adjPFrame, bd=5, width=40)
        self.pPrice.grid(row=6, column=1, columnspan=3)
        
        self.displayList.bind('<<ListboxSelect>>', self.productInfo)
        Button(adjPFrame, text="Delete", command=self.delProduct, padx=15, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).grid(row=7, column=2, padx=2, pady=5)
        Button(adjPFrame, text="Edit/New", command=self.newProduct, padx=15, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).grid(row=7, column=3, padx=2, pady=5)
    
    def displayProductListbox(self):
        self.displayList = Listbox(self.adjustP, yscrollcommand=self.adjPscrollbar.set, height=12)
        self.displayList.bind('<<ListboxSelect>>', self.productInfo)
        for key, val in self.productList.items():
            self.displayList.insert(END, key)
        self.displayList.grid(row=1, column=0, padx=2, pady=2)
        self.adjPscrollbar.config( command = self.displayList.yview )

    def productInfo(self, event):
        self.pName.delete(0, END)
        self.pName.insert(END, self.displayList.get(ANCHOR))

        self.pPrice.delete(0, END)
        self.pPrice.insert(END, self.productList.get(self.pName.get()))

    def newProduct(self):
        try:
            self.productList.update({self.pName.get() : int(self.pPrice.get())})
            self.displayProductListbox()
            
            self.updateSettings()
        except ValueError as e:
            messagebox.showerror("Invalid Value", "Enter an integer: \n" + str(e))

    def delProduct(self):
        try :
            self.productList.pop(self.pName.get())
            self.displayProductListbox()
            
            self.updateSettings()
        except KeyError as e:
            messagebox.showerror("Invalid Name", "Enter a correct product name:\n" + str(e) + " is not found")
    

    #Membership Window
    def memberManage(self):
        self.memWin = Toplevel(self.mainWin)
        self.memWin.configure(bg=self.bg)
        self.memWin.title("Membership Management")
        self.memWin.geometry("750x400")
        
        regis = LabelFrame(self.memWin, text="Register New Member", bg=self.bg, fg=self.fg, font=("Calibri", 12))
        regis.pack()
        self.registerEntry = Entry(regis, bd=5, width=35)
        self.registerEntry.pack()
        Button(regis, text="Register Silver Member", command=self.registerSilMember, pady=5, padx=10, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).pack(pady=10, padx=2, side=RIGHT)
        Button(regis, text="Register Gold Member", command=self.registerGoldMember, pady=5, padx=10, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).pack(pady=10, padx=2, side=RIGHT)
        Button(regis, text="Register Platinum Member", command=self.registerPlatMember, pady=5, padx=10, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).pack(pady=10, padx=2, side=RIGHT)

        mframe = LabelFrame(self.memWin, bg=self.bg, fg=self.fg, font=("Calibri", 12))
        mframe.pack(side=LEFT)
        frame1 = LabelFrame(mframe, text="Silver Discount Rate %", padx=10, pady=5, bg=self.bg, fg=self.fg, font=("Calibri", 12))
        frame1.pack(padx=10, pady=10, anchor=W)
        self.silDis = Entry(frame1, bd=5, width=35)
        self.silDis.pack()

        frame2 = LabelFrame(mframe, text="Gold Discount Rate %", padx=10, pady=5, bg=self.bg, fg=self.fg, font=("Calibri", 12))
        frame2.pack(padx=10, pady=10, anchor=W)
        self.goldDis = Entry(frame2, bd=5, width=35)
        self.goldDis.pack()

        frame3 = LabelFrame(mframe, text="Platinum Discount Rate %", padx=10, pady=5, bg=self.bg, fg=self.fg, font=("Calibri", 12))
        frame3.pack(padx=10, pady=10, anchor=W)
        self.platDis = Entry(frame3, bd=5, width=35)
        self.platDis.pack()
        Button(mframe, text="Confirm", command=self.setMemRate, padx=10, bg=self.bg, fg=self.fg, font=("Calibri", 10, font.BOLD)).pack(pady=10, padx=2)
        
        self.memListText = Text(self.memWin, width=60, height=17)
        self.memListText.pack(anchor=E, side=RIGHT, padx=3, pady=2)
        
        self.updateMemList()
        
    def updateMemList(self):
        self.memListText.delete('1.0', END)
        self.memListText.insert(END, "\n====================== Members List ======================\n ")
        for i in self.memberList:
            self.memListText.insert(END, f" \n {i.id} \t\t{i.__class__.__name__}")
    
    def registerSilMember(self):
        self.registerEntry.delete(0, END)
        generateNewMem = self.currentDate+str(self.memberOrder).zfill(4)
        self.memberList.append(membershipSilver(generateNewMem, self.memberVal.get("sil")))
        self.registerEntry.insert(END, generateNewMem)
        self.memberOrder += 1
        
        self.updateMemList()
        self.updateSettings()
            
    def registerGoldMember(self):
        self.registerEntry.delete(0, END)
        generateNewMem = self.currentDate+str(self.memberOrder).zfill(4)
        self.memberList.append(membershipGold(generateNewMem, self.memberVal.get("gold")))
        self.registerEntry.insert(END, generateNewMem)
        self.memberOrder += 1
        
        self.updateMemList()
        self.updateSettings()
        
    def registerPlatMember(self):
        self.registerEntry.delete(0, END)
        generateNewMem = self.currentDate+str(self.memberOrder).zfill(4)
        self.memberList.append(membershipPlatinum(generateNewMem, self.memberVal.get("plat")))
        self.registerEntry.insert(END, generateNewMem)
        self.memberOrder += 1
        
        self.updateMemList()
        self.updateSettings()
            
    def setMemRate(self):
        try:
            if self.silDis.get() == '':
                raise Exception
            self.memberVal.update({"sil" : 1.0 - float(self.silDis.get())/100})
        except ValueError as e:
            messagebox.showerror("Invalid Value", "Enter a percentage for silver: \n" + str(e))
        except Exception:
            pass
            
        try:
            if self.goldDis.get() == '':
                raise Exception
            self.memberVal.update({"gold" : 1.0 - float(self.goldDis.get())/100})
        except ValueError as e:
            messagebox.showerror("Invalid Value", "Enter a percentage for gold: \n" + str(e))
        except Exception:
            pass
        
        try:
            if self.platDis.get() == '':
                raise Exception
            self.memberVal.update({"plat" : 1.0 - float(self.platDis.get())/100})
        except ValueError as e:
            messagebox.showerror("Invalid Value", "Enter a percentage for platinum: \n" + str(e))
        except Exception:
            pass
            
        self.updateSettings()


    #Table Window
    def orderWin(self):
        self.welFrame.destroy()
        self.welPad.destroy()
        self.tablePad = Label(self.mainWin, text="\t \t        ", bg=self.bg, fg=self.fg, font=("Calibri", 15))
        self.tablePad.grid(row=0, column=0)
        self.orderWinLabel = Label(self.mainWin, text="Tables Management", bg=self.bg, fg=self.fg, font=("Calibri", 20))
        self.orderWinLabel.grid(row=0, column=1, padx=2, pady=2)
        
        self.tableNo = 1
        try:
            self.loadBill(f"{os.path.dirname(os.path.abspath(__file__))}\{self.currentDate}.pickle")
        except:
            self.orderNo = 1
        self.tableList = []

        try:
            if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}\\tables.pickle"):
                raise Exception
        except:
            self.loadDraw = Button(self.mainWin, text="Load", command=self.loadTablepos, width=80, bg=self.bg, fg=self.fg, font=("Calibri", 20))
            self.loadDraw.grid(row=2, column=1, padx=2, pady=2)
          
        self.recallCanvas()
        self.doneDrawButton = Button(self.mainWin, text="Confirm", command=self.doneDraw, width=80, bg=self.bg, fg=self.fg, font=("Calibri", 20))

    def recallCanvas(self):
        self.orderWinLabel.config(text="Tables Management")
        self.canvasFrame = LabelFrame(self.mainWin)
        self.canvasFrame.grid(row=1, column=1, padx=2, pady=2)
        self.canvas = Canvas(self.canvasFrame, width=1100, height=600, bg=self.bg)
        self.canvas.pack()
        
        if len(self.tableList) == 0:
            self.canvas.bind('<Button-1>', self.draw)
        else:
            for i in self.tableList:
                self.canvas.create_rectangle(i.pos["x"]-40, i.pos["y"]-40, i.pos["x"]+40, i.pos["y"]+40, outline=self.fg, fill=self.sec, width=2)
                self.canvas.create_text(i.pos["x"], i.pos["y"], text="Table " + str(i.number), fill=self.fg, font=("Calibri", 12))
                self.doneDraw()

    def draw(self, click):
        if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}\\tables.pickle"):
            self.loadDraw.destroy()
        self.doneDrawButton.grid(row=3, column=1, padx=2, pady=2)
        
        try:
            for i in self.tableList:
                if (click.x > i.pos.get("x") - 80 and click.x < i.pos.get("x") + 80) and (click.y > i.pos.get("y") - 80 and click.y < i.pos.get("y") + 80):
                    raise Exception
            self.canvas.create_rectangle(click.x-40, click.y-40, click.x+40, click.y+40, outline=self.fg, fill=self.bg, width=2)
            self.tableList.append(tableInfo(self.tableNo, {"x" : click.x, "y" : click.y}))
            self.canvas.create_text(click.x, click.y, text="Table " + str(self.tableNo), fill=self.fg, font=("Calibri", 12))
            self.tableNo += 1
        except:
            pass
            
    def doneDraw(self):
        self.canvas.unbind('<Button-1>')
        self.doneDrawButton.destroy()
        self.saveTablepos()
        
        self.canvas.bind('<Button-1>', self.tableOrder)
    
    def tableOrder(self, click):
        for i in self.tableList:
            if abs(click.x - int(i.pos["x"])) <= 40 and abs(click.y - int(i.pos["y"])) <= 40:
                i.order = self.orderNo
                self.canvasFrame.grid_forget()
                self.orderWinLabel.grid_forget()
                self.orderLabel = Label(self.mainWin, text="Table: " + str(i.number) + "\nOrder: " + str(self.orderNo), bg=self.bg, fg=self.fg, font=("Calibri", 15, font.BOLD))
                self.orderLabel.grid(row=1, column=1, padx=2, pady=2)
                
                self.billDetail = billInfo(self.orderNo, i.pos)
                self.menuDisplay()
                
                self.orderNo += 1

    def saveTablepos(self):
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\\tables.pickle", 'wb') as f:
            pickle.dump(self.tableList, f)

    def loadTablepos(self):
        self.loadDraw.destroy()
        self.canvasFrame.grid_forget()
        
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\\tables.pickle", 'rb') as f:
            self.tableList = pickle.load(f)

        self.recallCanvas()
    
    
    #Order Window
    def menuDisplay(self):
        self.orderDetail = dict()
        
        self.orderFrame = LabelFrame(self.mainWin, bg=self.bg, fg=self.fg)
        self.orderFrame.grid(row=2, column=1, padx=5, pady=5)
        self.orderScrollbar = Scrollbar(self.orderFrame, bg=self.bg)
        self.orderScrollbar.grid(row=2, rowspan=5, column=2, sticky=NS)
        self.displayMenu = Listbox(self.orderScrollbar, yscrollcommand=self.orderScrollbar.set)
        self.displayOrderListbox()
        self.displayMenu.bind('<<ListboxSelect>>', self.updateBillEntry)

        self.orderAmountFrame = LabelFrame(self.orderFrame, text="Amount", font=("Calibri", 13), bg=self.bg, fg=self.fg)
        self.orderAmountFrame.grid(row=2, column=3)
        self.orderAmount = Entry(self.orderAmountFrame, bd=3, width=15, font=15)
        self.orderAmount.pack()
        self.orderBack = Button(self.orderFrame, text="Enter", command=self.updateBill, width=15, height=5, font=("Calibri", 15), bg=self.bg, fg=self.fg)
        self.orderBack.grid(row=3, column=3, padx=2, pady=2, sticky=N)
        
        self.memFrame = LabelFrame(self.orderFrame, text="Membership ID: ", font=("Calibri", 13), bg=self.bg, fg=self.fg)
        self.memFrame.grid(row=4, column=3, padx=2, pady=2)
        self.enterMemID = Entry(self.memFrame, bd=3, width=15, font=15)
        self.enterMemID.pack()
        
        self.qrGenBut = Button(self.orderFrame, text="QR Code Payments", command=self.qrGen, width=15, height=2, font=("Calibri", 10), bg=self.bg, fg=self.fg)
        self.qrGenBut.grid(row=5, column=3, padx=2, pady=2, sticky=N)
        
        self.orderBack = Button(self.orderFrame, text="Confirm", command=self.endBill, width=15, height=5, font=("Calibri", 15), bg=self.bg, fg=self.fg)
        self.orderBack.grid(row=6, column=3, padx=2, pady=2, sticky=N)
        
        self.billHeader = Label(self.orderFrame, text="Order Summary", font=("Calibri", 13), bg=self.bg, fg=self.fg)
        self.billHeader.grid(row=1, column=4)
        self.billDisplay = Text(self.orderFrame, height=35, width=60)
        self.billDisplay.insert(END, " Menu\t\tAmount\t\tPrice\t\tSum\n\n")
        self.billDisplay.grid(row=2, column=4, padx=5, pady=5, rowspan=5)
    
    def qrGen(self):
        try:
            global img
            self.calBill()
            qr = qrcode.generate_payload(self.qrID, self.billDetail.totalpp)
            img = ImageTk.PhotoImage(qrcode.to_image(qr))
            
            qrWin = Toplevel(self.mainWin)
            qrWin.title("QR Code Payment")
            Label(qrWin, text="QR Code Payment", font=("Calibri", 15)).pack()
            Label(qrWin, text=f"Total : {self.billDetail.totalpp}", font=("Calibri", 10)).pack()
            canvas= Canvas(qrWin, width= 430, height= 500)
            canvas.pack()
            canvas.create_image(10,10,anchor=NW,image=img)
        except:
            messagebox.showerror("Promptpay ID Error", "Promptpay ID is currently nulll")
           
    def calBill(self):
        total = 0
        for key, val in self.orderDetail.items():
            total+= int(self.productList.get(key))*val
        self.billDetail.total = total
        
        if self.enterMemID.get() == "":
            self.billDetail.membership = None
            self.billDetail.totalpp = total
            self.billDetail.totalpp *= self.serRate
            self.billDetail.totalpp *= self.taxRate
            self.billDetail.totalpp = round(self.billDetail.totalpp, 2)
        else:
            for i in self.memberList:
                if self.enterMemID.get() == str(i.id):
                    self.billDetail.membership = i.__class__.__name__
                    self.billDetail.totalpp = i.discountDeduction(total)
                    self.billDetail.totalpp *= self.serRate
                    self.billDetail.totalpp *= self.taxRate
                    self.billDetail.totalpp = round(self.billDetail.totalpp, 2)
                    
                    break
                else:
                    self.billDetail.totalpp = total
                    self.billDetail.totalpp *= self.serRate
                    self.billDetail.totalpp *= self.taxRate
                    self.billDetail.totalpp = round(self.billDetail.totalpp, 2)
    
    def endBill(self):
        self.billDetail.time = datetime.datetime.now().strftime('%H:%M:%S')
        self.billDetail.order = self.orderDetail
        
        self.calBill()
        
        self.orderList.append(self.billDetail)
        self.orderFrame.grid_forget()
        
        self.saveBill()
        self.loadBill(f"{os.path.dirname(os.path.abspath(__file__))}\{self.currentDate}.pickle")
        self.orderBack.forget()
        self.recallCanvas()
    
    def displayOrderListbox(self):
        self.displayMenu = Listbox(self.orderFrame, yscrollcommand=self.orderScrollbar.set , height=24, width=35, font=30)
        for key, val in self.productList.items():
            self.displayMenu.insert(END, key)
        self.displayMenu.grid(row=2, column=0, columnspan=2, rowspan=5, sticky=E)
        self.orderScrollbar.config( command = self.displayMenu.yview )  
    
    def updateBillEntry(self, event):
        self.orderAmount.delete(0, END)
        selection = self.displayMenu.curselection()
        try:
            if self.orderDetail.get((self.displayMenu.get(selection))) is None:
                self.orderAmount.insert(END, "")
            else:
                self.orderAmount.insert(END, str(self.orderDetail.get((self.displayMenu.get(selection)))))
        except: 
            pass
    
    def updateBill(self):
        try:
            selection = self.displayMenu.curselection()
            self.orderDetail.update({self.displayMenu.get(selection) : int(self.orderAmount.get())})
            orderText = ""
            
            self.calBill()
            self.billDisplay.delete('1.0', END)
            orderText = " Menu\t\tAmount\t\tPrice\t\tSum\n\n"
            for key, val in self.orderDetail.items():
                orderText += f" {key}\t\t{val}\t\t{int(self.productList.get(key))}\t\t{int(self.productList.get(key))*val}\n"
            orderText += f"\n \t\t\t\t\tTotal :\t{self.billDetail.total}\n \t\t\t\t\tNet   :\t{self.billDetail.totalpp:.2f}"
            self.billDisplay.insert(END, orderText)
        except ValueError as e:
            messagebox.showerror("Invalid Value", "Enter an integer: \n" + str(e))
        except:
            pass

    def saveBill(self):
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\{self.currentDate}.pickle", 'wb') as f:
            pickle.dump(self.orderList, f)
    
    def loadBill(self, file):
        with open(file, 'rb') as f:
            self.orderList = pickle.load(f)
            self.orderNo = self.orderList[-1].number + 1
    
    #Analysis Function
    def incomeSum(self, file):
        try:
            self.loadBill(file)
            self.incomeStat = {"Net Total" : 0.0, "Total" : 0.0}

            for i in self.orderList:
                self.incomeStat["Total"] += i.total
                self.incomeStat["Net Total"] += i.totalpp
                        
            plt.bar(list(self.incomeStat.keys()), list(self.incomeStat.values()))
        
            plt.ylabel("Amount")
            plt.title("Income Summary")
            plt.show()
        except:
            messagebox.showerror("Data Not Found", "Database is empty")
    
    def preferredDish(self, file):
        try:
            self.loadBill(file)
            menu = dict()

            for i in self.orderList:
                for key, val in i.order.items():
                    if key in menu:
                        menu[key] = menu[key] + val
                    else:
                        menu.update({key : val})
            
            for i in self.productList.keys():
                if i not in menu.keys():
                    menu.update({i : 0})
            
            fig, ax = plt.subplots()
            ax.barh(list(menu.keys()), list(menu.values()))
            for s in ['top', 'bottom', 'left', 'right']:ax.spines[s].set_visible(False)
            
            ax.xaxis.set_ticks_position('none')
            ax.yaxis.set_ticks_position('none')
            
            ax.xaxis.set_tick_params(pad = 5)
            ax.yaxis.set_tick_params(pad = 10)
            
            ax.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2)
            ax.invert_yaxis()
            ax.set_title('Number of dishes ordered', loc ='left')
            
            plt.show()
        except Exception as e:
            messagebox.showerror("Error", "Failed to proceed :\n" + str(e))
 
    def peakTime(self, file):
        try:
            self.loadBill(file)
            self.timeStat = dict()
            
            for i in self.orderList:
                if i.time[:2] not in self.timeStat:
                    self.timeStat.update({i.time[:2] : 1})
                else:
                    self.timeStat.update({i.time[:2] : int(self.timeStat.get(i.time[:2])) + 1})
            
            plt.plot(self.timeStat.keys(), self.timeStat.values())
            plt.title('Peak Time Analysis')
            plt.xlabel('Time')
            plt.ylabel('Amount')
            plt.show()
        except:
            messagebox.showerror("Data Not Found", "Database is empty")
    
    def membershipUsage(self, file):
        try:
            self.loadBill(file)
            self.memberStat = {"None" : 0, "Silver" : 0, "Gold" : 0, "Platinum" : 0}
            for i in self.orderList:
                match i.membership:
                    case None:
                        self.memberStat["None"] += 1
                    case 'membershipSilver':
                        self.memberStat["Silver"] += 1
                    case 'membershipGold':
                        self.memberStat["Gold"] += 1
                    case 'membershipPlatinum':
                        self.memberStat["Platinum"] += 1

            fig1, ax1 = plt.subplots()
            ax1.pie(list(self.memberStat.values()), labels=list(self.memberStat.keys()), autopct='%1.1f%%', shadow=True, startangle=90)
            ax1.axis('equal')
            plt.title('Membership Analysis')
            plt.show()
        except:
            messagebox.showerror("Data Not Found", "Database is empty")

class Member(ABC):

    def __init__(self, id):
        self.id = id
    
    @abstractmethod
    def discountDeduction(self, total):
        pass

class membershipSilver(Member):

    def __init__(self, id, discount):
        super().__init__(id)
        self.discount = discount

    def discountDeduction(self, total):
        return self.discount*total

class membershipGold(Member):

    def __init__(self, id, discount):
        super().__init__(id)
        self.discount = discount

    def discountDeduction(self, total):
        return self.discount*total
    
class membershipPlatinum(Member):

    def __init__(self, id, discount):
        super().__init__(id)
        self.discount = discount

    def discountDeduction(self, total):
        return self.discount*total
    
class tableInfo:
    
    def __init__(self, number, pos):
        self.number = number
        self.pos = pos

class billInfo(tableInfo):

    def __init__(self, number, pos):
        super().__init__(number, pos)
        self.order = None
        self.membership = None
        self.time = ""
        self.total = 0
        self.totalpp = 0

class Analysis(Main, Prompt):
    
    def __init__(self):
        self.anaWin = Tk()
        self.anaWin.title("Statistical Menu")
        self.anaWin.geometry("400x400")
        
        try:
            self.loadSettings()
        except:
            messagebox.showerror("Data Not Found", "Database undetected")
        
        self.currentData = Label(self.anaWin, text="Current data: None", font=("Calibri", 12, font.BOLD))
        self.currentData.pack()
        
        self.open = Button(self.anaWin, text="Open", command=self.openFile, font=("Calibri", 10, font.BOLD))
        self.open.pack(padx=10, pady=10)
        self.incomeSumBut = Button(self.anaWin, text="Income Summary", command=lambda:self.incomeSum(self.filename), state=DISABLED, font=("Calibri", 10), padx=35, pady=2)
        self.incomeSumBut.pack(padx=10, pady=5)
        self.preferredDishBut = Button(self.anaWin, text="Ordering Statistic", command=lambda:self.preferredDish(self.filename), state=DISABLED, font=("Calibri", 10), padx=35, pady=2)
        self.preferredDishBut.pack(padx=10, pady=5)
        self.peakTimeBut = Button(self.anaWin, text="Peak-Time Analysis", command=lambda:self.peakTime(self.filename), state=DISABLED, font=("Calibri", 10), padx=30, pady=2)
        self.peakTimeBut.pack(padx=10, pady=5)
        self.membershipUsageBut = Button(self.anaWin, text="Membership Usage Statistic", command=lambda:self.membershipUsage(self.filename), state=DISABLED, font=("Calibri", 10), padx=8, pady=2)
        self.membershipUsageBut.pack(padx=10, pady=5)
        
        Label(self.anaWin, text="Enter the name of your company to enter Management Mode.", font=("Calibri", 10),).pack(padx=10, pady=10)
        self.prompt = Entry(self.anaWin, bd=5, width=35)
        self.prompt.pack()
        Button(self.anaWin, text="Management Mode", command=self.setName, font=("Calibri", 10), padx=8, pady=2).pack(padx=10, pady=5)
        Button(self.anaWin, text="Exit", command=self.anaWin.destroy, font=("Calibri", 10), padx=8, pady=2).pack(padx=10, pady=5)
        
        self.anaWin.mainloop()

    def openFile(self):
        try:
            self.filename = filedialog.askopenfilename(initialdir = f"{os.path.dirname(os.path.abspath(__file__))}",title = "Select a File",filetypes = (("pickle files","*.pickle*"),("all files","*.*")))
            self.loadBill(self.filename)
            self.currentData.config(text=f"Current data: {self.filename[-15:]}")
            
            self.incomeSumBut.config(state='normal')
            self.preferredDishBut.config(state='normal')
            self.membershipUsageBut.config(state='normal')
            self.peakTimeBut.config(state='normal')
        except:
            messagebox.showerror("Data Not Found", "Invalid file chosen")    

Prompt()