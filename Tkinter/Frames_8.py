from tkinter import *
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')

frame = LabelFrame(root, text="This is my Frame...", padx=5, pady=5)
frame.pack(padx=50, pady=50)

b = Button(frame, text="Don't Click Here!")
b.pack()

root.mainloop()