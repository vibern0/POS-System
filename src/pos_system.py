
class Item:
    def __init__(self, name, price, tax):
        self.name = name
        self.price = price
        self.tax = tax

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getTax(self):
        return self.tax

class BuyList:
    def __init__(self):
        self.buy_list = []
        self.total = 0

    def addItem(self, item):
        self.buy_list.append(item)

    def getAllItems(self):
        return self.buy_list

class POS:

    def __init__(self):
        self.user = ""

    def setUser(self):
        return self

    def getUser(self):
        return self.user

    def newBuyList(self):
        self.buyList = BuyList()

    def getBuyList(self):
        return self.buyList

    def printBuyList(self):
        i = self.buyList.getAllItems()
        for item in i:
            print(item.getName())
            print(item.getPrice())
            print(item.getTax())
            print(" ")
