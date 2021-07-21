from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, NumericProperty


class VolumeLevel(BoxLayout):
    color = ListProperty([1, 0, 0, 1])
    level = NumericProperty(0)

    def __init__(self, **kwargs):
        super(VolumeLevel, self).__init__(**kwargs)

    def change_level(self, level):
        self.level = level