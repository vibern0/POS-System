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
import buttonex
import pos_system
import loginscreen

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
    label_tprice = ObjectProperty()
    #pos = pos_system.POS()

    ###
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.connDB = sqlite3.connect('possystem.db')
        self.userLogin()

    ###
    def userLogin(self):
        content = loginscreen.LoginScreen(root_self=self)

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
    def userLogout(self):
        pass

    ###
    def loadMainWindow(self):

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

    ###
    def loadBarOptions(self):
        self.a_baroptions.add_widget(Button(text = 'Close Session'))
        self.a_baroptions.add_widget(Button(text = 'New List'))
        self.a_baroptions.add_widget(Button(text = 'Finish'))
        self.bt_next = buttonex.ButtonEx(text = 'Next')
        self.a_baroptions.add_widget(self.bt_next)
        self.bt_previous = buttonex.ButtonEx(text = 'Previous')
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
        button = Button(text=obj.text, size_hint_y = None, height = 40)
        button.bind(on_press = self.removeToBuyList)
        self.a_buylist.add_widget(button)
        self.updateTotalPrice()

    ###
    def removeToBuyList(self, obj):
        self.a_buylist.remove_widget(obj)
        self.updateTotalPrice()

    ###
    def startNewBuyList(self):
        pass

    ###
    def updateTotalPrice(self):
        pass


class PosApp(App):

    def build(self):
        return Controller()