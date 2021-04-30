from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time


root = Tk()
root.title("State Bank of Amphibius")
root.resizable(False,False)

def clock():
    a = time.strftime("%H")
    b = time.strftime("%M")
    c = time.strftime("%S")
    L5.config(text=a+":"+b+":"+c)
    L5.after(1000,clock)


def SubW():
    global E22
    global L32
    
    a = int(E22.get())
    if a < 1000 :
        messagebox.showerror('Erorr','Insufficient Balance')
        print(L32.config(text="You can not withdraw money at this time"))

def back1():
    
    root1.deiconify()
    

def With():
    
    global E22
    global L32
    root1.withdraw()
    
    root2 = Tk()
    root2.title("WithDrawal Options")
    L12 = Label(root2,text="Please Enter Your Amount in Rs.")
    L12.grid(row=0,column=0,columnspan=2)
    E22 = Entry(root2,width=20)
    E22.grid(row=1,column=0,columnspan=2)
    B12= Button(root2,text="Submit",command=SubW)
    B12.grid(row=2,column=0,pady=5)
    B22 = Button(root2,text="Back",command=back1)
    B22.grid(row=2,column=1,pady=5)
    L32 = Label(root2,text="")
    L32.grid(row=3,column=0,columnspan=2)

def back2():
    root1.deiconify()
    

def Depo():
    root1.withdraw()
    root3 = Tk()
    root3.title("Deposits Options")
    L13 = Label(root3,text="Please Enter Your Amount")
    L13.grid(row=0,column=0,columnspan=2)
    E23 = Entry(root3,width=20)
    E23.grid(row=1,column=0,columnspan=2)
    B13= Button(root3,text="Submit")
    B13.grid(row=6,column=0,pady=5)
    B23 = Button(root3,text="Back",command=back2)
    B23.grid(row=6,column=1,pady=5)

def back3():
    
    root1.deiconify()

def Bal():
    root1.withdraw()
    root4 = Tk()
    root4.title("Balance Options")
    L14 = Label(root4,text="Please Choose Your Account")
    L14.grid(row=0,column=0,columnspan=2)
    B14= Button(root4,text="Submit")
    B14.grid(row=6,column=0,pady=5)
    B24 = Button(root4,text="Back",command=back3)
    B24.grid(row=6,column=1,pady=5)

def back4():
    
    root1.deiconify()

def Tran():
    root1.withdraw()
    root5 = Tk()
    root5.title("Transfers and payments Options")
    L15 = Label(root5,text="Please Choose Your Option")
    L15.grid(row=0,column=0,columnspan=2)
    B15= Button(root5,text="Submit")
    B15.grid(row=6,column=0,pady=5)
    B25 = Button(root5,text="Back",command=back4)
    B25.grid(row=6,column=1,pady=5)

def back5():
    
    root1.deiconify()

def Oth():
    root1.withdraw()
    root6 = Tk()
    root6.title("Other Services Options")
    L16 = Label(root6,text="Please Choose Your Option")
    L16.grid(row=0,column=0,columnspan=2)
    kst= StringVar()
    C16= ttk.Combobox(root6,textvariable=kst)
    C16.grid(row=1,column=0,columnspan=2)
    C16['values'] = ('Update PIN',"Mini Statement",'Mobile Recharge',"Electricity Bill","Insurance Bill")
    B16 = Button(root6,text="Submit")
    B16.grid(row=6,column=0,pady=5)
    B26 = Button(root6,text="Back",command=back5)
    B26.grid(row=6,column=1,pady=5)

def back6():
    
    root1.deiconify()

def Upd():
    root1.withdraw()
    root7 = Tk()
    root7.title("Update Information Options")
    L17 = Label(root7,text="Please Choose Your Option")
    L17.grid(row=0,column=0,columnspan=2)
    lst= StringVar()
    C17= ttk.Combobox(root7,textvariable=lst)
    C17.grid(row=1,column=0,columnspan=2)
    C17['values'] = ('Mobile No.','Email Address',"Aadhar Card No.","Pan Card No.")
    B17 = Button(root7,text="Submit")
    B17.grid(row=6,column=0,pady=5)
    B27 = Button(root7,text="Back",command=back6)
    B27.grid(row=6,column=1,pady=5)

def back7():
    
    root.deiconify()


def SubMit():
    global root1
    if E1.get() == "Shubham" and E2.get() == '1234' :
        print(L3.config(text="Login Sucessefull !"))
        root.withdraw()
        root1 = Tk()
        root1.title("Banking Options")
        L10 = Label(root1,text="Please your Banking Option")
        L10.grid(row=0,column=0,columnspan=2)
        B11 = Button(root1,text="Withdrawals",width=20,command=With)
        B11.grid(row=1,column=0,pady=5)
        B21 = Button(root1,text="Deposits",width=20,command=Depo)
        B21.grid(row=1,column=1,pady=5)
        B31 = Button(root1,text="Balance inquiries",width=20,command=Bal)
        B31.grid(row=2,column=0,pady=5)
        B41 = Button(root1,text="Transfers and payments ",width=20,command=Tran)
        B41.grid(row=2,column=1,pady=5)
        B51 = Button(root1,text="Other Services",width=20,command=Oth)
        B51.grid(row=3,column=0,pady=5)
        B61 = Button(root1,text="Update Information",width=20,command=Upd)
        B61.grid(row=3,column=1,pady=5)
        B17 = Button(root1,text="Submit")
        B17.grid(row=6,column=0,pady=5)
        B27 = Button(root1,text="Back",command=back7)
        B27.grid(row=6,column=1,pady=5)
        

    else :
        messagebox.showerror("Erorr","Please enter correct inputs to Login")
        print(L3.config(text="Wrong Credentials"))
        #B1.config(state=DISABLED)
        

def Can():
    E1.delete(0,END)
    E2.delete(0,END)
    L3.config(text="")

L1 = Label(root,text="Enter the User Id :",width=20,anchor="center")
L1.grid(row=2,column=0,columnspan=2)
E1 = Entry(root,width=20,justify="c")
E1.grid(row=3,column=0,columnspan=2)
L2 = Label(root,text="Enter the Password :",width=20,anchor="center")
L2.grid(row=4,column=0,columnspan=2)
E2 = Entry(root,width=20)
E2.grid(row=5,column=0,columnspan=2)
E2.config(show="*")

B1 = Button(root,text="Submit",command=SubMit)
B1.grid(row=6,column=0,pady=5)
B2 = Button(root,text="Cancel",command=Can)
B2.grid(row=6,column=1,pady=5)
L3 = Label(root,text="")
L3.grid(row=7,column=0,columnspan=2)
L5 = Label(root,text="")
L5.grid(row=8,column=0,columnspan=2)

clock()

root.mainloop()