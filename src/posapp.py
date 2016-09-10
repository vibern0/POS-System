# -*- coding: utf-8 -*-

import kivy
kivy.require('1.0.5')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.properties import ObjectProperty, BooleanProperty
from kivy.uix.popup import Popup


from buttonex import ButtonEx
from pos.pos_system import POS, Item
from database.db import Database
from session.loginscreen import LoginScreen
from session.logoutscreen import LogoutScreen

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
        self.database = Database();
        self.userLogin()
    
    ###
    def registerLogs(self, log_type):
        self.database.registerLogs(self.pos_system.getUserID(), log_type)

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

        if(self.pos_system.getBuyList() == None):
            self.bt_newlist.enabled = True
            self.bt_clearlist.enabled = False
            self.bt_finishlist.enabled = False

        self.menu_page = 0

    ###
    def loadBarOptions(self):
        self.a_baroptions.add_widget(Button(text='Close Session', on_press=self.userLogout))
        self.bt_newlist = ButtonEx(text = 'New List', on_press=self.startNewBuyList)
        self.a_baroptions.add_widget(self.bt_newlist)
        self.bt_clearlist = ButtonEx(text = 'Clear List', on_press=self.clearBuyList)
        self.a_baroptions.add_widget(self.bt_clearlist)
        self.bt_finishlist = ButtonEx(text = 'Finish List', on_press=self.finishBuyList)
        self.a_baroptions.add_widget(self.bt_finishlist)
        self.bt_next = ButtonEx(text = 'Next', on_press = self.changePage)
        self.a_baroptions.add_widget(self.bt_next)
        self.bt_previous = ButtonEx(text = 'Previous', on_press = self.changePage)
        self.a_baroptions.add_widget(self.bt_previous)
        self.a_baroptions.add_widget(Button(text = 'Menu', on_press = self.loadMainWindow))

    ###
    def changePage(self, obj):
        if obj == self.bt_next:
            self.menu_page = self.menu_page + 1
        elif obj == self.bt_previous:
            self.menu_page = self.menu_page - 1

        self.openNewMenu(obj = obj)

    ###
    def openNewMenu(self, obj):
        op_n = 1
        total_rows = 0
        if obj != self.bt_next and obj != self.bt_previous:
            self.menu_type = obj.text.lower()

        cursor = self.database.loadArticles(self.menu_type, self.menu_page)

        self.a_articles.clear_widgets()

        for row in cursor:
            total_rows = total_rows + 1
            if(total_rows > 9) : break
            button = Button(text=row[1])
            button.bind(on_press=self.addToBuyList)
            button.item = Item(id_p = row[0], name = row[1], price = row[2], tax = 0.2)
            op_n = op_n + 1
            self.a_articles.add_widget(button)

        for a in range(op_n-1, 9):
            self.a_articles.add_widget(Label(text=''))

        if(total_rows > 9):
            self.bt_next.enabled = True
        else:
            self.bt_next.enabled = False

        if(self.menu_page > 0):
            self.bt_previous.enabled = True
        else:
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
        self.pos_system.getBuyList().addItem(obj.item)
        self.updateTotalPrice()

    ###
    def removeFromBuyList(self, obj):
        self.a_buylist.remove_widget(obj)
        self.pos_system.getBuyList().removeItem(item_name = obj.text)
        self.updateTotalPrice()

    ###
    def clearBuyList(self, obj=None):
        self.a_buylist.clear_widgets()
        self.pos_system.getBuyList().clearList()
        self.updateTotalPrice()

    ###
    def startNewBuyList(self, obj):
        self.pos_system.newBuyList()
        self.bt_clearlist.enabled = True
        self.bt_finishlist.enabled = True
        self.bt_newlist.enabled = False

    ###
    def finishBuyList(self, obj):
        #ask to confirm
        content = BoxLayout(orientation = 'vertical')
        content.add_widget(Label(text = 'Do you really want to finish?'))
        button_confirm = Button(text='Finish')
        button_confirm.bind(on_press=self.registerBuy)
        button_cancel = Button(text='Cancel')
        button_cancel.bind(on_press=self.popup.dismiss)
        options = BoxLayout()
        options.add_widget(button_confirm)
        options.add_widget(button_cancel)
        content.add_widget(options)
        
        #
        self.popup = Popup(
                    title           = 'Finish Buy List',
                    content         = content,
                    size_hint       = (None, None),
                    size            = (400, 100)
                )

        # open the popup
        self.popup.open()
        
    ###
    def registerBuy(self, obj):
        self.database.registerBuy(self.pos_system.getBuyList(), 5533, self.pos_system.getUserName())
        
        self.clearBuyList()
        self.bt_clearlist.enabled = False
        self.bt_finishlist.enabled = False
        self.bt_newlist.enabled = True
        self.popup.dismiss()
    
    ###
    def updateTotalPrice(self):
        #
        self.a_price.label_price.text = str(self.pos_system.getBuyList().getTotalPrice()) + '€'


class PosApp(App):

    def build(self):
        return Controller()
