from kivy.app import App
from kivy.uix.widget import Widget
from gui.components.VolumeLevel.VolumeLevel import VolumeLevel
from kivy.clock import Clock
import random

class TestPage(Widget):
    def build(self):
        Clock.schedule_interval(self.update, 1 / 20)
        return self

    def update(self, *args):
        self.ids["volume"].change_level(random.uniform(0, 1))



class TestApp(App):
    def build(self):
        return TestPage().build()


TestApp().run()
