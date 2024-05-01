from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Icons,Images, and Exit Buttons")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')

user_img = ImageTk.PhotoImage(Image.open("images/Dice.png"))
user_label = Label(image=user_img)
user_label.pack()








button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()