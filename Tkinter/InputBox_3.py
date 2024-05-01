from faulthandler import disable
from tkinter import *

root = Tk() 

e = Entry(root, width=50)
e.pack()

def userClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

userButton = Button(root, text='Enter Your Name', command=userClick)
userButton.pack()

root.mainloop() 