import kivy
kivy.require('1.0.5')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.popup import Popup

import sqlite3
from buttonex import ButtonEx
from pos_system import POS
from loginscreen import LoginScreen
from logoutscreen import LogoutScreen

#from kivy.config import Config
#Config.set('graphics', 'fullscreen', 'auto')

APPERTIZERS_NAME    = 'Appetizers'
MEAT_NAME           = 'Meat'
FISH_NAME           = 'Fish'
VEGAN_NAME          = 'Vegan'
DRINKS_NAME         = 'Drinks'
DESSERT_NAME        = 'Dessert'


class Controller(FloatLayout):

    a_buylist = ObjectProperty()
    a_articles = ObjectProperty()
    a_baroptions = ObjectProperty()
    a_price = ObjectProperty()

    ###
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.pos_system = POS()
        self.connDB = sqlite3.connect('possystem.db')
        self.userLogin()

    ###
    def userLogin(self):
        content = LoginScreen(root_self = self)

        ##
        self.popup = Popup(
                        title           = 'User Login',
                        content         = content,
                        auto_dismiss    = False,
                        size_hint       = (None, None),
                        size            = (400, 170)
                    )

        # open the popup
        self.popup.open()

    ###
    def userLogout(self, obj):
        content = LogoutScreen(root_self = self)

        self.popup = Popup(
                        title           = 'User Logout',
                        content         = content,
                        auto_dismiss    = False,
                        size_hint       = (None, None),
                        size            = (400, 170)
                    )

        # open the popup
        self.popup.open()

    ###
    def loadMainWindow(self, obj = None):

        self.atual_menu = 0
        op_n = 1
        mainOptions = [APPERTIZERS_NAME, MEAT_NAME, FISH_NAME, VEGAN_NAME, DRINKS_NAME, DESSERT_NAME]

        self.a_articles.clear_widgets()

        for op in mainOptions:
            button = Button(text=op)
            button.bind(on_press=self.openNewMenu)
            op_n = op_n + 1
            self.a_articles.add_widget(button)

        for a in range(op_n-1, 9):
            self.a_articles.add_widget(Label(text=''))

        self.bt_next.enabled = False
        self.bt_previous.enabled = False
        self.bt_clearlist.enabled = False
        self.bt_finishlist.enabled = False

    ###
    def loadBarOptions(self):
        self.a_baroptions.add_widget(Button(text='Close Session', on_press=self.userLogout))
        self.bt_newlist = ButtonEx(text = 'New List', on_press=self.startNewBuyList)
        self.a_baroptions.add_widget(self.bt_newlist)
        self.bt_clearlist = ButtonEx(text = 'Clear List', on_press=self.clearBuyList)
        self.a_baroptions.add_widget(self.bt_clearlist)
        self.bt_finishlist = ButtonEx(text = 'Finish List', on_press=self.finishBuyList)
        self.a_baroptions.add_widget(self.bt_finishlist)
        self.bt_next = ButtonEx(text = 'Next')
        self.a_baroptions.add_widget(self.bt_next)
        self.bt_previous = ButtonEx(text = 'Previous')
        self.a_baroptions.add_widget(self.bt_previous)
        self.a_baroptions.add_widget(Button(text = 'Menu', on_press = self.loadMainWindow))

    ###
    def openNewMenu(self, obj):
        op_n = 1
        query = 'SELECT name FROM products WHERE type="' + obj.text.lower() + '" LIMIT 9'
        cursor = self.connDB.execute(query)

        self.a_articles.clear_widgets()

        for row in cursor:
            button = Button(text=row[0])
            button.bind(on_press=self.addToBuyList)
            op_n = op_n + 1
            self.a_articles.add_widget(button)

        for a in range(op_n-1, 9):
            self.a_articles.add_widget(Label(text=''))

        self.bt_next.enabled = True
        self.bt_previous.enabled = False

    ###
    def addToBuyList(self, obj):
        if(self.pos_system.getBuyList() == None):
            content = Label(text = 'You need to start a new list!')
            popup = Popup(
                        title           = 'No Buy List',
                        content         = content,
                        size_hint       = (None, None),
                        size            = (400, 100)
                    )

            # open the popup
            popup.open()
            return

        button = Button(text=obj.text, size_hint_y = None, height = 40)
        button.bind(on_press = self.removeFromBuyList)
        self.a_buylist.add_widget(button)
        self.pos_system.getBuyList().addItem(item_name = obj.text, price = 5)
        self.updateTotalPrice()

    ###
    def removeFromBuyList(self, obj):
        self.a_buylist.remove_widget(obj)
        self.pos_system.getBuyList().removeItem(item_name = obj.text)
        self.updateTotalPrice()

    ###
    def clearBuyList(self, obj):
        self.a_buylist.clear_widgets()
        self.pos_system.getBuyList().clearList()

    ###
    def startNewBuyList(self, obj):
        self.pos_system.newBuyList()
        self.bt_clearlist.enabled = True
        self.bt_finishlist.enabled = True
        self.bt_newlist.enabled = False

    ###
    def finishBuyList(self, obj):
        self.clearBuyList(obj=obj)
        self.bt_clearlist.enabled = False
        self.bt_finishlist.enabled = False
        self.bt_newlist.enabled = True

    ###
    def updateTotalPrice(self):
        #
        self.a_price.label_price.text = str(self.pos_system.getBuyList().getTotalPrice()) + "€"


class PosApp(App):

    def build(self):
        return Controller()