from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class LoginScreen(BoxLayout):

    root_self = ObjectProperty()

    ###
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        ###
        self.grid = GridLayout()
        self.grid.cols = 2
        self.grid.add_widget(Label(text='User Name'))
        self.grid.username = TextInput(multiline=False)
        self.grid.add_widget(self.grid.username)
        self.grid.add_widget(Label(text='password'))
        self.grid.password = TextInput(password=True, multiline=False)
        self.grid.add_widget(self.grid.password)
        ###
        self.options = BoxLayout()
        self.options.size_hint_y = 0.5
        self.options.bt_cancel = Button(text='Cancel')
        self.options.add_widget(self.options.bt_cancel)
        self.options.bt_login = Button(text='Login')
        self.options.bt_login.bind(on_press=self.bt_login_clicked)
        self.options.add_widget(self.options.bt_login)
        ###
        self.add_widget(self.grid)
        self.add_widget(self.options)

    ###
    def bt_login_clicked(self, obj):
        print(self.grid.username.text)
        
        self.root_self.loadBarOptions()
        self.root_self.loadMainWindow()

        self.root_self.popup.dismiss()

    ###
    def bt_cancel_clicked(self, obj):
        self.root_self.popup.dismiss()