from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Icons,Images, and Exit Buttons")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')

#Turns Images into Variables
img1 = ImageTk.PhotoImage(Image.open("images/Girl.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images/cat.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images/sunset.jpg"))
img4 = ImageTk.PhotoImage(Image.open("images/Jump.png"))
img5 = ImageTk.PhotoImage(Image.open("images/wizard.jpg"))

#Turns Image variables into a List
img_list = [img1,img2,img3,img4,img5]

# Status Bar Variable
status = Label(root, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

# Label Variable and First Grid Output
user_label = Label(image=img1)
user_label.grid(row=0, column=0, columnspan=3)

def forward(img_num):
    global user_label
    global button_forward
    global button_back

    #Removes current image on screen
    user_label.grid_forget()
    # Reasigns new image from List
    user_label = Label(image=img_list[img_num-1])
    # Updates the Button's img_num Value
    button_forward = Button(root, text=">>", command=lambda: forward(img_num+1))
    button_back = Button(root, text="<<", command=lambda: back(img_num-1))

    #Disbles the button when last image is reached.
    if img_num == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    #Outputs the new image label and buttons with new values
    user_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    
    #Update Status Bar
    status = Label(root, text="Image " + str(img_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0,columnspan=3, sticky=W+E)

def back(img_num):
    global user_label
    global button_forward
    global button_back

    
    user_label.grid_forget()
    user_label = Label(image=img_list[img_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(img_num+1))
    button_back = Button(root, text="<<", command=lambda: back(img_num-1))

    #Disbles the button when first image is reached.
    if img_num == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    user_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    status = Label(root, text="Image " + str(img_num) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0,columnspan=3, sticky=W+E)

# Back, Exit, Forward Button Variables and calls to forward/back functions
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

#Button Grid Output, Where the Buttons and Status Bar will be located
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2, pady=10)
status.grid(row=2, column=0,columnspan=3, sticky=W+E)

root.mainloop()