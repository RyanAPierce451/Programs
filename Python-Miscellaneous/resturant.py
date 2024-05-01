'''
PROGRAMMER:  RYAN PIERCE
DATE:        03-02-2022 
ASSIGNMENT:  BRANCHING AND LOOPING 
ALGORITHM:   LOOP THROUGH A MENU WHILE INPUTING NUMBER OF GUEST, SELECTING ITEMS ON MENU, INPUT QUANITY OF SELECTED ITEM, 
             INPUT IF GUEST IS STILL SELECTING ITEMS, AND A PRINT OF TOTAL COST WITH AND WITHOUT TAX 
'''

total = 0
check_list = []
menu_items = {
    "Plain Egg": 1.95,
    "Bacon and Egg": 3.45,
    "Oatmeal": 2.95,
    "Muffin": 1.75,
    "French Toast": 4.95,
    "Pancake": 1.50,
    "Bacon (2 slices)": 1.95,
    "Fresh Fruit": 3.25,
    "Coffee": 1.95,
    "Tea": 1.95
}

print("Hi how many our dining?")

while True: ## loop to check input for integer
    guest_number = input("Enter An integer: ")
    if(guest_number) != True:
        try:
            guest_number = int(guest_number)
            break
        except ValueError:
            print("Error! Not An Integer. Try Again")

g = guest_number ## total guest used in final reciept

print("\nRight this way to your table, here's our menu.\n")
print("Ryan's Morning Meal\nPlain Egg --$1.95\nBacon and Egg -- #3.45\nOatmeal -- $2.95\nMuffin -- $1.75") ## Menu
print("French Toast -- $4.95\nPancake -- $1.50\nBacon (2 slices) -- $1.95\nFresh Fruit -- $3.25\nCoffee -- $1.95\nTea -- $1.95\n") ## Menu

print("**MUST BE TYPED EXACT WAY DISPLAYED OR ITEM WON'T WORK**") ## Important User message

while guest_number != 0: ## MAIN Loop of selections 
    item_price_total = 0
    j = 1
    while True: ## Loop to check if item exist
        item_choice = input("\nWhat would you like to order: ")
        if item_choice in menu_items:
            break
        else:
            print("Sorry we don't have that item, Try again.")

    while True: ## Loop to check user input for amount of selected item
        print(f"{item_choice}, and how many would you like: ", end = "")
        item_amount = input("")
        if(item_amount) != True:
            try:
                item_amount = int(item_amount)
                break
            except ValueError:
                print("Error! Not An Integer. Try Again")

    print('Order of', item_amount , item_choice,"meals\n")

    while j != 0: ## Loop to check guest continues order or moves on to next guest
        if guest_number != 0:
            print("Is guest", guest_number, "finished ordering: ", end = "")
            guest_reply = int(input("(1)Yes (2)No\nTYPE THE NUMBER ASSOCIATED WITH RESPONSE: "))
            if guest_reply == 1:
                guest_number -= 1
                j = 0
            elif guest_reply == 2:
                j = 0
            else:
                print("Invalid Choice, Try Again")
      
    item_price_total = menu_items.get(item_choice) * int(item_amount)
    total += item_price_total
    check_list.insert(0, "x") ## Creating Item List for final print
    check_list.insert(1, str(item_amount))
    check_list.insert(2, "      ")
    check_list.insert(3, str(item_choice))
    check_list.insert(4, "     $")
    check_list.insert(5, str(menu_items.get(item_choice)))
    check_list.insert(6, "     $")
    check_list.insert(7, str(round(menu_items.get(item_choice) * item_amount,2)))

print("\n        Ryan's Morning Meal\n")
print("Guest Check            Party of", g)
print("Table: 102            Ticket 4589")
print("Server: RYAN              REG 104")
print("=====================================")
print("Qty Description       Price   Amount")
print("=====================================")
print("             **DINE-IN**")
for i in range(0, len(check_list), 8): 
    print("".join(check_list[i:i+8])) ## Printing list from 0 - 7 then indenting

tax = total * 0.0825
total_due = total + (total * 0.0825)
print("                             ---------")
print("Sub Total:                     $%.2f" % (total))
print("Sales Tax:                     $%.2f" % (tax))
print("                             ---------")
print("                        Total: $%.2f" % (total_due),)
print("                  Balance Due: $%.2f" % (total_due))