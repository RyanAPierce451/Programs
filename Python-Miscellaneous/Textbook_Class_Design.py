"""
************
PROGRAMMER: RYAN A PIERCE
DATE:   OCTOBER 06, 2022
ASSIGNMENT:  HOMEWORK #5: TEXTBOOK CLASS DESIGN
ALGORITHM:   MODIFY CLASS OBJECTS WITH INPUT COMMANDS

************
"""

class Textbook_Inventory:

    def __init__(self):
        self.id = int(0)
        self.e_qty = int(0)
        self.e_price = float(20)
        self.f_qty = int(0)
        self.f_price = float(10)

    def getTotalValue(value):
        total_books = value.e_qty + value.f_qty
        total_price = (value.e_price * value.e_qty) + (value.f_price * value.f_qty)
        print(f'Total Books: {total_books}')
        print(f'Total Value: ${total_price}')

    def sell(remove):
        while True:
            question = input("\nAre you selling a Excellent Book or Fair Book? \n**TYPE E OR F**\n").upper()
            if question == "E":
                many = int(input("How Many Are You Selling: ")) 
                remove.e_qty -= many
                break
            elif question == "F":
                many = int(input("How Many Are You Selling: ")) 
                remove.f_qty -= many
                break
            else:
                print("Not an Answer Try Again\n")

    def buy(add):
        while True:
            question = input("\nAre you buying a Excellent Book or Fair Book? \n**TYPE E OR F**\n").upper()
            if question == "E":
                many = int(input("How Many Are You Buying: ")) 
                add.e_qty += many
                break
            elif question == "F":
                many = int(input("How Many Are You Buying: ")) 
                add.f_qty += many
                break
            else:
                print("Not an Answer Try Again\n")


librarian = Textbook_Inventory()
librarian.id = int(input("ID Number: "))
librarian.e_qty = int(input("Excellent QTY: "))
librarian.e_price = float(input("Excellent Condition Book Price: "))
librarian.f_qty = int(input("Fair QTY: "))
librarian.f_price = float(input("Fair Condition Book Price: "))

librarian.sell()
librarian.buy()

print("\nThe Final List:")
print(f"ID: {librarian.id}")
print(f"Excellent Books: {librarian.e_qty}")
print(f"Excellent Book Price: ${librarian.e_price}")
print(f"Fair Books: {librarian.f_qty}")
print(f"Fair Book Price: ${librarian.f_price}")
librarian.getTotalValue()

