from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')
root.geometry("400x400")

def show():
    uLabel = Label(root, text=var.get()).pack()
    uLabel2 = Label(root, text=var2.get()).pack()


var = StringVar()
var2 = IntVar()

c = Checkbutton(root, text="String Box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

c2 = Checkbutton(root, text="Integer Box", variable=var2)
c2.deselect()
c2.pack()

uButton = Button(root, text="Show Selection", command=show).pack()


root.mainloop()