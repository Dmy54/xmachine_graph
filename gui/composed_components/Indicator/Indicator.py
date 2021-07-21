from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
from gui.components.LabelWithBorder.LabelWithBorder import LabelWithBorder
from gui.components.VolumeLevel.VolumeLevel import VolumeLevel
from kivy.clock import Clock

class Indicator(BoxLayout):
    header_label_text = StringProperty("0.0")
    footer_label_text = StringProperty("-")
    level = NumericProperty(0.0)
    volume_color = ListProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        self.volume_update_timer = 1/20

        super(Indicator, self).__init__(**kwargs)
        Clock.schedule_interval(self.update_volume_level, self.volume_update_timer)

    def set_text(self, head, floor):
        self.header_label_text = head
        self.footer_label_text = floor

    def update_volume_level(self, *args):
        self.ids["volume"].change_level(self.level)
