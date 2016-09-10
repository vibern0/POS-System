from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty

class LogoutScreen(BoxLayout):

    root_self = ObjectProperty()

    ###
    def __init__(self, **kwargs):
        super(LogoutScreen, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.add_widget(Label(text='Do you want to logout?'))
        self.bottom_layout = BoxLayout()
        self.add_widget(self.bottom_layout)
        self.bt_no = Button(text='No', on_press = self.answerNo)
        self.bottom_layout.add_widget(self.bt_no)
        self.bt_yes = Button(text='Yes', on_press = self.answerYes)
        self.bottom_layout.add_widget(self.bt_yes)

    ###
    def answerNo(self, obj):
        #
        self.root_self.popup.dismiss()

    ###
    def answerYes(self, obj):
        self.root_self.database.registerLogs(self.root_self.getUserID(), 0)
        #
        self.root_self.a_buylist.clear_widgets()
        self.root_self.a_articles.clear_widgets()
        self.root_self.a_baroptions.clear_widgets()
        self.root_self.a_price.clear_widgets()
        #
        self.root_self.popup.dismiss()
        #
        self.root_self.userLogin()
