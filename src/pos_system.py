
class Item:
    def __init__(self, id_p, name, price, tax):
        self.id = id_p
        self.name = name
        self.price = price
        self.tax = tax

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_tax(self):
        return self.tax


class BuyList:
    def __init__(self):
        self.buyList = []
        self.total = 0

    def add_item(self, item):
        self.buyList.append(item)

    def remove_item(self, item_name):
        for item in self.buyList:
            if item.get_name() == item_name:
                self.buyList.remove(item)

    def get_all_items(self):
        return self.buyList

    def get_total_price(self):
        total_price = 0
        for product in self.buyList:
            total_price += product.get_price() + product.get_price() * product.get_tax()

        return total_price

    def clear_list(self):
        self.buyList = []


class POS:

    def __init__(self):
        self.buyList = None
        self.user = None
        self.userId = None

    def set_username(self, name):
        self.user = name

    def get_username(self):
        return self.user

    def set_user_id(self, user_id):
        self.userId = user_id

    def get_user_id(self):
        return self.userId

    def new_buy_list(self):
        self.buyList = BuyList()

    def close_buy_list(self):
        self.buyList = None

    def get_buy_list(self):
        return self.buyList
