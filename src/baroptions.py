# -*- coding: utf-8 -*-

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

kivy.require('1.0.5')


class BarOptions(BoxLayout):

    bt_newlist = ObjectProperty()
    bt_clearlist = ObjectProperty()
    bt_finishlist = ObjectProperty()
    bt_next = ObjectProperty()
    bt_previous = ObjectProperty()

    pos_system = ObjectProperty()

    def __init__(self, **kwargs):
        super(BarOptions, self).__init__(**kwargs)
        self.bt_newlist.enabled = True
        self.bt_clearlist.enabled = False
        self.bt_finishlist.enabled = False
        self.bt_next.enabled = False
        self.bt_previous = False
        self.menu_page = 0

    def start_new_buy_list(self, instance):
        self.pos_system.new_buy_list()
        self.bt_clearlist.enabled = True
        self.bt_finishlist.enabled = True
        self.bt_newlist.enabled = False

    def clear_buy_list(self):
        self.a_buylist.clear_widgets()
        self.pos_system.get_buy_list().clear_list()
        self.update_total_price()

    def finish_buy_list(self):
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text='Do you really want to finish?'))
        button_confirm = Button(text='Finish')
        button_confirm.bind(on_press=self.register_buy)
        button_cancel = Button(text='Cancel')
        button_cancel.bind(on_press=self.dismiss)
        options = BoxLayout()
        options.add_widget(button_confirm)
        options.add_widget(button_cancel)
        content.add_widget(options)

        popup_finish = Popup(
            title='Finish Buy List',
            content=content,
            size_hint=(None, None),
            size=(400, 100)
        )

        popup_finish.open()

    def next_page(self):
        self.menu_page = self.menu_page + 1

    def previous_page(self):
        self.menu_page = self.menu_page - 1
