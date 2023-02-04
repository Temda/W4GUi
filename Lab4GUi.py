'''
Author  : Chaiyapon Sowanna
STD ID  : 1650702473
Week    : 4
Label   : Class Activity
Desc    : Lab 4
Date    : 2023-01-31
'''

'''
Hint!

1 สร้างหน้าต่างโปรแกรม พร้อมกำหนด grid rowconfigure, columnconfigure ให้เหมาะสม
2 ออกแบบโครงสร้างของหน้าจอด้วย Frame & Labelframe พร้อมกำหนด grid rowconfigure, columnconfigure ให้เหมาะสมกับแต่ละ Frame
3 วาง widget ตามแบบ
4 ประกาศตัวแปรประเภท Spy เพื่อช่วยผูกข้อมูลกับ widget
5 ผูก function กับ widget เพื่อคำนวณ และแสดงรายละเอียด
6 ใช้ messagebox สำหรับ confirm กับผู้ใช้

Keep Fighting!

'''


from tkinter import *
from tkinter import messagebox

def mainwindow() :
    root = Tk()
    root.title("Lab4 : My sweet cake shop by Chaiyapon Sowanna")
    root.geometry("900x700")
    root.configure(bg="pink")
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1,weight=1)
    root.columnconfigure((0,1),weight=4)
    return(root)
    
def createframe(root):
    top = Frame(root,bg="pink")
    top.rowconfigure((0),weight=1)
    top.columnconfigure((0),weight=1)
    top.grid_propagate(0)

    fm_left = Frame(root,bg="light blue")
    fm_left.rowconfigure((1,2,3),weight=2)
    fm_left.rowconfigure((4),weight=1)
    fm_left.columnconfigure((0,1),weight=1)
    top.grid_propagate(0)

    fm_right = Frame(root,bg="#8FC9A3")
    fm_right.rowconfigure((1,2,3),weight=1)
    fm_right.rowconfigure((4),weight=3)
    fm_right.columnconfigure((0,1),weight=1)
    top.grid_propagate(0)

    fm_bottom = Frame(root,bg="pink")
    fm_bottom.rowconfigure(0,weight=1)
    fm_bottom.columnconfigure((0,1),weight=1)
    top.grid_propagate(0)
    
    top.grid(row=0,columnspan=2,sticky=NSEW)
    fm_left.grid(row=1,column=0,sticky=NSEW)
    fm_right.grid(row=1,column=1,sticky=NSEW)
    fm_bottom.grid(row=2,columnspan=2,sticky=NSEW)
    return(root,top,fm_left,fm_right,fm_bottom)

def widgettop(top):
    txt1 = Label(top,text="My cake shop",bg="Pink", font='Tahoma 30 bold',fg="white")
    txt1.grid(row=0,column=0,columnspan=2)

def widgetleft(left):
    left_label = Label(left,text="Cake Menu",bg='lightblue',fg='black',font='Tahoma 15',anchor=NW)
    left_label.grid(row=0,padx=5,ipadx=30,sticky=NW)

    pro1_img = Label(left,image=img1,bg="light blue",anchor=S)
    pro1_txt = Label(left,text="Product 1:Wow 1\n Price 180 THB",bg="lightblue",fg="Black",font='Tahoma 15',anchor=S)
    product1 = Spinbox(left,from_=0,to=10,justify=CENTER,bg="white",fg='Black',highlightbackground="light blue",width=12,state="readonly", textvariable=v1)
    pro1_txt.grid(row=1,column=1,ipady=20,sticky=NW)
    
    product1.grid(row=1,column=1,rowspan=2,pady=100, ipadx="40", sticky=NW)
    pro1_img.grid(row=1,column=0)
    pro2_img = Label(left,image=img2,bg="light blue",anchor=S)
    pro2_txt = Label(left,text="Product 2:Wow 2\n Price 250 THB",bg="lightblue",fg="Black",font='Tahoma 15',anchor=S)
    product2 = Spinbox(left,from_=0,to=10,justify=CENTER,bg="white",fg='Black',highlightbackground="light blue",width=12,state="readonly", textvariable=v2)
    pro2_txt.grid(row=2,column=1,ipady=20,sticky=NW)
    product2.grid(row=2,column=1,rowspan=2,pady=100, ipadx="40", sticky=NW)
    pro2_img.grid(row=2,column=0)
    pro3_img = Label(left,image=img3,bg="light blue",anchor=S)
    pro3_txt = Label(left,text="Product 3:Wow 3\n Price 380 THB",bg="lightblue",fg="Black",font='Tahoma 15',anchor=S)
    product3 = Spinbox(left,from_=0,to=10,justify=CENTER,bg="white",fg='Black',highlightbackground="light blue",width=12,state="readonly", textvariable=v3)
    pro3_txt.grid(row=3,column=1,ipady=20,sticky=NW)
    product3.grid(row=3,column=1,rowspan=2,pady=100, ipadx="40", sticky=NW)
    pro3_img.grid(row=3,column=0)

    checkout_btn = Button(left,text="Checkout",image=img4,compound=LEFT,fg="Black",highlightbackground="White", height=30, command=submits)
    checkout_btn.grid(row=4,columnspan=2,sticky=NSEW)


