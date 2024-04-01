#Import librairies
from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf #abandonned package, needed a fix to correctly display the loading bar
import os

#Define root
root=Tk()
root.geometry("630x700+400+100")
root.title("PDF Viewer")
root.configure(bg="white")

#Define browseFiles function to get pdf/txt files
def browseFiles():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                        title="select pdf file",
                                        filetype=(("PDF File", ".pdf"),
                                                  ("PDF File", ".PDF"),
                                                  ("All file", ".txt")))
    v1=pdf.ShowPdf()
    v2=v1.pdf_view(root, pdf_location=open(filename, "r"), width=77, height=100)
    v2.pack(pady=(0, 0))

#Define button
Button(root, text="open", command=browseFiles, width=40,
       font="arial 20", bd=4).pack()

root.mainloop()


