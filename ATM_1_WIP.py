from tkinter import *
from tkinter import ttk

root = Tk()
root.title("State Bank of Amphibius")

def With():
    root2 = Tk()
    root2.title("WithDrawal Options")
    L12 = Label(root2,text="Please Enter Your Amount")
    L12.grid(row=0,column=0,columnspan=2)

def Depo():
    root3 = Tk()
    root3.title("Deposits Options")
    L13 = Label(root3,text="Please Enter Your Amount")
    L13.grid(row=0,column=0,columnspan=2)
    
def Bal():
    root4 = Tk()
    root4.title("Balance Options")
    L14 = Label(root4,text="Please Choose Your Account")
    L14.grid(row=0,column=0,columnspan=2)

def Tran():
    root5 = Tk()
    root5.title("Transfers and payments Options")
    L15 = Label(root5,text="Please Choose Your Option")
    L15.grid(row=0,column=0,columnspan=2)

def Oth():
    root6 = Tk()
    root6.title("Other Services Options")
    L16 = Label(root6,text="Please Choose Your Option")
    L16.grid(row=0,column=0,columnspan=2)
    kst= StringVar()
    C16= ttk.Combobox(root6,textvariable=kst)
    C16.grid(row=1,column=0,columnspan=2)
    C16['values'] = ('Update PIN',"Mini Statement",'Mobile Recharge',"Electricity Bill","Insurance Bill")

def Upd():
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
    B27 = Button(root7,text="Cancel")
    B27.grid(row=6,column=1,pady=5)


def SubMit():
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
    
def CanCel():
    pass

L1 = Label(root,text="Enter the User Id :",width=20,anchor="center")
L1.grid(row=2,column=0,columnspan=2)
E1 = Entry(root,width=20,justify="c")
E1.grid(row=3,column=0,columnspan=2)
L2 = Label(root,text="Enter the Password :",width=20,anchor="center")
L2.grid(row=4,column=0,columnspan=2)
E2 = Entry(root,width=20)
E2.grid(row=5,column=0,columnspan=2)

B1 = Button(root,text="Submit",command=SubMit)
B1.grid(row=6,column=0,pady=5)
B1 = Button(root,text="Cancel",command=CanCel)
B1.grid(row=6,column=1,pady=5)
L3 = Label(root,text="")
L3.grid(row=7,column=0,columnspan=2)

root.mainloop()