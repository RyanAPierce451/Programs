"""
PROGRAMMER: RYAN PIERCE
DATE:   09/04/2022
ASSIGNMENT:  Homework #1: High Point Craps  
ALGORITHM: Graphical Dice Simulator Trying to beat the first roll.
"""
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
from playsound import playsound
import random
import tkinter.font


bkg_color = "#0D865D" # Hex Color Green
white = "#FFFFFF" # Hex Color 
grey = "#D3D3D3"
yellow = "#F0E68C"

root = Tk() 
root.title("High Point Craps")
root.iconbitmap('C:/Users/ryanp/Documents/Python Files/Tkinter/Icons/Dice.ico')
root.geometry("960x720")
root.configure(bg=bkg_color)

def pSound():
    playsound("C:/Users/ryanp/Documents/Python Files/High Point Crap/dice_images/ThrowDice.mp3", block=True)

def CheckRoll():
    global RollToBeat
    global message
    global firstRoll
    global roll_count
    if total <= 3 and firstRoll != 0:
        messagebox.showinfo("Low Roll", "Re-Roll")
        pass
    if firstRoll == 1:
        if total > RollToBeat:
            if total > 3 and total < 11:
                RollToBeat = total
                if message == 1:
                    messagebox.showinfo("Number to Beat", "Beat This Number\nYou Have 2 Rolls.")
                    PointLabel.config(text=f"The Roll to Beat: {RollToBeat}")
                    RemainingLabel.config(text=f"Rolls Remaining: {roll_count}")
                    message -= 1
                    firstRoll -= 1
    elif firstRoll == 0:
        if roll_count != 0:
            roll_count -= 1
            RemainingLabel.config(text=f"Rolls Remaining: {roll_count}")
        if total > RollToBeat:
            messagebox.showinfo("You Won", "You Rolled High Enough. You Win!")
            root.destroy()
        if roll_count == 1 and total <= RollToBeat:
            messagebox.showinfo("One Roll", "Didn't Roll High Enough.\nOne Roll Remaining .")
        if roll_count == 0 and total <= RollToBeat:
            respond = messagebox.showinfo("You Lose", "Out of Rolls. You Lose.")
            if respond == "ok":
                root.destroy()
        
def Even_Money_Check(x):
    if x >= 11 and firstRoll != 0:
        messagebox.showinfo("Money Won", "You Doubled Your Money")
        global cash
        cash = cash*2
        uCash.config(text=(f"Cash: ${cash}"))

def get_value(x):
    if x == diceImg1:
        return(1)
    elif x == diceImg2:
        return(2)
    elif x == diceImg3:
        return(3)
    elif x == diceImg4:
        return(4)
    elif x == diceImg5:
        return(5)
    elif x == diceImg6:
        return(6)

def Roll_Dice():
    #Grabs from Dice List and Selects randomly
    dice1 = random.choice(dice_list)
    dice2 = random.choice(dice_list)

    #Gives Dice Value
    dvalue1 = get_value(dice1)
    dvalue2 = get_value(dice2)

    #Updates the Labels
    diceL1.config(image=dice1)
    diceL2.config(image=dice2)

    #Updates Dice Values
    dicevalue1.config(text=dvalue1)
    dicevalue2.config(text=dvalue2)

    #Update the Total
    global total
    total = dvalue1 + dvalue2
    totalLabel.config(text=f"You Rolled: {total}")
    
    #Plays Dice Sound
    pSound()  
    #Checks first Roll is higher then 11    
    Even_Money_Check(total)
    #Main Game Rolling Function
    CheckRoll()  
        
#Dice Images
diceImg0= ImageTk.PhotoImage(Image.open("C:/Users/ryanp/Documents/Python Files/High Point Crap/dice_images/d0.png"))
diceImg1= ImageTk.PhotoImage(Image.open("C:/Users/ryanp/Documents/Python Files/High Point Crap/dice_images/d1.png"))
diceImg2= ImageTk.PhotoImage(Image.open("C:/Users/ryanp/Documents/Python Files/High Point Crap/dice_images/d2.png"))
diceImg3= ImageTk.PhotoImage(Image.open("C:/Users/ryanp/Documents/Python Files/High Point Crap/dice_images/d3.png"))
diceImg4= ImageTk.PhotoImage(Image.open("C:/Users/ryanp/Documents/Python Files/High Point Crap/dice_images/d4.png"))
diceImg5= ImageTk.PhotoImage(Image.open("C:/Users/ryanp/Documents/Python Files/High Point Crap/dice_images/d5.png"))
diceImg6= ImageTk.PhotoImage(Image.open("C:/Users/ryanp/Documents/Python Files/High Point Crap/dice_images/d6.png"))


#Dice List
dice_list = [diceImg1,diceImg2,diceImg3,diceImg4,diceImg5,diceImg6]

# Text
helv20 = tkinter.font.Font(family="Helvetica",size=20,weight="bold")
helv24 = tkinter.font.Font(family="Helvetica",size=24,weight="bold")
helv36 = tkinter.font.Font(family="Helvetica",size=36,weight="bold")

#number of rolls, Start message.
roll_count = 2
RollToBeat = 0
message = 1
firstRoll = 1


# Creates a Frame
uFrame = Frame(root, bg=bkg_color)
uFrame.pack(pady=20)

# Creates Dice Labels
diceL1 = Label(uFrame, image=diceImg0, bg=bkg_color)
diceL1.grid(row=0, column=0)
dicevalue1 = Label(uFrame, text="",font=helv24,bg=bkg_color)
dicevalue1.grid(row=1,column=0)


diceL2 = Label(uFrame, image=diceImg0, bg=bkg_color)
diceL2.grid(row=0, column=1,)
dicevalue2 = Label(uFrame, text="",font=helv24,bg=bkg_color)
dicevalue2.grid(row=1,column=1)

#Creates Roll To Beat Label
PointLabel = Label(root, text="",font=helv36, bg=bkg_color, fg=yellow)
PointLabel.pack()

#Creates Roll Button
uButton = Button(root, text="Roll Dice", command=Roll_Dice, font=helv20)
uButton.pack(pady=20)

#Creates Totals Label
totalLabel = Label(root, text="", font=helv36,bg=bkg_color, fg=grey)
totalLabel.pack(pady=40)

# Creates Cash Label
cash = 100
uCash = Label(root, text=(f"Cash: ${cash}"),font=helv24,bg=bkg_color)
uCash.pack(pady=20)

# Creates Remaining Dice Rolls Label
RemainingLabel = Label(root, text="", font=helv20,bg=bkg_color, fg=grey)
RemainingLabel.pack(pady=20)

root.mainloop()