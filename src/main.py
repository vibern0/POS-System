import kivy
kivy.require('1.0.7')

from g_interface import InterfaceApp
from pos_system import *

if __name__ == '__main__':
    InterfaceApp().run()

p = POS()
p.newBuyList()
b = p.getBuyList()
b.addItem(Item("apple", 5, 1))
b.addItem(Item("orange", 4, 1))
b.addItem(Item("banana", 6, 2))

p.printBuyList()
