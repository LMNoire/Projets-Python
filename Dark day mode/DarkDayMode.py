#Import librairie
from tkinter import *

#Define root
root=Tk()
root.title("Toogle Switch")
root.geometry("400x600")
root.configure(bg="white")

button_mode=True

#Define customize function to switch between dark and day
def customize():
    global button_mode
    if button_mode:
        button.config(image=off, bg="#26242f", activebackground="#26242f")
        root.config(bg="#26242f")
        button_mode=False
    else:
        button.config(image=on, bg="white", activebackground="white")
        root.config(bg="white")
        button_mode=True

#Images as button
on=PhotoImage(file=r"C:\Users\selim\Desktop\py\Dark day mode\light.png")
off=PhotoImage(file=r"C:\Users\selim\Desktop\py\Dark day mode\dark.png")

button=Button(root, image=on, bd=0, bg="white", activebackground="white", command=customize)
button.pack(padx=50, pady=50)

root.mainloop()