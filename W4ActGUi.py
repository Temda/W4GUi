'''
Author  : Chaiyapon Sowanna
STD ID  : 1650702473
Week    : 4
Label   : Class Activity
Desc    : Basic GUI #3
Date    : 2023-01-31

To finish this class activity, calculating total amount 
from three items when each item is clicked.

'''

from multiprocessing.sharedctypes import Value
from optparse import Values
from tkinter import *

# To initialize a window for application
# สร้างหน้าต่าง และกำหนดค่า ของหน้าต่างของโปรแกรม
def mainwindow() :
    root = Tk()
    root.title("GUI3: Class Activity of Week4")
    root.geometry("600x500")
    root.configure(bg='lightgreen')
    root.rowconfigure((0,2),weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=4)
    return(root)

# To initialize layout widgets of window application
# จัดวาง Layout ของหน้าต่างโปรแกรม
def createframe(root) :
    top = Frame(root,bg='#694E4E')
    top.rowconfigure(0,weight=1)
    top.columnconfigure((0,1),weight=1)
    fm_left = Frame(root,bg='#F3C5C5')
    fm_left.rowconfigure((0,1,2),weight=1)
    fm_left.columnconfigure(0,weight=1)
    fm_right = Frame(root,bg='#886F6F')
    fm_right.rowconfigure((0,1,2),weight=1)
    fm_right.columnconfigure(0,weight=1)
    fm_bottom = Frame(root,bg='#694E4E')
    fm_bottom.rowconfigure(0,weight=1)
    fm_bottom.columnconfigure(0,weight=1)
    top.grid(row=0,columnspan=2,sticky=NSEW)
    fm_left.grid(row=1,column=0,sticky=NSEW)
    fm_right.grid(row=1,column=1,sticky=NSEW)
    fm_bottom.grid(row=2,columnspan=2,sticky=NSEW)
    return(root,top,fm_left,fm_right,fm_bottom)

# To initialize widgets of top frame.
def widgettop(top) : 
    btn1 = Button(top,image=img1,text="Click Me1",compound='top')
    btn1.grid(row=0,column=0,ipadx=30)
    btn2 = Button(top,image=img2,text="Click Me2",compound='top')
    btn2.grid(row=0,column=1,ipadx=30)

# To initialize widgets of left frame.
def widgetleft(left) :
    tag1 = Label(left,image=img3,bg='#F3C5C5')
    tag1.grid(row=0)
    tag2 = Label(left,image=img4,bg='#F3C5C5')
    tag2.grid(row=1)
    tag3 = Label(left,image=img5,bg='#F3C5C5')
    tag3.grid(row=2)

# To initialize widgets of right frame.
def widgetright(right) :
    # TODO : Hint!
    # ** To configure widgets **
    
    click1 = Checkbutton(right,text="Address book1: 100 bahts",bg='#694E4E', 
    onvalue = 100, 
    offvalue = 0,
    variable=v1,
    command=fnclick)
    click1.grid(row=0,sticky='w',padx=20,ipadx=30,ipady=10)
    click2 = Checkbutton(right,text="Address book2: 250 bahts",bg='#694E4E', 
    onvalue = 250, 
    offvalue = 0,
    variable=v2,
    command=fnclick)
    click2.grid(row=1,sticky='w',padx=20,ipadx=30,ipady=10)
    click3 = Checkbutton(right,text="Address book3: 150 bahts",bg='#694E4E', 
    onvalue = 150, 
    offvalue = 0,
    variable=v3,
    command=fnclick)
    click3.grid(row=2,sticky='w',padx=20,ipadx=30,ipady=10)

# To initialize widgets of bottom frame.
def widgetbottom(bottom) :
    lbl_showtotal = Label(bottom,bg='#694E4E', font=("Helvetica", "16","bold"))
    lbl_showtotal.grid(row=0, column=0, sticky=NSEW, ipady=10,pady=5)
    return lbl_showtotal

# Function for calculating and display total amount.
def fnclick() :
    # to access global variable `net`
    global net
    net = v1.get() +  v2.get() + v3.get()
    # print(v1.get())
    # print(v2.get())
    # print(v3.get())
    
    print(net)

    # total = net + v1.get(values=100) + v2.get() + v3.get()
    # print(total)
    
    # TODO: Hint!
    # To calculate total amount and assign the result to `net`
    # after you get the result, don't forget to uncomment below.
    # 
    # YOUR CODE
    if net == 0:
        lbl_showtotal["bg"] = '#F8DEB5'
        lbl_showtotal["fg"] = '#CD0404'
        output.set("-โปรดเลือกรายการ-")
        lbl_showtotal["textvariable"] = output
    else:
        lbl_showtotal["bg"] = '#F8DEB5'
        lbl_showtotal["fg"] = '#694E4E'
        output.set("Total Amount = %0.2f"%net)
        lbl_showtotal["textvariable"] = output
    # lbl_showtotal["text"] = output


    

root = mainwindow()
net = 0

# define control widget variable.
v1,v2,v3 = IntVar(),IntVar(),IntVar()
output = StringVar()

# Prepare images
img1 = PhotoImage(file='images/icon1.png')
img2 = PhotoImage(file='images/icon2.png')
img3 = PhotoImage(file="images/book1.png")
img4 = PhotoImage(file="images/book2.png")
img5 = PhotoImage(file="images/book3.png")

# create window and frame widgets
root,fm_top,fm_left,fm_right,fm_bottom = createframe(root)

# create widgets for each layout
widgettop(fm_top)
widgetleft(fm_left)
widgetright(fm_right)
lbl_showtotal = widgetbottom(fm_bottom)

# open application window
root.mainloop()
