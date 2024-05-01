from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk() 
root.title("Frames to Programs")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')

def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())
    file.close()

b = Button(root, text="Open", command=openFile).pack()
root.mainloop()