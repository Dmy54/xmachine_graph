from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from gui.components.LabelWithBorder.LabelWithBorder import LabelWithBorder

class Indicator(BoxLayout):
    header_label_text = StringProperty("0.0")
    floor_label_text = StringProperty("-")

    def __init__(self, **kwargs):
        super(Indicator, self).__init__(**kwargs)

    def set_text(self, head, floor):
        self.header_label_text = head
        self.floor_label_text = floor