def widgetright(right):

    right_label = Label(right,text="Product Summary",bg='#8FC9A3',fg='black',font='Tahoma 15',anchor=NW)
    right_label.grid(row=0,ipady=10,padx=5,sticky=NW)

    text1 = Label(right,text="Product 1:Wow 1\n Price 180 THB",bg='#8FC9A3',fg="black",font='Tahoma 15')

    box1 = Entry(right, bg="white", width=20, fg="black", font='Tahoma 10', textvariable="")
    box1.config(state=DISABLED)
    text1.grid(row=1,column=0)
    box1.grid(row=1,column=1, ipady=5)

    text2 = Label(right,text="Product 2:Wow 2\n Price 250 THB",bg='#8FC9A3',fg="black",font='Tahoma 15')

    box2 = Entry(right, bg="white", width=20, fg="black", font='Tahoma 10', textvariable="")
    box2.config(state=DISABLED)
    text2.grid(row=2,column=0)
    box2.grid(row=2,column=1, ipady=5)

    text3 = Label(right,text="Product 3:Wow 3\n Price 380 THB",bg='#8FC9A3',fg="black",font='Tahoma 15')
    box3 = Entry(right, bg="white", width=20, fg="black", font='Tahoma 10', textvariable="")

    box3.config(state=DISABLED)
    text3.grid(row=3,column=0)
    box3.grid(row=3,column=1, ipady=5)

    total = Label(right,text="Total price:",bg='#8FC9A3',fg="black",font='Tahoma 15')

    box4 = Entry(right, bg="white", width=20, fg="black", font='Tahoma 10', textvariable="")


    box4.config(state=DISABLED)
    total.grid(row=4,column=0,pady=30,sticky=N)
    box4.grid(row=4,column=1,pady=30,sticky=N, ipady=5)

    return box1,box2,box3,box4

def widgetbottom(bottom):
    click1 = Button(bottom,text="Exit program",image=img5,compound=LEFT,command=fnQuit,fg="Black",highlightbackground="White", height=40, width=130)
    click1.grid(row=0,column=0,columnspan=2,sticky=E,pady=10,padx=10)


    
def submits():
    global net
    pro1 = v1.get() * 180 # value 1
    pro2 = v2.get() * 250 # value 2
    pro3 = v3.get() * 380 # value 3

    net = pro1 + pro2 + pro3 #total
    print(net)
    if net > 0:
        output1.set(pro1) # value 1
        output2.set(pro2) # value 2
        output3.set(pro3) # value 3
        output4.set(net) # total

        box1["textvariable"] = output1
        box2["textvariable"] = output2
        box3["textvariable"] = output3
        box4["textvariable"] = output4
    else:
        messagebox.showerror(title="แจ้งเตือน", message="กรุณาเลือกรายการ",)

def fnQuit():
    result = messagebox.askyesno("Exit Program","Do you want to quit?")
    if result == 1:
        quit()




root = mainwindow()
net = 0

v1,v2,v3,v4 = IntVar(),IntVar(),IntVar(),IntVar()
output1 = StringVar()
output2 = StringVar()
output3 = StringVar()
output4 = StringVar()


img1 = PhotoImage(file="images/cake_1.png").subsample(2)
img2 = PhotoImage(file="images/cake_2.png").subsample(2)
img3 = PhotoImage(file="images/cake_3.png").subsample(2)
img4 = PhotoImage(file="images/cart.png").subsample(2)
img5 = PhotoImage(file="images/exit.png").subsample(2)

root,fm_top,fm_left,fm_right,fm_bottom = createframe(root)

widgettop(fm_top)
widgetleft(fm_left)
box1,box2,box3,box4, = widgetright(fm_right)
widgetbottom(fm_bottom)

root.mainloop()