"""
************
PROGRAMMER: RYAN A PIERCE
DATE:   February 02, 2023
ASSIGNMENT:  HOMEWORK #1: HIGH POINT CRAPS
ALGORITHM:  USER-INPUT ENTER KEY TO ROLL DICE TO GET A TOTAL.
            THE TOTAL NEEDS TO BE BETWEEN 4-10 | 
            2-3 RE-ROLL | 
            11-12 EVEN MONEY WIN AND RE-ROLL | 
            TRY TO ROLL HIGHER THEN FIRST ROLL (YOU GET 2 CHANCES)
************
"""

import random

def Roll_Two_Dice(Roll): 
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1, dice2

def Even_Money_Check(Total_Roll):
    if Total_Roll >= 11:
        Money_Check = True
    else:
        Money_Check = False
    return Money_Check

def Process_Point(Total_Roll):
    x = 3 # NUMBER OF TRIES
    print(f"\nYour total to beat is: {Total_Roll}")
    while x != 0:
        User_Input = input('Press Enter to roll ')
        Roll = ()
        Roll = Roll_Two_Dice(Roll)
        New_Total = sum(Roll)
        print(Roll, '=', New_Total)
        if New_Total > Total_Roll:
            return New_Total
        else:
            x -= 1
            if x == 1:
                print(New_Total, 'is not good enough last chance. Re-Roll')
            else: print(New_Total, 'That is not good enough to beat', Total_Roll)
    return New_Total

while True: #breaks after acceptable roll has been made
    User_Input = input('Press Enter to roll ') 
    Roll = ()
    Roll = Roll_Two_Dice(Roll) # random roll function for 2 numbers
    Total_Roll = sum(Roll) # sums up total of 2 numbers
    print('You rolled:', Roll, '\nYour total is:', Total_Roll) # Tells the User what they rolled and the total of that roll
    MCheck = Even_Money_Check(Total_Roll) #checks to see if total roll is 11 or more
    if MCheck == True: # User will roll again
        print('Even money won')
        continue
    elif Total_Roll <= 3: # User will roll again
        print('Re-roll')
        continue
    else: # a roll between a total of 4 or 10 has been made which breaks the loop
        break
Game = Process_Point(Total_Roll) # Function for when requirements are met for the roll game

if Game <= Total_Roll: #message for player at the end of the game based on the appropriate outcome
    print('you lose')
else:
    print('you win')

'''
FIX
2 TRIES TO 3 TRIES
REMOVED LIST FOR TUPLE
'''