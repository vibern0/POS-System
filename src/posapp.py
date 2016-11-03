# -*- coding: utf-8 -*-

import kivy
kivy.require('1.0.5')

from kivy.app import App
from controller.controller import Controller

class PosApp(App):

    def build(self):
        return Controller()
