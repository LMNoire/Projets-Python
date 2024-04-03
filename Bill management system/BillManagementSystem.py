#Import librairie
from tkinter import *

#Define root
root=Tk()
root.geometry("1000x500")
root.title("Bill management")
root.resizable(False, False)

#Define reset and total functions
def Reset():
    entry_water.delete(0, END)
    entry_tea.delete(0, END)
    entry_coffee.delete(0, END)
    entry_chocolate.delete(0, END)
    entry_soda.delete(0, END)
    entry_pancake.delete(0, END)

def Total():
    try:a1=int(Water.get())
    except:a1=0

    try:a2=int(Tea.get())
    except:a2=0

    try:a3=int(Coffee.get())
    except:a3=0

    try:a4=int(Chocolate.get())
    except:a4=0

    try:a5=int(Soda.get())
    except:a5=0

    try:a6=int(Pancake.get())
    except:a6=0

    c1=0*a1
    c2=1.5*a2
    c3=1.5*a3
    c4=1.5*a4
    c5=2*a5
    c6=2*a6

    lbl_total=Label(f2, font=('aria', 20, 'bold'), text="Total", width=16, fg="lightyellow", bg="black")
    lbl_total.place(x=0, y=50)

    entry_total=Entry(f2,font=('aria', 20, 'bold'), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_total.place(x=20, y=100)

    totalcost=c1+c2+c3+c4+c5+c6
    string_bill="€.", str('%.2f' %totalcost)
    Total_bill.set(string_bill)


#Define GUI interface
Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

f=Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1,width=300, height=370)
f.place(x=10, y=118)

Label(f, text="Menu", font=("Gabriola", 40, 'bold'), fg="black", bg="lightgreen").place(x=80,y=0)

#Menu
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Water....................Free", fg="black", bg="lightgreen").place(x=10, y=80)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Tea.....................1.50€", fg="black", bg="lightgreen").place(x=10, y=110)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Coffee..................1.50€", fg="black", bg="lightgreen").place(x=10, y=140)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Chocolate...............1.50€", fg="black", bg="lightgreen").place(x=10, y=170)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Soda....................2.00€", fg="black", bg="lightgreen").place(x=10, y=200)
Label(f, font=("Lucida Calligraphy", 15, 'bold'), text="Pancake.................2.00€", fg="black", bg="lightgreen").place(x=10, y=230)

f2=Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Bill=Label(f2, text="Bill", font=('calibri', 20), bg="lightyellow")
Bill.place(x=120, y=10)

f1=Frame(root, bd=5, height=370,width=300, relief=RAISED)
f1.pack()

Water=StringVar()
Tea=StringVar()
Coffee=StringVar()
Chocolate=StringVar()
Soda=StringVar()
Pancake=StringVar()
Total_bill=StringVar()

lbl_water=Label(f1, font=("aria", 20, 'bold'), text="Water", width=12, fg="blue4")
lbl_tea=Label(f1, font=("aria", 20, 'bold'), text="Tea", width=12, fg="blue4")
lbl_coffee=Label(f1, font=("aria", 20, 'bold'), text="Coffee", width=12, fg="blue4")
lbl_chocolate=Label(f1, font=("aria", 20, 'bold'), text="Chocolate", width=12, fg="blue4")
lbl_soda=Label(f1, font=("aria", 20, 'bold'), text="Soda", width=12, fg="blue4")
lbl_pancake=Label(f1, font=("aria", 20, 'bold'), text="Pancake", width=12, fg="blue4")

#Label position
lbl_water.grid(row=1,column=0)
lbl_tea.grid(row=2,column=0)
lbl_coffee.grid(row=3,column=0)
lbl_chocolate.grid(row=4,column=0)
lbl_soda.grid(row=5,column=0)
lbl_pancake.grid(row=6,column=0)

#Amount of items
entry_water=Entry(f1, font=("aria", 20, 'bold'),textvariable=Water, bd=6, width=8, bg="lightpink")
entry_tea=Entry(f1, font=("aria", 20, 'bold'),textvariable=Tea, bd=6, width=8, bg="lightpink")
entry_coffee=Entry(f1, font=("aria", 20, 'bold'),textvariable=Coffee, bd=6, width=8, bg="lightpink")
entry_chocolate=Entry(f1, font=("aria", 20, 'bold'),textvariable=Chocolate, bd=6, width=8, bg="lightpink")
entry_soda=Entry(f1, font=("aria", 20, 'bold'),textvariable=Soda, bd=6, width=8, bg="lightpink")
entry_pancake=Entry(f1, font=("aria", 20, 'bold'),textvariable=Pancake, bd=6, width=8, bg="lightpink")

entry_water.grid(row=1, column=1)
entry_tea.grid(row=2, column=1)
entry_coffee.grid(row=3, column=1)
entry_chocolate.grid(row=4, column=1)
entry_soda.grid(row=5, column=1)
entry_pancake.grid(row=6, column=1)

#Buttons
btn_reset=Button(f1, bd=5, fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Reset", command=Reset)
btn_reset.grid(row=7, column=0)

btn_total=Button(f1,bd=5,fg="black", bg="lightblue", font=("ariel", 16, 'bold'), width=10, text="Total", command=Total)
btn_total.grid(row=7, column=1)

root.mainloop()