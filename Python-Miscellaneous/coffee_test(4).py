import coffee

def show_inventory(K, E, C):
    print("*** COFFEE INVENTORY ***")
    print(K)
    print("*-"*12)
    print(E)
    print("*-"*12)
    print(C)
    print()

def main():
    Kona = coffee.Coffee("Hawaiian Kona", 20.95, 100)
    Ethiopian = coffee.Coffee("Ethiopian", 8.00, 1000)
    Columbian = coffee.Coffee("Columbian", 9.50, 1700)

    show_inventory(Kona, Ethiopian, Columbian)

    print("\n\nYou are going to sell 20 pounds of Kona.")
    Kona.sell_coffee(20)

    print("*** HAWAIIAN KONA INVENTORY ***")
    print(Kona)
    print()

    Kona.buy_coffee(500)

    show_inventory(Kona, Ethiopian, Columbian)
main()
