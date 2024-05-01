from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')



def open():
    global uImg
    root.filename = filedialog.askopenfilename(initialdir="Users/ryanp/Documents/Python Files/Tkinter/images",title="Select File", filetypes=(("all files","*.*"),("png files", "*.png")))
    uLabel = Label(root, text=root.filename).pack()
    uImg = ImageTk.PhotoImage(Image.open(root.filename))
    uImgLabel = Label(image=uImg).pack()


ubtn = Button(root, text="Open File", command=open).pack()

root.mainloop()