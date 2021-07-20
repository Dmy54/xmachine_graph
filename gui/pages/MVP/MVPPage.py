from kivy.uix.widget import Widget
from gui.components.SetGraph.SetGraph import SetGraph

class MVPPage(Widget):
    def build(self):
        return self

    def hello(self):
        self.ids['hello_button'].text = 'hello'