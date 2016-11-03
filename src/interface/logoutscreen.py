from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

class LogoutScreen(BoxLayout):

    root_self = ObjectProperty()

    ###
    def __init__(self, **kwargs):
        super(LogoutScreen, self).__init__(**kwargs)
        #defined on .kv file

    ###
    def answerNo(self):
        #
        self.root_self.popup.dismiss()

    ###
    def answerYes(self):
        self.root_self.database.registerLogs(self.root_self.pos_system.getUserID(), 0)
        #
        self.root_self.a_buylist.clear_widgets()
        self.root_self.a_articles.clear_widgets()
        self.root_self.a_baroptions.clear_widgets()
        self.root_self.a_price.clear_widgets()
        #
        self.root_self.popup.dismiss()
        #
        self.root_self.userLogin()
