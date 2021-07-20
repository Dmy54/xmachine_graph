from kivy.uix.widget import Widget
from kivy.garden.graph import Graph, MeshLinePlot
from math import sin, cos
from kivy.clock import Clock


class SetGraph(Widget):
    def __init__(self, **kwargs):
        super(SetGraph, self).__init__(**kwargs)

        self.plot1 = MeshLinePlot(color=[1, 0, 0, 1])
        self.plot2 = MeshLinePlot(color=[1, 1, 0, 1])
        self.i = 10
        self.start()

    def start(self):
        Clock.schedule_interval(self.update_graph, 1 / 10)

    def stop(self):
        Clock.unschedule(self.update_graph)

    def update_points(self):
        pass

    def update_xaxis(self):
        if self.i >= 100:
            self.ids["graph_main"].xmax += 1
            self.ids["graph_main"].xmin += 1

    def update_yaxis(self):
        pass

    def update_graph(self, *args):
        self.plot1.points = [(x, sin(x / 10.)) for x in range(0, self.i)]
        self.plot2.points = [(x, cos(x / 4)) for x in range(0, self.i)]
        self.i += 1
        self.graph_main.add_plot(self.plot1)
        self.graph_main.add_plot(self.plot2)
        self.update_xaxis()