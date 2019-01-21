# -*- coding: utf-8 -*-

import kivy

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from pos_system import POS, Item
from db import Database
from buttonex import ButtonEx
from loginscreen import LoginScreen
from logoutscreen import LogoutScreen
from baroptions import BarOptions

kivy.require('1.0.5')

# from kivy.config import Config
# Config.set('graphics', 'fullscreen', 'auto')

APPERTIZERS_NAME = 'Appetizers'
MEAT_NAME = 'Meat'
FISH_NAME = 'Fish'
VEGAN_NAME = 'Vegan'
DRINKS_NAME = 'Drinks'
DESSERT_NAME = 'Dessert'


class Controller(FloatLayout):

    a_buylist = ObjectProperty()
    a_articles = ObjectProperty()
    a_baroptions = ObjectProperty()
    a_price = ObjectProperty()

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.pos_system = POS()
        self.database = Database()
        self.baroptions = BarOptions(pos_system=self.pos_system)
        self.atual_menu = 0
        self.menu_page = 0
        self.user_login()

    def register_logs(self, log_type):
        self.database.register_logs(self.pos_system.get_user_id(), log_type)

    def user_login(self):
        LoginScreen(controller=self)

    def user_logout(self, instance):
        LogoutScreen(controller=self)

    def load_main_window(self):

        self.atual_menu = 0
        op_n = 1
        main_options = [APPERTIZERS_NAME, MEAT_NAME, FISH_NAME, VEGAN_NAME, DRINKS_NAME, DESSERT_NAME]

        self.a_articles.clear_widgets()

        for op in main_options:
            button = Button(text=op)
            button.bind(on_press=self.open_new_menu)
            op_n = op_n + 1
            self.a_articles.add_widget(button)

        for a in range(op_n-1, 9):
            self.a_articles.add_widget(Label(text=''))

        self.bt_next.enabled = False
        self.bt_previous.enabled = False

        if self.pos_system.get_buy_list() is None:
            self.bt_newlist.enabled = True
            self.bt_clearlist.enabled = False
            self.bt_finishlist.enabled = False

        self.menu_page = 0

    def load_bar_options(self):
        self.a_baroptions.add_widget(Button(text='Close Session', on_press=self.user_logout))
        self.bt_newlist = ButtonEx(text = 'New List', on_press=self.baroptions.start_new_buy_list)
        self.a_baroptions.add_widget(self.bt_newlist)
        self.bt_clearlist = ButtonEx(text = 'Clear List', on_press=self.baroptions.clear_buy_list)
        self.a_baroptions.add_widget(self.bt_clearlist)
        self.bt_finishlist = ButtonEx(text = 'Finish List', on_press=self.baroptions.finish_buy_list)
        self.a_baroptions.add_widget(self.bt_finishlist)
        self.bt_next = ButtonEx(text = 'Next', on_press = self.baroptions.next_page)
        self.a_baroptions.add_widget(self.bt_next)
        self.bt_previous = ButtonEx(text = 'Previous', on_press = self.baroptions.previous_page)
        self.a_baroptions.add_widget(self.bt_previous)
        self.a_baroptions.add_widget(Button(text = 'Menu', on_press = self.load_main_window))

    def open_new_menu(self, instance):
        op_n = 1
        total_rows = 0
        menu_type = ''
        if instance != self.bt_next and instance != self.bt_previous:
            menu_type = instance.text.lower()

        cursor = self.database.load_articles(menu_type, self.menu_page)

        self.a_articles.clear_widgets()

        for row in cursor:
            total_rows = total_rows + 1
            if total_rows > 9:
                break
            button = Button(text=row[1])
            button.bind(on_press=self.add_to_buy_list)
            button.item = Item(id_p=row[0], name=row[1], price=row[2], tax=0.2)
            op_n = op_n + 1
            self.a_articles.add_widget(button)

        for a in range(op_n-1, 9):
            self.a_articles.add_widget(Label(text=''))

        self.bt_next.enabled = (total_rows > 9)
        self.bt_previous.enabled = (self.menu_page > 0)

    def add_to_buy_list(self, instance):
        if self.pos_system.get_buy_list() is None:
            popup = Popup(
                title='No Buy List',
                content=Label(text='You need to start a new list!'),
                size_hint=(None, None),
                size=(400, 100)
            )
            popup.open()
            return

        button = Button(text=instance.text, size_hint_y = None, height = 40)
        button.bind(on_press=self.remove_from_buy_list)
        self.a_buylist.add_widget(button)
        self.pos_system.get_buy_list().add_item(instance.item)
        self.update_total_price()

    def remove_from_buy_list(self, instance):
        self.a_buylist.remove_widget(instance)
        self.pos_system.get_buy_list().remove_item(item_name = instance.text)
        self.update_total_price()

    def register_buy(self, instance):
        self.database.register_buy(self.pos_system.get_buy_list(), 5533, self.pos_system.get_username())

        self.clear_buy_list()
        self.pos_system.close_buy_list();
        self.bt_clearlist.enabled = False
        self.bt_finishlist.enabled = False
        self.bt_newlist.enabled = True
        self.popup.dismiss()

    def update_total_price(self):
        self.a_price.label_price.text = str(self.pos_system.get_buy_list().get_total_price()) + '€'
