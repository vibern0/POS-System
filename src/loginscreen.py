# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button


class LoginScreen(BoxLayout):

    username = Button()
    password = Button()

    def __init__(self, controller, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.controller = controller
        self.popup_login = Popup(
            title='User Login',
            content=self,
            auto_dismiss=False,
            size_hint=(None, None),
            size=(400, 170)
        )

        self.popup_login.open()

    def bt_login(self):
        row = self.controller.database.is_valid_login(self.username.text, self.password.text)

        if row is None:
            content = Label(text='Username or Password incorrect!')
            popup_error = Popup(
                title='User Login',
                content=content,
                size_hint=(None, None),
                size=(400, 100)
            )
            popup_error.open()
            return

        self.controller.pos_system.set_username(self.username.text)
        self.controller.pos_system.set_user_id(row[0])
        self.controller.database.register_logs(self.controller.pos_system.get_user_id(), 0)

        self.controller.load_bar_options()
        self.controller.load_main_window()

        self.controller.a_price.label_price = Label(text='0€')
        self.controller.a_price.add_widget(self.controller.a_price.label_price)

        self.popup_login.dismiss()

    def bt_cancel(self):
        self.popup_login.dismiss()
