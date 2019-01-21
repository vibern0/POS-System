# -*- coding: utf-8 -*-

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


class LogoutScreen(BoxLayout):

    def __init__(self, controller, **kwargs):
        super(LogoutScreen, self).__init__(**kwargs)
        self.controller = controller
        self.popup_lougout = Popup(
            title='User Logout',
            content=self,
            auto_dismiss=False,
            size_hint=(None, None),
            size=(400, 170)
        )

        self.popup_lougout.open()

    def answer_no(self):
        self.popup_lougout.dismiss()

    def answer_yes(self):
        self.controller.database.register_logs(self.controller.pos_system.get_user_id(), 0)

        self.controller.a_buylist.clear_widgets()
        self.controller.a_articles.clear_widgets()
        self.controller.a_baroptions.clear_widgets()
        self.controller.a_price.clear_widgets()

        self.popup_lougout.dismiss()

        self.controller.user_login()
