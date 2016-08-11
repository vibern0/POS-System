from kivy.uix.button import Button
from kivy.properties import BooleanProperty

from pos_system import Item

class Article(Button, Item):
    enabled = BooleanProperty(True)

    def abc(self):
        pass
