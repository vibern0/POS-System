import kivy
kivy.require('1.0.5')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.properties import ObjectProperty, BooleanProperty

import sqlite3

#from kivy.config import Config
#Config.set('graphics', 'fullscreen', 'auto')

APPERTIZERS_NAME    = 'Appetizers'
MEAT_NAME           = 'Meat'
FISH_NAME           = 'Fish'
VEGAN_NAME          = 'Vegan'
DRINKS_NAME         = 'Drinks'
DESSERT_NAME        = 'Dessert'

class MyButton(Button):
    enabled = BooleanProperty(True)

    def on_enabled(self, instance, value):
        if value:
            self.background_color = [1,1,1,1]
            self.color = [1,1,1,1]
        else:
            self.background_color = [1,1,1,.3]
            self.color = [1,1,1,.5]

    def on_touch_down( self, touch ):
        if self.enabled:
            return super(self.__class__, self).on_touch_down(touch)


class Controller(FloatLayout):

    a_buylist = ObjectProperty()
    a_articles = ObjectProperty()
    label_tprice = ObjectProperty()
    bt_next = ObjectProperty()
    bt_previous = ObjectProperty()

    ###
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.connDB = sqlite3.connect('possystem.db')
        self.loadMainWindow()

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
    def openNewMenu(self, obj):
        op_n = 1
        query = 'SELECT name FROM articles WHERE type="' + obj.text.lower() + '" LIMIT 9'
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
        self.a_buylist.add_widget(button)


class PosApp(App):

    def build(self):
        return Controller()