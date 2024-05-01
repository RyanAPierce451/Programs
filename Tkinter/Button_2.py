from faulthandler import disable
from tkinter import *

root = Tk() 

def userClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

userButton = Button(root, text='Click Me!', command=userClick, fg='blue')
userButton.pack()

root.mainloop() 