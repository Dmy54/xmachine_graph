from kivy.uix.widget import Widget
from gui.composed_components.Indicator.Indicator import Indicator

class MainPage(Widget):

    def build(self):
        self.ids["real_force"].set_text('1.0', 'real force')
        self.ids["exp_force"].set_text('1.0', 'exp_force')
        self.ids["rel_force"].set_text('1.0', 'rel_force')
        self.ids["k_f_scale"].set_text('1.0', 'k_f_scale')
        return self
