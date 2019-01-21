# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from controller import Controller

kivy.require('1.0.5')


class PosApp(App):
    def build(self):
        return Controller()
