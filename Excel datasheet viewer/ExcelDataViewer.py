from tkinter import *
from tkinter import messagebox
from tkinter import ttk, filedialog
import numpy
import pandas as pd

#Define interface
root=Tk()
root.title("Excel Datasheet Viewer")
root.geometry('1100x400+200+200')
image_icon=PhotoImage(file=r"C:\Users\selim\Desktop\py\Excel datasheet viewer\excel.png")
root.iconphoto(False, image_icon)

#Define open file
def open():
    filename = filedialog.askopenfilename(title="Open a file",
                                          filetypes=(("xlsx files", "*.xlsx"),
                                                     ("All Files", "*.")))
    
    #If corrupted file
    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)

        except:
            messagebox.showerror("Error", "You can't access this file")

    #Clear previous data
    tree.delete(*tree.get_children())

    #Datasheet heading
    tree['column'] = list(df.columns)
    tree['show'] = "headings"

    #Heading title
    for col in tree['column']:
        tree.heading(col, text=col)

    #Data
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tree.insert("", "end", values=row)

#Define frame
frame = Frame(root)
frame.pack(pady=25)

#Define treeview
tree = ttk.Treeview(frame)
tree.pack()

#Define open file button
button = Button(root, text='Open', width=60,height=2, font=30, fg="white", bg="#0078d7", command=open)
button.pack(padx=10,pady=20)

root.mainloop()