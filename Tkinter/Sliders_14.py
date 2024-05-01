from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')
root.geometry("400x400")

def slide():
    uLabel = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack() # IMPORTANT DON'T PACK ON SAME LINE

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

uLabel = Label(root, text=horizontal.get()).pack()

uButton = Button(root, text="Click Me!", command=slide).pack()

root.mainloop()