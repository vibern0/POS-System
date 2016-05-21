from kivy.app import App

class InterfaceApp(App):
    def build(self):
        pass

    def on_touch_down(self, touch):
        print("Touch")
