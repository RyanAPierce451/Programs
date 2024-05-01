from tkinter import *
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')

#r = IntVar()

#List of Tuples
Toppings = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]


pizz = StringVar()
pizz.set("Pepperoni")

#Loop to create radio buttons based on MODES variable
for text, Top_value in Toppings:
    Radiobutton(root, text=text, variable=pizz, value=Top_value).pack(anchor=W)

#radiobuton is clicked a value is passed and updates the label
def clicked(value):
    uLabel = Label(root, text=value)
    uLabel.pack()

uButton = Button(root, text="Click Me!", command=lambda: clicked(pizz.get()))
uButton.pack()

root.mainloop()