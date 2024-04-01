#Import librairies
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

#Define showimage function
def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", 
                                          filetype=(("JPG File", "*.jpg"),
                                                    ("PNG File", "*.png"),
                                                    ("All files", "*.")))
    if filename:
        img = Image.open(filename)
        #Get root dimentions
        window_width = root.winfo_width()
        window_height = root.winfo_height()
        
        #Resize image
        img.thumbnail((window_width, window_height))
        
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image = img

#Define interface
root=Tk()

frame=Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)

lbl=Label(root)
lbl.pack()

#Define buttons to select an image and exit
btn=Button(frame, text="Select Image", command=showimage)
btn.pack(side=tk.LEFT)

btn2=Button(frame, text="Exit", command=lambda:exit())
btn2.pack(side=tk.LEFT, padx=12)

root.title("Image Viewer")
root.geometry("400x450")

root.mainloop()