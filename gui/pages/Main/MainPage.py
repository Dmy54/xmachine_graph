from kivy.uix.widget import Widget
from gui.composed_components.Indicator.Indicator import Indicator
from kivy.clock import Clock
import random

class MainPage(Widget):

    def build(self):
        Clock.schedule_interval(self.work_imitation, 1/20)
        return self

    def work_imitation(self, *args):
        self.ids["real_force"].level = random.uniform(0, 1)
        self.ids["exp_force"].level = random.uniform(0, 1)
        self.ids["rel_force"].level = random.uniform(0, 1)
        self.ids["k_f_scale"].level = random.uniform(0, 1)