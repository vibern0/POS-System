# -*- coding: utf-8 -*-

import kivy
kivy.require('1.0.5')

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

import sys
sys.path.append('./../src/')

from pos.pos_system import POS, Item
from database.db import Database
from interface.buttonex import ButtonEx
from interface.loginscreen import LoginScreen
from interface.logoutscreen import LogoutScreen


class BarOptions(BoxLayout):

    bt_newlist = ObjectProperty()
    bt_clearlist = ObjectProperty()
    bt_finishlist = ObjectProperty()
    bt_next = ObjectProperty()
    bt_previous = ObjectProperty()

    pos_system = ObjectProperty()

    ###
    def __init__(self, **kwargs):
        super(BarOptions, self).__init__(**kwargs)
        self.bt_newlist.enabled = True
        self.bt_clearlist.enabled = False
        self.bt_finishlist.enabled = False
        self.bt_next.enabled = False
        self.bt_previous = False

    ###
    def startNewBuyList(self, instance):
        self.pos_system.newBuyList()
        self.bt_clearlist.enabled = True
        self.bt_finishlist.enabled = True
        self.bt_newlist.enabled = False

    ###
    def clearBuyList(self):
        self.a_buylist.clear_widgets()
        self.pos_system.getBuyList().clearList()
        self.updateTotalPrice()

    ###
    def finishBuyList(self):
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
    def nextPage(self):
        self.menu_page = self.menu_page + 1
        ###self.openNewMenu(obj = obj)

    ###
    def previousPage(self):
        self.menu_page = self.menu_page - 1
        ###
