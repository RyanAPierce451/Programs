from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World!")
  
    if response == 1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()
    

Button(root, text="popup", command=popup).pack()

root.mainloop()