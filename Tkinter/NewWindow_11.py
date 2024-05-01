from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')

def open():
    global uImg
    top = Toplevel()
    top.title("Spiderman")
    top.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')
    uImg = ImageTk.PhotoImage(Image.open("images/Spiderman.jpg"))
    uLabel = Label(top, image=uImg).pack()
    btn2 = Button(top, text="Close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", command=open).pack()


root.mainloop()