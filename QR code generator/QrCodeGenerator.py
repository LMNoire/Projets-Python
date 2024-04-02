#Import librairies
from tkinter import *
import qrcode

#Define root
root=Tk()
root.title("Qr code generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False, False)

#Define icon photo
image_icon=PhotoImage(file=r"C:\Users\selim\Desktop\py\QR code generator\icon.png")
root.iconphoto(False, image_icon)

#Define generate qr code function
def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    #Save result
    qr.save(r"C:\Users\selim\Desktop\py\QR code generator\Qrcode/" + str(name) + ".png")

    #Display result
    global Image
    Image=PhotoImage(file=r"C:\Users\selim\Desktop\py\QR code generator\Qrcode/" + str(name) + ".png")
    Image_view.config(image=Image)

Image_view=Label(root, bg="#AE2321")
Image_view.pack(padx=50, pady=10, side=RIGHT)

#GUI interface
Label(root, text="Title", fg="white", bg="#AE2321", font=15,).place(x=50, y=170)

title=Entry(root, width=13, font="arial 15")
title.place(x=50, y=200)

entry=Entry(root, width=28, font="arial 15")
entry.place(x=50, y=250)

Button(root, text="Generate", width=20, height=2, bg="black", fg="white", command=generate).place(x=50, y=300)

root.mainloop()