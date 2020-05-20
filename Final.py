from tkinter import *   
import mysql.connector
import tkinter.messagebox
from tkinter import ttk
import tkinter.scrolledtext as scrolledtext
from PIL import ImageTk,Image
from datetime import date
import datetime
import os
import random

mydb=mysql.connector.connect(host="localhost",user="root",passwd="password",database="Pharmacy")
c=mydb.cursor()

#for dealer and purchase
c.execute("SELECT MAX(D_ID) from dealer")
for r in c:
    id=r[0]

#for sales
d=datetime.datetime.now()
dat=datetime.datetime.now().date()

prod_list=[]
prod_price=[]
prod_quan=[]
prod_dic={}

inq=[]
bc=[]

#for inventory

class Login_window:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.master.title("LOGIN WINDOW")
        self.master.geometry("1366x768+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        #background image
        self.bgImage=ImageTk.PhotoImage(file="C:/Users/akaas/Desktop/Project/bg4.jpeg")#insert bg4 here
        self.img=Label(master, image=self.bgImage)
        self.img.place(x=0,y=0,relwidth=1, relheight=1)

        #get all images
        self.user_icon=PhotoImage(file="C:/Users/akaas/Desktop/Project/user1.png")#insert user1 here
        self.password_icon=PhotoImage(file="C:/Users/akaas/Desktop/Project/password1.png")#insert password1 here
        self.login_icon=PhotoImage(file="C:/Users/akaas/Desktop/Project/login5.png")#insert login5 here


        Login_frame=Frame(master,bg="white")
        Login_frame.place(x=215,y=250)

        self.logolb=Label(Login_frame,image=self.login_icon)
        self.logolb.grid(row=0,columnspan=2,pady=20)

        self.userli=Label(Login_frame,text="Username",image=self.user_icon,compound=LEFT, font=('arial 13 bold'),bg="white").grid(row=1,column=0,padx=20,pady=10)
        self.passwordli = Label(Login_frame, text="Password", image=self.password_icon, compound=LEFT, font=('arial 13 bold'),bg="white").grid(row=2, column=0, padx=20, pady=10)

        self.txtuser = Entry(Login_frame, bd=5,relief=GROOVE, font=('arial 13 bold'))
        self.txtuser.grid(row=1,column=1,padx=20,pady=10)
        self.txtuser.focus()
        
        self.txtpassword = Entry(Login_frame, bd=5,relief=GROOVE, font=('arial 13 bold'),show='*')
        self.txtpassword.grid(row=2,column=1,padx=20,pady=10)


        self.btn_login= Button(Login_frame, text="Login", font=('arail 13 bold'), width=10, height=1, bg="firebrick3",fg='white',command=self.login_sys)
        self.btn_login.grid(row=3,column=1,pady=15)
        self.master.bind("<Return>",self.login_sys)
        
        self.btn_clr = Button(Login_frame, text="Reset", font=('arail 13 bold'), width=10, height=1, bg="firebrick3",fg='white',command=self.clear_all)
        self.btn_clr.place(x=60,y=292)

    def clear_all(self, *args, **kwargs):
        self.txtuser.delete(0, END)
        self.txtpassword.delete(0, END)

    def login_sys(self, *args, **kwargs):
        user=(self.txtuser.get())
        pas=(self.txtpassword.get())

        if(user==str("ABC")) and (pas==str(1234)):
            root.deiconify()
            top.destroy()
        else:
            tkinter.messagebox.showinfo("Error", "Invalid Username/Password")
            self.txtpassword.focus()

class Main_menu:
    def __init__(self, master):
        self.master = master
        self.master.title("PMS")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master)
        self.frame.pack()


        #background image
        self.bgImage=PhotoImage(file="C:/Users/akaas/Desktop/Project/bg.png")
        self.img=Label(master,image=self.bgImage)
        self.img.place(x=0,y=0,relwidth=1, relheight=1)

        self.btn_prc = Button(master, text="Purchase", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white',command=self.new_window_purchase)
        self.btn_prc.place(x=270, y=260)

        self.btn_sls = Button(master, text="Sales", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white',command=self.new_window_sales)
        self.btn_sls.place(x=270, y=330)

        self.btn_dlr = Button(master, text="Dealers", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white', command=self.new_window_dealer)
        self.btn_dlr.place(x=270, y=400)

        self.btn_invn = Button(master, text="Inventory", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white',command=self.new_window_inventory)
        self.btn_invn.place(x=270, y=470)

        self.btn_expinvn = Button(master, text="Expired inventory", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white',command=self.new_window_expiredinventory)
        self.btn_expinvn.place(x=270, y=540)


    def new_window_dealer(self):
        self.newWindow=Toplevel(self.master)        
        self.application=dealer(self.newWindow)

    def new_window_purchase(self):
        self.newWindow=Toplevel(self.master)
        self.application=purchase(self.newWindow)

    def new_window_sales(self):
        self.newWindow=Toplevel(self.master)
        self.application=sales(self.newWindow)

    def new_window_inventory(self):
        self.newWindow=Toplevel(self.master)
        self.application=inventory(self.newWindow)

    def new_window_expiredinventory(self):
        self.newWindow=Toplevel(self.master)
        self.application=expired_inventory(self.newWindow)




class dealer:
    def __init__(self, master):
        self.master = master
        self.master.title("Dealer")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.heading = Label(master, text="DEALERS", font=('arial 40 bold'), fg='steelblue', bg='powder blue')
        self.heading.place(x=600, y=0)

        # labels and entries for the window
        self.dname_1 = Label(master, text="Enter Dealer's name", font=('arial 18 bold'), bg='powder blue')
        self.dname_1.place(x=0, y=100)

        self.D_ID_1 = Label(master, text="Enter Dealer's ID", font=('arial 18 bold'), bg='powder blue')
        self.D_ID_1.place(x=0, y=150)

        self.D_phno_1 = Label(master, text="Enter Dealer's phone number", font=('arial 18 bold'), bg='powder blue')
        self.D_phno_1.place(x=0, y=200)

        self.D_add_1 = Label(master, text="Enter Dealer's address", font=('arial 18 bold'), bg='powder blue')
        self.D_add_1.place(x=0, y=250)

        # entry boxes for labels
        self.Dname_e = Entry(master, width=30, font=('arial 18 bold'))
        self.Dname_e.place(x=360, y=100)

        self.D_ID_e = Entry(master, width=30, font=('arial 18 bold'))
        self.D_ID_e.place(x=360, y=150)

        self.D_phno_e = Entry(master, width=30, font=('arial 18 bold'))
        self.D_phno_e.place(x=360, y=200)

        self.D_add_e = Entry(master, width=30, font=('arial 18 bold'))
        self.D_add_e.place(x=360, y=250)

        # button to search by name
        self.btn_D_srcname = Button(master, text="Search", font=('arail 13 bold'), width=10, height=1, bg="steelblue",fg='white', command=self.search_name)
        self.btn_D_srcname.place(x=1220, y=60)

        # button to clear
        self.btn_clear = Button(master, text="Clear all fields", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white', command=self.clear_all)
        self.btn_clear.place(x=360, y=300)

        # button to add to dealer list
        self.btn_D_addtolist = Button(master, text="Add to list", font=('arail 13 bold'), width=18, height=2,bg="steelblue", fg='white', command=self.add_dealer)
        self.btn_D_addtolist.place(x=562, y=300)

        # button to show all dealers
        self.btn_D_list = Button(master, text="View list of dealers", font=('arail 13 bold'), width=18, height=2,bg="steelblue", fg='white', command=self.dealer_list)
        self.btn_D_list.place(x=532, y=500)

        # adding textbox
        self.tBox = scrolledtext.ScrolledText(master, width=70, height=40)
        self.tBox.place(x=770, y=100)

        # function to clear entry boxes

    def clear_all(self, *args, **kwargs):
        self.Dname_e.delete(0, END)
        self.D_ID_e.delete(0, END)
        self.D_phno_e.delete(0, END)
        self.D_add_e.delete(0, END)

        # function for displaying dealer list

    def dealer_list(self, *args, **kwargs):
        win = Tk()
        frm = Frame(win)
        win.title("LIST OF DEALERS")

        frm.pack(side=tkinter.LEFT, padx=10)
        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4), show="headings", height=25)
        tv.pack()
        tv.heading(1, text="DEALER'S ID")
        tv.column(1, minwidth=0, width=150)
        tv.heading(2, text="DEALER'S NAME")
        tv.column(2, minwidth=0, width=150)
        tv.heading(3, text="DEALER'S PHNO.")
        tv.column(3, minwidth=0, width=150)
        tv.heading(4, text="DEALER'S ADDRESS")
        tv.column(4, minwidth=0, width=150)
        sql = "SELECT* FROM dealer"
        c.execute(sql)
        rows = c.fetchall()
        for x in rows:
            tv.insert('', 'end', values=(x[0], x[1], x[2], x[3]))

    # function to add new dealer
    def add_dealer(self, *args, **kwargs):
        # get from entry box
        self.Dname = self.Dname_e.get()
        self.D_ID = self.D_ID_e.get()
        self.D_phno = self.D_phno_e.get()
        self.D_add = self.D_add_e.get()

        if (self.Dname == '' or self.D_phno == '' or self.D_add == ''):
            tkinter.messagebox.showinfo("Error", "Please fill all entries",parent=self.master)
            self.Dname_e.focus()

        else:
            q = "SELECT* FROM dealer WHERE D_name=%s AND D_phno=%s AND D_add=%s"  # start of comment
            c.execute(q, (self.Dname, self.D_phno, self.D_add))

            data = "error"
            for i in c:
                data = i
            if (data == "error"):
                q = """INSERT INTO dealer(D_name,D_phno,D_add) VALUES(%s,%s,%s)"""
                c.execute(q, (self.Dname, self.D_phno, self.D_add))
                mydb.commit()
                tkinter.messagebox.showinfo("Success", "New Dealer added",parent=self.master)
                self.Dname_e.focus()


            else:
                tkinter.messagebox.showinfo("ERROR", "Dealer already in database",parent=self.master)
                self.Dname_e.focus()

        # search dealer by name

    def search_name(self, *args, **kwargs):
        self.tBox.config(state="normal")
        self.tBox.delete(1.0, END)
        self.Dname = self.Dname_e.get()
        self.D_ID = self.D_ID_e.get()
        self.D_phno = self.D_phno_e.get()
        self.D_add = self.D_add_e.get()
        sql = "SELECT* FROM dealer WHERE D_name=%s OR D_ID=%s OR D_phno=%s OR D_add=%s"
        c.execute(sql, (self.Dname, self.D_ID, self.D_phno, self.D_add))
        rows = c.fetchall()
        self.tBox.insert(END, "  DEALER ID  |   DEALER NAME   | DEALER PHONE NO | DEALER ADDRESS \n")
        for x in rows:
            fx1 = str(x[0])
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            self.tBox.insert(END, (
                        "   " + fx1 + " " * (10 - len(fx1)) + "| " + fx2 + " " * (16 - len(fx2)) + "| " + fx3 + " " * (
                            16 - len(fx3)) + "| " + fx4))
            self.tBox.insert(END, "\n")
        self.tBox.config(state="disabled")


class purchase:
    def __init__(self, master):
        self.master = master
        self.master.title("Purchase")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()


        self.heading = Label(master, text="PURCHASE", font=('arial 40 bold'), fg='steelblue',bg='powder blue')
        self.heading.place(x=500, y=0)

        # labels and entries for window
        self.name_1 = Label(master, text="Enter product name", font=('arial 18 bold'),bg='powder blue')
        self.name_1.place(x=0, y=100)

        self.prod_ID_1 = Label(master, text="Enter product ID", font=('arial 18 bold'),bg='powder blue')
        self.prod_ID_1.place(x=0, y=150)

        self.qty_1 = Label(master, text="Enter quantity", font=('arial 18 bold'),bg='powder blue')
        self.qty_1.place(x=0, y=200)

        self.D_ID_1 = Label(master, text="Enter Dealer ID", font=('arial 18 bold'),bg='powder blue')
        self.D_ID_1.place(x=0, y=250)

        self.D_name_1 = Label(master, text="Enter Dealer name", font=('arial 18 bold'),bg='powder blue')
        self.D_name_1.place(x=0, y=300)

        self.CP_1 = Label(master, text="Enter cost price per unit", font=('arial 18 bold'),bg='powder blue')
        self.CP_1.place(x=0, y=350)

        self.DOE_1 = Label(master, text="Date of expiry", font=('arial 18 bold'),bg='powder blue')
        self.DOE_1.place(x=0, y=400)

        self.DOP_1 = Label(master, text="Date of purchase", font=('arial 18 bold'),bg='powder blue')
        self.DOP_1.place(x=0, y=450)

        # entry box for labels
        self.name_e = Entry(master, width=30, font=('arial 18 bold'))
        self.name_e.place(x=330, y=100)

        self.prod_ID_e = Entry(master, width=30, font=('arial 18 bold'))
        self.prod_ID_e.place(x=330, y=150)

        self.qty_e = Entry(master, width=30, font=('arial 18 bold'))
        self.qty_e.place(x=330, y=200)

        self.D_ID_e = Entry(master, width=21, font=('arial 18 bold'))
        self.D_ID_e.place(x=330, y=250)

        self.D_name_e = Entry(master, width=30, font=('arial 18 bold'))
        self.D_name_e.place(x=330, y=300)

        self.CP_e = Entry(master, width=30, font=('arial 18 bold'))
        self.CP_e.place(x=330, y=350)

        self.DOE_e = Entry(master, width=30, font=('arial 18 bold'))
        self.DOE_e.place(x=330, y=400)

        self.DOP_e = Entry(master, width=30, font=('arial 18 bold'))
        self.DOP_e.place(x=330, y=450)

        # button to add
        self.btn_add = Button(master, text="Add to inventory", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white', command=self.get_items)
        self.btn_add.place(x=532, y=500)

        # button to clear
        self.btn_clear = Button(master, text="Clear all fields", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white', command=self.clear_all)
        self.btn_clear.place(x=330, y=500)

        # button to show purchase history
        self.btn_p_history = Button(master, text="View purchase history", font=('arail 13 bold'), width=18, height=2,bg="steelblue", fg='white', command=self.purc_history)
        self.btn_p_history.place(x=532, y=700)

        # button for searcing dealer ID
        self.btn_D_ID = Button(master, text="Search", font=('arail 13 bold'), width=10, height=1, bg="steelblue",fg='white', command=self.search_dealer)
        self.btn_D_ID.place(x=616, y=250)

        # add text box
        self.tBox = scrolledtext.ScrolledText(master, width=70, height=40)
        self.tBox.place(x=770, y=100)
        
        # scroll=Scrollbar(self,command=self.tBox.yview)
        # scroll.place(x=840,y=71,sticky="nsew")
        # self.tBox['yscrollcommand']=scroll.set

        self.tBox.insert(END, "You have " + str(id) + " dealers\n\n")

        sql = "SELECT* FROM dealer"
        c.execute(sql)
        rows = c.fetchall()
        self.tBox.insert(END, "  DEALER ID  |   DEALER NAME   | DEALER PHONE NO | DEALER ADDRESS \n")
        for x in rows:
            fx1 = str(x[0])
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            self.tBox.insert(END, (
                        "   " + fx1 + " " * (10 - len(fx1)) + "| " + fx2 + " " * (16 - len(fx2)) + "| " + fx3 + " " * (
                            16 - len(fx3)) + "| " + fx4))
            self.tBox.insert(END, "\n")
        self.tBox.config(state="disabled")

    def get_items(self, *args, **kwargs):
        # get from entry box
        self.name = self.name_e.get()
        self.qty = self.qty_e.get()
        self.prod_ID = self.prod_ID_e.get()
        self.D_ID = self.D_ID_e.get()
        self.D_name = self.D_name_e.get()
        self.CP = self.CP_e.get()
        self.DOE = self.DOE_e.get()
        self.DOP = self.DOP_e.get()

        if (self.name == '' or self.qty == '' or self.prod_ID == '' or self.D_ID == '' or self.D_name == '' or self.CP == '' or self.DOE == '' or self.DOP == ''):
            tkinter.messagebox.showinfo("Error", "Please fill all entries",parent=self.master)
            self.name_e.focus()
        else:
            print("GG")
            q = "SELECT* FROM inventory WHERE Prod_name=%s AND DOE=%s"  # start of comment
            c.execute(q, (self.name, self.DOE))
            data = "error"
            for i in c:
                data = i
            if (data == "error"):
                print("DNE")
                self.SP = float(self.CP) * 1.1
                q = """INSERT INTO inventory(Prod_name,DOE,Prod_ID,Qty,CostPrice,SellingPrice) VALUES(%s,%s,%s,%s,%s,%s)"""
                c.execute(q, (self.name, self.DOE, self.prod_ID, self.qty, self.CP, self.SP))
            else:
                print("present")  # end of comment
                ini = "SELECT* FROM inventory WHERE Prod_name=%s AND DOE=%s"
                c.execute(ini, (self.name, self.DOE))
                for r in c:
                    self.old_qty = r[3]
                    self.new_qty = int(self.old_qty) + int(self.qty)
                    sql = "UPDATE inventory SET Qty=%s WHERE Prod_name=%s AND DOE=%s"
                    c.execute(sql, (self.new_qty, self.name, self.DOE))

            # REMOVE DEALER INSERTION ONCE DEALER WINDOW HAS BEEN MADE
            # d="""INSERT INTO DEALER(D_name,D_phno,D_add) VALUES(%s,%s,%s)"""
            # c.execute(d,('ABC','8291701407','Mumbai'))
            sql = """INSERT INTO purchase(Prod_name,Prod_ID,D_ID,D_NAME,Qty,CostPrice,DOE,DOP) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
            c.execute(sql, (self.name, self.prod_ID, self.D_ID, self.D_name, self.qty, self.CP, self.DOE, self.DOP))
            mydb.commit()
            tkinter.messagebox.showinfo("Success", "Successfully added to inventory",parent=self.master)
            self.name_e.focus()
        self.name_e.focus()

        # function for clear entries button

    def clear_all(self, *args, **kwargs):
        # num=id+1
        self.name_e.delete(0, END)
        self.qty_e.delete(0, END)
        self.CP_e.delete(0, END)
        self.prod_ID_e.delete(0, END)
        self.D_name_e.delete(0, END)
        self.D_ID_e.delete(0, END)
        self.DOP_e.delete(0, END)
        self.DOE_e.delete(0, END)

        # function for purchase history button

    def purc_history(self, *args, **kwargs):
        win = Tk()
        frm = Frame(win)
        win.title("PURCHASE HISTORY")

        frm.pack(side=tkinter.LEFT, padx=10)
        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=25)
        tv.pack()
        tv.heading(1, text="Purchase ID")
        tv.column(1, minwidth=0, width=150)
        tv.heading(2, text="Product Name")
        tv.column(2, minwidth=0, width=150)
        tv.heading(3, text="Quantity")
        tv.column(3, minwidth=0, width=150)
        tv.heading(4, text="Dealer Name")
        tv.column(4, minwidth=0, width=150)
        tv.heading(5, text="Dealer ID")
        tv.column(5, minwidth=0, width=150)
        tv.heading(6, text="Cost Price")
        tv.column(6, minwidth=0, width=150)
        tv.heading(7, text="Date Of Expiry")
        tv.column(7, minwidth=0, width=150)
        tv.heading(8, text="Date Of Purchase")
        tv.column(8, minwidth=0, width=150)
        sql = "SELECT P_ID,Prod_name,Qty,D_name,D_ID,CostPrice,DOE,DOP FROM purchase"
        c.execute(sql)
        rows = c.fetchall()
        for x in rows:
            tv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))

        # function to search dealer

    def search_dealer(self, *args, **kwargs):
        self.tBox.config(state="normal")
        self.tBox.delete(1.0, END)
        self.Dname = self.D_name_e.get()
        self.D_ID = self.D_ID_e.get()
        if(self.Dname=='' and self.D_ID==''):
            sql = "SELECT* FROM dealer"
            c.execute(sql)
        else:
            sql = "SELECT* FROM dealer WHERE D_name=%s OR D_ID=%s"
            c.execute(sql, (self.Dname, self.D_ID))
        rows = c.fetchall()
        self.tBox.insert(END, "  DEALER ID  |   DEALER NAME   | DEALER PHONE NO | DEALER ADDRESS \n")
        for x in rows:
            fx1 = str(x[0])
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            self.tBox.insert(END, (
                        "   " + fx1 + " " * (10 - len(fx1)) + "| " + fx2 + " " * (16 - len(fx2)) + "| " + fx3 + " " * (
                            16 - len(fx3)) + "| " + fx4))
            self.tBox.insert(END, "\n")
        self.tBox.config(state="disabled")



class sales:
    def __init__(self, master):
        self.master = master
        self.master.title("Sales")
        self.master.geometry("1366x768+0+0"


        #suraj's code
        self.left = Frame(master, width=800, bg='white', height=768)
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=566, bg='lightblue', height=768)
        self.right.pack(side=LEFT)

        self.header = Label(self.left, text="SALES", font=('arial 40 bold'), bg='white',fg='steelblue')
        self.header.place(x=250, y=0)

        self.date = Label(self.right, text=str(d.strftime("%A")) + "," + str(d.strftime("%B")) + " " + str(d.strftime("%d")) + " " + str(d.strftime("%Y")), font=('arial 12 bold'), bg='lightblue')
        self.date.place(x=200, y=0)

        self.time = Label(self.right, text=str(d.strftime("%X")) + " " + str(d.strftime("%p")), font=('arial 12 bold'),bg='lightblue')
        self.time.place(x=240, y=20)

        self.cart = Label(self.right, text="Preview", font=('arial 27 bold'), bg='lightblue', fg='red')
        self.cart.place(x=0, y=50)

        self.Product = Label(self.right, text="Product", font=('arial 18 bold'), bg='lightblue')
        self.Product.place(x=0, y=110)

        self.Qty = Label(self.right, text="Quantity", font=('arial 18 bold'), bg='lightblue')
        self.Qty.place(x=250, y=110)

        self.Amt = Label(self.right, text="Amount", font=('arial 18 bold'), bg='lightblue')
        self.Amt.place(x=450, y=110)

        self.name = Label(self.left, text="Medicine's Name", font=('arial 18 bold'), bg='white')
        self.name.place(x=0, y=100)

        self.entern = Entry(self.left, width=25, font=('arial 18 italic bold'), bg='lightyellow')
        self.entern.place(x=200, y=100)
        self.entern.focus()

        self.search = Button(self.left, text="Search", width=25, height=2, bg='orange', activebackground='purple',command=self.data)
        self.search.place(x=345, y=150)

        self.price = Label(self.left, text="", font=('arial 27 bold'), bg='white', fg='green')
        self.price.place(x=0, y=200)

        self.totalp = Label(self.right, text="", font=('arial 27 bold'), bg='lightblue', fg='blue')
        self.totalp.place(x=0, y=600)

        c.execute("SELECT Qty from inventory")
        Inv = c.fetchall()
        for i in Inv:
            inq.append(i[0])

    def data(self, *args):

        self.get_n = self.entern.get()
        if self.get_n == "":
            tkinter.messagebox.showwarning("Insert Status", "Medicine Name not entered!!",parent=self.master)
        else:
            c.execute("SELECT SellingPrice,Qty,DOE from Inventory where Prod_name=%s order by DOE", (self.get_n,))
            y = c.fetchall()
            self.aprice = []
            self.doex = []
            for i in y:
                self.aprice.append(i[1])
                self.doex.append(i[2])
            self.stock = sum(self.aprice)
            for i in y:
                if i[0] != None and i[1] != None and i[2] != None:
                    self.p = i[0]
                    self.price.configure(text="Price is ₹ " + str(self.p))

                    self.q = Label(self.left, text="Enter Quantity", font=('arial 18 bold'), bg='white')
                    self.q.place(x=0, y=300)

                    self.enterq = Entry(self.left, width=25, font=('arial 18 italic bold'), bg='lightyellow')
                    self.enterq.place(x=200, y=300)
                    self.enterq.focus()

                    self.add = Button(self.left, text="Add to Cart", width=25, height=2, bg='orange',activebackground='purple', command=self.add_cart)
                    self.add.place(x=345, y=350)

                    self.paid = Label(self.left, text="Amount Paid", font=('arial 18 bold'), bg='white')
                    self.paid.place(x=0, y=420)

                    self.enterp = Entry(self.left, width=25, font=('arial 18 italic bold'), bg='lightyellow')
                    self.enterp.place(x=200, y=420)

                    self.change = Button(self.left, text="Calculate Change", width=25, height=2, bg='orange',activebackground='purple', command=self.change_fun)
                    self.change.place(x=345, y=470)

                    tkinter.messagebox.showinfo("Inventory Status", "Stock available is %s." % self.stock,parent=self.master)
                    break

            if y == []:
                tkinter.messagebox.showerror("Sorry", "%s is not available at the Moment!!" % self.get_n,parent=self.master)
                self.entern.focus()
                self.entern.delete(0, END)

    def add_cart(self, *args):
        self.quan = int(self.enterq.get())
        if self.quan > int(self.stock):
            tkinter.messagebox.showerror("Error", "Stock available is only %s!!\nPlease enter correct amount" % self.stock,parent=self.master)
            self.enterq.delete(0, END)
            self.enterq.focus()
        else:
            self.final = float(self.quan) * float(self.p)
            flag = 1
            for i in range(len(prod_list)):
                if prod_list[i] == self.get_n:
                    prod_quan[i] += self.quan
                    prod_price[i] += self.final
                    flag = 0
                    break
            if flag == 1:
                prod_list.append(self.get_n)
                prod_quan.append(self.quan)
                prod_price.append(self.final)

            self.x_index = 0
            self.y_index = 150
            self.count = 0
            for self.i in prod_list:
                self.tempn = Label(self.right, text=str(prod_list[self.count]), font=('arial 18 bold'), bg='lightblue')
                self.tempn.place(x=0, y=self.y_index)

                self.tempq = Label(self.right, text=str(prod_quan[self.count]), font=('arial 18 bold'), bg='lightblue')
                self.tempq.place(x=250, y=self.y_index)

                self.tempp = Label(self.right, text=str(prod_price[self.count]) + '0', font=('arial 18 bold'),bg='lightblue')
                self.tempp.place(x=450, y=self.y_index)

                self.y_index += 40
                self.count += 1

                self.totalp.configure(text="Total : ₹ " + str(sum(prod_price)) + '0')

                self.q.place_forget()
                self.enterq.place_forget()
                self.price.configure(text="")
                self.add.destroy()

                self.entern.focus()
                self.entern.delete(0, END)
            tkinter.messagebox.showinfo("Success", "Added to your Cart",parent=self.master)

            if self.get_n not in prod_dic.keys():
                prod_dic[self.get_n] = self.aprice
            co = 0
            for i in range(len(self.aprice)):
                co += 1
                if self.quan >= self.aprice[i]:
                    self.quan -= self.aprice[i]
                    self.aprice[i] = 0
                else:
                    self.aprice[i] -= self.quan
                    break
            prod_dic[self.get_n] = self.aprice

            for x in range(co):
                c.execute("UPDATE inventory SET Qty=%s WHERE Prod_name=%s and DOE=%s",
                          (prod_dic[self.get_n][x], self.get_n, self.doex[x]))
                mydb.commit()

    def change_fun(self, *args):
        self.amount = float(self.enterp.get())

        self.ototal = float(sum(prod_price))
        self.bal = self.amount - self.ototal

        if self.bal < 0:
            tkinter.messagebox.showerror("Error", "Enter Right Amount to avoid cancellation of Bill",parent=self.master)
            self.enterp.focus()
            self.enterp.delete(0, END)

        else:

            self.name.place_forget()
            self.entern.place_forget()
            self.search.destroy()

            self.change.configure(state='disabled')

            self.na = Label(self.left, text="Customer's Details", font=('arial 18 bold'), bg='white')
            self.na.place(y=100)

            self.fn = Label(self.left, text="First Name", font=('arial 18 bold'), bg='white')
            self.fn.place(y=150)
            self.fn.focus()

            self.fne = Entry(self.left, font=('arial 18 bold italic'), bg='lightyellow', width=25)
            self.fne.place(x=250, y=150)

            self.ln = Label(self.left, text="Last Name", font=('arial 18 bold'), bg='white')
            self.ln.place(y=200)

            self.lne = Entry(self.left, font=('arial 18 bold italic'), bg='light yellow', width=25)
            self.lne.place(x=250, y=200)

            self.n = Button(self.left, text="Store Name", width=25, height=2, bg='orange', activebackground='purple',command=self.names)
            self.n.place(x=295, y=250)

            self.t_bal = Label(self.left, text="Balance: ₹ " + str(self.bal) + '0', font=('arial 30 bold'), fg='green',bg='white')
            self.t_bal.place(y=340)

            self.fn = []
            self.fq = []
            self.fd = []
            self.sp = []

            c.execute("SELECT Prod_name,Qty,DOE,SellingPrice from Inventory")
            w = c.fetchall()
            for i in w:
                self.fn.append(i[0])
                self.fq.append(i[1])
                self.fd.append(i[2])
                self.sp.append(i[3])

            global bc
            bc = [0 for i in range(len(self.fn))]
            for i in range(len(self.fq)):
                bc[i] = inq[i] - self.fq[i]

    def names(self, *args):

        self.fns = str(self.fne.get())
        self.lns = str(self.lne.get())

        self.bill = Button(self.left, text="Generate Bill", width=90, height=2, bg='red', activebackground='blue',command=self.generate_bill)
        self.bill.place(x=70, y=600)
        self.bill.focus()

        self.n.configure(state='disabled')

    def generate_bill(self, *args):

        global bc
        for i in range(len(inq)):
            if bc[i] == 0:
                continue
            else:
                sq = (
                    "INSERT INTO SALES(S_date,Cust_Fname,Cust_Lname,Prod_name,Qty,U_price,T_price,DOE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
                c.execute(sq, (dat, self.fns, self.lns, self.fn[i], bc[i], self.sp[i], bc[i] * self.sp[i], self.fd[i]))
                mydb.commit()

        tkinter.messagebox.showinfo("Success", "Your Bill is being generated!!",parent=self.master)
        self.bill.configure(state='disabled')

        c.execute("DELETE FROM inventory where Qty=0")
        mydb.commit()

        f = open("bill.txt", "a")
        f.write(str(dat))
        f.write("\n")
        f.close()

        cd = 0
        ct = 0
        f = open("bill.txt", "r")
        x = f.read()
        for i in x.split("\n"):
            if i == str(dat):
                cd += 1
            if i:
                ct += 1
        f.close()

        # in the folder where you have all the code Create a folder called Invoice
        # In invoice folder a new folder will be created with name as date and all bills of that date are stored in it
        directory = "C:/Users/akaas/Desktop/Project/Invoice/" + str(dat) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        com = "\t\tCOVID-19 Relief Pharmacy Pvt Ltd\n"
        add = "\t\t       Chennai,India\n"
        phone = "\t\t        9799999999\n"
        sample = "\t\t         Invoice\n"
        datee = "\t\t" + str(dat)
        tim = "\t" + str(d.strftime("%X")) + " " + str(d.strftime("%p"))

        table_head = "\n\n\t--------------------------------------------\n\tS.No\t  Products    \t Qty\t  Amount\n\t--------------------------------------------"
        final = com + add + phone + sample + datee + tim + "\n\n\t" + "Bill Number : " + str(ct) + "\n\tCustomer Name : " + self.fns + " " + self.lns + table_head

        # The bill is stored as Invoice number of that particular date
        file = "C:/Users/akaas/Desktop/Project/Invoice/%s/" % str(dat) + "Invoice" + str(cd) + ".txt"
        f = open(file, 'w')
        f.write(final)

        for i in range(len(prod_list)):
            f.write("\n\t" + str(i + 1) + "\t" + str(prod_list[i] + "        ")[:14] + "\t " + str(
                prod_quan[i]) + "\t  " + str(prod_price[i]) + "0")
        f.write("\n\n\tTOTAL: Rs " + str(sum(prod_price)) + "0")
        f.write("\n\tThanks for visiting")
        f.close()

        # Opening the bill
        os.system("C:/Desktop/Project/Invoice/%s/Invoice%s.txt" % (str(dat), str(cd)))

        prod_list.clear()
        prod_price.clear()
        prod_quan.clear()
        prod_dic.clear()
        bc.clear()
        inq.clear()
        self.fq.clear()
        self.fn.clear()
        self.fd.clear()
        self.sp.clear()

#akash's code
class inventory:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.master.title("LOGIN WINDOW")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.heading = Label(master, text="INVENTORY", font=('arial 40 bold'), fg=('steelblue'),bg="powder blue")
        self.heading.place(x=600, y=0)

        # lables
        self.name_l = Label(master, text="Enter product Name", font=('arial 18 bold'),bg="powder blue")
        self.name_l.place(x=10, y=100)

        self.doe = Label(master, text="Enter DOE", font=('arial 18 bold'),bg="powder blue")
        self.doe.place(x=10, y=150)

        self.p_id = Label(master, text="Enter Product ID", font=('arial 18 bold'),bg="powder blue")
        self.p_id.place(x=10, y=200)

        self.qty = Label(master, text="Enter Quantity", font=('arial 18 bold'),bg="powder blue")
        self.qty.place(x=10, y=250)

        self.cp = Label(master, text="Enter Cost Price", font=('arial 18 bold'),bg="powder blue")
        self.cp.place(x=10, y=300)

        self.sp = Label(master, text="Enter Selling Price", font=('arial 18 bold'),bg="powder blue")
        self.sp.place(x=10, y=350)

        # entries for lables
        self.name_e = Entry(master, width=30, font=('arial 18 bold'))
        self.name_e.place(x=300, y=100)

        self.doe_e = Entry(master, width=30, font=('arial 18 bold'))
        self.doe_e.place(x=300, y=150)

        self.pid_e = Entry(master, width=30, font=('arial 18 bold'))
        self.pid_e.place(x=300, y=200)

        self.qty_e = Entry(master, width=30, font=('arial 18 bold'))
        self.qty_e.place(x=300, y=250)

        self.cp_e = Entry(master, width=30, font=('arial 18 bold'))
        self.cp_e.place(x=300, y=300)

        self.sp_e = Entry(master, width=30, font=('arial 18 bold'))
        self.sp_e.place(x=300, y=350)

        # button for search
        self.btn_add = Button(master, text="Search", font=('arial 13 bold'), width=18, height=2, bg="steelblue", fg="white",command=self.search_row)

        self.btn_add.place(x=500, y=400)

        #btn to clear all
        self.btn_clear = Button(master, text="Clear all fields", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white',command=self.clear_all)
        self.btn_clear.place(x=300, y=400)

        # button to view inventory
        self.btn_view = Button(master, text="VIEW THE INVENTORY", font=('arial 13 bold'), width=20, height=2, bg="lightgreen", fg="white",command=self.inventory_list)
        self.btn_view.place(x=480, y=500)
        self.tBox = scrolledtext.ScrolledText(master, width=70, height=40)
        self.tBox.place(x=760, y=100)
        # scrolled box on the right

    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.doe_e.delete(0, END)
        self.pid_e.delete(0, END)
        self.qty_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)

    def search_row(self, *args, **kwargs):
        self.tBox.config(state="normal")
        self.tBox.delete(1.0, END)
        self.name = self.name_e.get()
        self.Doe = self.doe_e.get()
        self.pid = self.pid_e.get()
        self.qty_f = self.qty_e.get()
        self.c = self.cp_e.get()
        self.s = self.sp_e.get()
        if (self.Doe != ''):
            sql = "SELECT* FROM inventory where Prod_name=%s OR DOE=%s OR Prod_ID=%s OR Qty=%s OR CostPrice=%s OR SellingPrice=%s "
            c.execute(sql, (self.name, self.Doe, self.pid, self.qty_f, self.c, self.s))
            rows = c.fetchall()
        if (self.Doe == ''):
            sql = "SELECT* FROM inventory where Prod_name=%s OR Prod_ID=%s OR Qty=%s OR CostPrice=%s OR SellingPrice=%s "
            c.execute(sql, (self.name, self.pid, self.qty_f, self.c, self.s))
            rows = c.fetchall()

        self.tBox.insert(END, "   PRODUCT NAME    |    DOE     | PRODUCT ID |  QTY  |  CP  | SP  \n")
        for x in rows:
            fx1 = str(x[0])  # to access values of eac h column
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            fx5 = str(x[4])
            fx6 = str(x[5])
            self.tBox.insert(END, ("   " + fx1 + " " * (16 - len(fx1)) + "| " + fx2 + " " * (10 - len(fx2)) + " | " + fx3 + " " * (
                    11 - len(fx3)) + "| " + fx4 + " " * (6 - len(fx4)) + "| " + fx5 + " " * (
                                5 - len(fx5)) + "| " + fx6 + " " * (5 - len(fx6))))

            self.tBox.insert(END, "\n")
        self.tBox.config(state="disabled")

        # function to view the items in the inventory

    def inventory_list(self, *args, **kwargs):
        win = Tk()
        frm = Frame(win)
        win.title("LIST OF ITEMS IN INVENTORY")
        frm.pack(side=tkinter.LEFT, padx=10)
        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6), show="headings", height=25)
        tv.pack()
        tv.heading(1, text="PRODUCT NAME")
        tv.column(1, minwidth=0, width=150)

        tv.heading(2, text="DOE")
        tv.column(2, minwidth=0, width=150)

        tv.heading(3, text="PRODUCT ID")
        tv.column(3, minwidth=0, width=150)

        tv.heading(4, text="QTY")
        tv.column(4, minwidth=0, width=150)

        tv.heading(5, text="COST PRICE")
        tv.column(5, minwidth=0, width=150)

        tv.heading(6, text="SELLING PRICE")
        tv.column(6, minwidth=0, width=150)

        sql = "select* from inventory"
        c.execute(sql)
        rows = c.fetchall()
        for x in rows:
            tv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5]))

class expired_inventory:
    def __init__(self, master,*args,**kwargs):
        self.master = master
        self.master.title("LOGIN WINDOW")
        self.master.geometry("1366x768+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.heading = Label(master, text="EXPIRED INVENTORY", font=('arial 40 bold'), fg=('steelblue'),bg="powder blue")
        self.heading.place(x=400, y=0)

        # lables
        self.name_l = Label(master, text="Enter product Name", font=('arial 18 bold'),bg="powder blue")
        self.name_l.place(x=10, y=100)

        self.doe = Label(master, text="Enter DOE", font=('arial 18 bold'),bg="powder blue")
        self.doe.place(x=10, y=150)

        self.p_id = Label(master, text="Enter Product ID", font=('arial 18 bold'),bg="powder blue")
        self.p_id.place(x=10, y=200)

        self.qty = Label(master, text="Enter Quantity", font=('arial 18 bold'),bg="powder blue")
        self.qty.place(x=10, y=250)

        self.cp = Label(master, text="Enter Cost Price", font=('arial 18 bold'),bg="powder blue")
        self.cp.place(x=10, y=300)

        self.sp = Label(master, text="Enter Selling Price", font=('arial 18 bold'),bg="powder blue")
        self.sp.place(x=10, y=350)

        # entries for lables
        self.name_e = Entry(master, width=30, font=('arial 18 bold'))
        self.name_e.place(x=300, y=100)

        self.doe_e = Entry(master, width=30, font=('arial 18 bold'))
        self.doe_e.place(x=300, y=150)

        self.pid_e = Entry(master, width=30, font=('arial 18 bold'))
        self.pid_e.place(x=300, y=200)

        self.qty_e = Entry(master, width=30, font=('arial 18 bold'))
        self.qty_e.place(x=300, y=250)

        self.cp_e = Entry(master, width=30, font=('arial 18 bold'))
        self.cp_e.place(x=300, y=300)

        self.sp_e = Entry(master, width=30, font=('arial 18 bold'))
        self.sp_e.place(x=300, y=350)

        # button for search
        self.btn_add = Button(master, text="Search", font=('arial 13 bold'), width=18, height=2, bg="steelblue", fg="white",command=self.search_row)

        self.btn_add.place(x=500, y=400)

        #btn to clear all
        self.btn_clear = Button(master, text="Clear all fields", font=('arial 13 bold'), width=18, height=2,bg="steelblue", fg='white',command=self.clear_all)
        self.btn_clear.place(x=300, y=400)

        # button to view expired inventory
        self.btn_view = Button(master, text="VIEW THE EXPIRED INVENTORY", font=('arial 13 bold'), width=30, height=2, bg="red", fg="white",
                               command=self.EXPIRED_LIST)
        self.btn_view.place(x=400, y=500)

        # button to view inventory
        self.btn_view = Button(master, text="VIEW THE INVENTORY", font=('arial 13 bold'), width=20, height=2, bg="lightgreen", fg="white",
                               command=self.inventory_list)
        self.btn_view.place(x=180, y=500)


        self.tBox = scrolledtext.ScrolledText(master, width=70, height=40)
        self.tBox.place(x=760, y=100)

        # scrolled box on the right

    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0, END)
        self.doe_e.delete(0, END)
        self.pid_e.delete(0, END)
        self.qty_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)



    def search_row(self, *args, **kwargs):
        self.tBox.config(state="normal")
        self.tBox.delete(1.0, END)
        self.name = self.name_e.get()
        self.Doe = self.doe_e.get()
        self.pid = self.pid_e.get()
        self.qty_f = self.qty_e.get()
        self.c = self.cp_e.get()
        self.s = self.sp_e.get()
        if (self.Doe != ''):
            sql = "SELECT* FROM expired_inventory where Prod_name=%s OR DOE=%s OR Prod_ID=%s OR Qty=%s OR CostPrice=%s OR SellingPrice=%s "
            c.execute(sql, (self.name, self.Doe, self.pid, self.qty_f, self.c, self.s))
            rows = c.fetchall()
        if (self.Doe == ''):
            sql = "SELECT* FROM expired_inventory where Prod_name=%s OR Prod_ID=%s OR Qty=%s OR CostPrice=%s OR SellingPrice=%s "
            c.execute(sql, (self.name, self.pid, self.qty_f, self.c, self.s))
            rows = c.fetchall()

        self.tBox.insert(END, "   PRODUCT NAME    |    DOE     |PRODUCT ID  | QTY   | CP   | SP\n")
        for x in rows:
            fx1 = str(x[0])  # to access values of eac h column
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            fx5 = str(x[4])
            fx6 = str(x[5])
            self.tBox.insert(END, ( "   " + fx1 + " " * (16 - len(fx1)) + "| " + fx2 + " " * (10 - len(fx2)) + " | " + fx3 + " " * (
                        11 - len(fx3)) + "| " + fx4 + " " * (6 - len(fx4)) + "| " + fx5 + " " * (
                                5 - len(fx5)) + "| " + fx6 + " " * (5 - len(fx6))))

            self.tBox.insert(END, "\n")
        self.tBox.config(state="disabled")

        # function to view the items in the inventory

    def EXPIRED_LIST(self, *args, **kwargs):
        win = Tk()
        frm = Frame(win)
        win.title("LIST OF ITEMS IN EXPIRED INVENTORY")
        frm.pack(side=tkinter.LEFT, padx=10)
        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6), show="headings", height=25)
        tv.pack()
        tv.heading(1, text="PRODUCT NAME")
        tv.column(1, minwidth=0, width=150)

        tv.heading(2, text="DOE")
        tv.column(2, minwidth=0, width=150)

        tv.heading(3, text="PRODUCT ID")
        tv.column(3, minwidth=0, width=150)

        tv.heading(4, text="QTY")
        tv.column(4, minwidth=0, width=150)

        tv.heading(5, text="COST PRICE")
        tv.column(5, minwidth=0, width=150)

        tv.heading(6, text="SELLING PRICE")
        tv.column(6, minwidth=0, width=150)

        tdy = date.today()
        c.execute("SELECT * FROM inventory WHERE DOE < '%s'" % (tdy,))
        result = c.fetchall()
        for x in result:
            fx1 = str(x[0])  # to access values of each column
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            fx5 = str(x[4])
            fx6 = str(x[5])
            s = "INSERT INTO expired_inventory (Prod_name, DOE, Prod_ID, Qty, CostPrice, SellingPrice) VALUES(%s, %s, %s, %s, %s, %s)	"
            c.execute(s, (fx1, fx2, fx3, fx4, fx5, fx6))
            mydb.commit()
        c.execute("SELECT * FROM expired_inventory WHERE DOE < '%s'" % (tdy,))
        result = c.fetchall()
        for x in result:
            fx1 = str(x[0])  # to access values of eac h column
            fx2 = str(x[1])
            fx3 = str(x[2])
            fx4 = str(x[3])
            fx5 = str(x[4])
            fx6 = str(x[5])
            tv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5]))
            mydb.commit()
        c.execute("DELETE FROM inventory WHERE DOE < '%s'" % (tdy,))
        mydb.commit()
        # inventory

    def inventory_list(self, *args, **kwargs):
        win = Tk()
        frm = Frame(win)
        win.title("LIST OF ITEMS IN INVENTORY")
        frm.pack(side=tkinter.LEFT, padx=10)
        tv = ttk.Treeview(frm, columns=(1, 2, 3, 4, 5, 6), show="headings", height=25)
        tv.pack()
        tv.heading(1, text="PRODUCT NAME")
        tv.column(1, minwidth=0, width=150)

        tv.heading(2, text="DOE")
        tv.column(2, minwidth=0, width=150)

        tv.heading(3, text="PRODUCT ID")
        tv.column(3, minwidth=0, width=150)

        tv.heading(4, text="QTY")
        tv.column(4, minwidth=0, width=150)

        tv.heading(5, text="COST PRICE")
        tv.column(5, minwidth=0, width=150)

        tv.heading(6, text="SELLING PRICE")
        tv.column(6, minwidth=0, width=150)

        sql = "select* from inventory"
        c.execute(sql)
        rows = c.fetchall()
        for x in rows:
            tv.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5]))

root=Tk()
top=Toplevel()
app=Login_window(top)
application=Main_menu(root)
root.withdraw()
root.mainloop()
