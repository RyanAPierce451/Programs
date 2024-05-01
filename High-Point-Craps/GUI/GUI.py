from tkinter import *

root = Tk() # The Tk class is typically instantiated using all default values.
# Creating a Label Widget
myLabel = Label(root, text="Hello World!")
# Putting it onto the screen
myLabel.pack()
root.mainloop()