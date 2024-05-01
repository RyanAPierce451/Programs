import random
from tabnanny import check
from telnetlib import GA

# Provides image based on dice value
def get_value(x):
    if x == 1:
        return("\u2680")
    elif x == 2:
        return("\u2681")
    elif x == 3:
        return("\u2682")
    elif x == 4:
        return("\u2683")
    elif x == 5:
        return("\u2684")
    elif x == 6:
        return("\u2685")

#Gives Dice Roll and Displays image Function
def Roll_Dice():
    #Creates Random Numbers
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    #Gets the Unicode Dice Images
    dicevalue1 = get_value(dice1)
    dicevalue2 = get_value(dice2)
    print(dicevalue1, dicevalue2)
    return dice1, dice2


def Process_Point(Total_Roll):
    global bet 
    global cash
    global total_bet
    #Number of Rolls
    remainingRolls = 2
    #Loops Based on Number of Rolls 
    while remainingRolls != 0:
        input('\nPress Enter to roll ')
        Roll = Roll_Dice()
        d1 = Roll[0]
        d2 = Roll[1]
        Total = sum(Roll)
        print(f"You Rolled a {d1} and {d2}")
        if Total > Total_Roll:
            if Total >= 11:
                cash += total_bet*2
                bet = 0
                print("High Roll. Bet Doubles, You Win! Bet goes to player.")
                return bet
            cash += total_bet 
            bet = 0
            print(f"Rolled an {Total} That beats the roll. Bet goes to player.")
            return bet
            

        else:
            remainingRolls -= 1
            if remainingRolls == 1:
                print(f'{Total} is not good enough to beat {Total_Roll} last chance. Re-Roll')
            else: 
                print(f'{Total} is not good enough to beat {Total_Roll}. bet goes to the house.\n')
                bet = 0
                return bet
                



cash = 100
bet = 0
print("Welcome to High Point Craps.\nRules:\nRoll the dice between 4 and 10 to get your Roll-To-Beat")
print("if you roll a 3 or lower you re-roll.\nif you roll a 11 or 12 you re-roll.\nYou have 2 tries to roll higher.")
print("During the game if you roll 11 or 12 you win double the bet amount.")
print("if you don't roll high enough after 2 tries you lose.")
print("if you roll high enough you win the bet amount.")
print(f"\nYour Cash: ${cash}")
while True:
    while bet == 0:
        value = False
        #Creates Betting Value
        while value == False:
            wager = input('\n***MUST BE A WHOLE NUMBER***\n***$5 or Higher***\nEnter an amount to bet: ')
            checkT = wager.isdigit()
            if checkT == True and int(wager) <= cash:
                if checkT == True and int(wager) >= 5:
                    bet = int(wager)
                    cash -= int(wager)
                    value = True
                    house_list = [bet, bet, bet, bet*2,bet/2]
                    house_bet = random.choice(house_list)
                    total_bet = bet + house_bet
                    print(f"\nYour Cash: ${cash}")
                    print(f"Betting: ${bet}, House Betting: {house_bet}")
                    print(f'Pot Value: ${total_bet}')
                else:
                    print("***INCORRECT INPUT***")
            elif checkT == False and int(wager) <= cash:
                    print("***INCORRECT INPUT***")
            else:
                print("***Insufficent Funds***")


    input('\nPress Enter to roll ')
    Roll = Roll_Dice()
    Total_Roll = sum(Roll)
    d1 = Roll[0]
    d2 = Roll[1]
    if Total_Roll > 3 and Total_Roll < 11: 
        print(f'You rolled {d1} and {d2}\nYour Roll to Beat is: {Total_Roll}\n')
        Process_Point(Total_Roll)
        print(f"\nYour Cash: ${cash}")
        if cash <= 4:
            print("Out of Cash. Game Over.")
            break
        while True:
            replay = str(input("\nTYPE Y/N\nWant to Play again?: ")).strip().capitalize()
            if replay == "Y":
                break
            elif replay == "N":
                break
            else:
                print("***INCORRECT INPUT***")
        if replay == "N":
            break
    elif Total_Roll <= 3:
        print(f'You rolled {d1} and {d2}\nYour Total is: {Total_Roll}\n\nToo Low. Re-Roll')
    elif Total_Roll >= 11:
        print(f'You rolled {d1} and {d2}\nYour Total is: {Total_Roll}\n\nToo High. Re-Roll')
print("Thanks for playing High Point Craps!")