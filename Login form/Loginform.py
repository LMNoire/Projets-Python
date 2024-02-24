#Import libraries
from tkinter import *
from tkinter import messagebox

#Define login by getting username and password
def login():
    username=entry1.get()
    password=entry2.get()

    #If one field is blank
    if (username == "" and password == ""):
        messagebox.showinfo("", "Empty field not allowed")

    #If creditentials are goods
    elif (username == "Test" and password == "Password"):
        messagebox.showinfo("", "Login success")

    #If creditentials are incorrect
    else:
        messagebox.showinfo("", "Incorrect username and password")

#Construct login box
root=Tk()
root.title("Login")
root.geometry("300x200")

global entry1
global entry2

#Labels
Label(root, text="Username").place(x=20, y=20)
Label(root, text="Password").place(x=20, y=70)

#Placeholders
entry1=Entry(root, bd=5)
entry1.place(x=140, y=20)

entry2=Entry(root, bd=5)
entry2.place(x=140, y=70)

#Login button
Button(root, text="Login", command="Login", height=3, width=13, bd=6).place(x=100, y=120)

root.mainloop()


