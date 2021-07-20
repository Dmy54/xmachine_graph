from kivy.uix.widget import Widget
from gui.components.SetGraph.SetGraph import SetGraph

class MVPPage(Widget):
    def build(self):
        return self

    def clear_main_graph(self):
        self.ids['graph_x'].clear_graph()

    def start_main_graph(self):
        self.ids['graph_x'].start()