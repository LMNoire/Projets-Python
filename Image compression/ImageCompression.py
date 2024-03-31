import tkinter as tk
from tkinter import filedialog
from PIL import Image

def compress_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path)
    myWidth, myHeight = img.size
    
    # Resize image with Lanczos filter
    img = img.resize((myWidth, myHeight), Image.LANCZOS)
    
    save_path = filedialog.asksaveasfilename()
    img.save(save_path + "_compressed.jpg")

def main():
    root = tk.Tk()
    root.title("Image Compression")
    
    compress_button = tk.Button(root, text="Compress Image", command=compress_image)
    compress_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()