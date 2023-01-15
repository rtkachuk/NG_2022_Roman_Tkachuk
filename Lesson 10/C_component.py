class Component:
    __name = ""
    __price = 0
    __discount = 0

    def __init__(self, name, price):
        self.__price = price
        self.__name = name
        self.__discount = 0

    def setPrice(self, price):
        if price > 0:
            self.__price = price
        else:
            print ("Error: price cannot be lower than 1")

    def getDiscountPrice(self):
        return self.__price - (self.__price / 100 * self.__discount)
    
    def __str__(self):
        return f"{self.__name}, price: {self.__price}"