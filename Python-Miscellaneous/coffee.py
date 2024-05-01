class Coffee:

    def __init__(self, kind, price, weight):
        self.__coffee_kind = kind
        self.__coffee_price = price
        self.__coffee_weight = weight

    def set_coffee_kind(self, kind):
        self.__coffee_kind = kind

    def set_coffee_price(self, price):
        self.__coffee_price = price

    def set_coffee_weight(self, weight):
        self.__coffee_weight = weight

    def get_coffee_kind(self):
        return self.__coffee_kind
    
    def get_coffee_price(self):
        return self.__coffee_price

    def get_coffee_weight(self):
        return self.__coffee_weight

    def buy_coffee(self, amt):
        self.__coffee_weight += amt

    def sell_coffee(self, amt):
        if self.__coffee_weight >= amt:
            self.__coffee_weight -= amt
        else:
            print("You do not have enough coffee on hand to sell the amount requested.")

    def __str__(self):
        return "Kind: "+ self.__coffee_kind + \
               "\nPrice: " + str(self.__coffee_price) + \
               "\nWeight: " + str(self.__coffee_weight)
    
