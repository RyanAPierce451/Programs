from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')
root.geometry("400x400")

def show():
    uLabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]
clicked = StringVar()
clicked.set("Select")

drop = OptionMenu(root, clicked, *options)
drop.pack()

uButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()