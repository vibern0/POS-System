
class Item:
    def __init__(self, id_p, name, price, tax):
        self.id = id_p
        self.name = name
        self.price = price
        self.tax = tax

    def getID(self):
        return self.id

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

    def removeItem(self, item_name):
        for item in self.buy_list:
            if(item.getName() == item_name):
                self.buy_list.remove(item)

    def getAllItems(self):
        return self.buy_list

    def getTotalPrice(self):
        total_price = 0
        for product in self.buy_list:
            total_price += product.getPrice() + product.getPrice() * product.getTax()

        return total_price

    def clearList(self):
        self.buy_list = []

class POS:

    def __init__(self):
        self.buyList = None
        self.user = None

    def setUserName(self, name):
        self.user = name

    def getUserName(self):
        return self.user

    def setUserID(self, user_id):
        self.userID = user_id

    def getUserID(self):
        return self.userID

    def newBuyList(self):
        self.buyList = BuyList()

    def closeBuyList(self):
        self.buyList = None

    def getBuyList(self):
        return self.buyList
