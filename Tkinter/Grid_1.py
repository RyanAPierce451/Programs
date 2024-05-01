from tkinter import *

root = Tk() # The Tk class is typically instantiated using all default values.
# Creating a Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name Is Ryan Pierce")
# Putting it onto the screen
# Messages won't adjust when screen changes size.
# The Grid is Relative
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop() 