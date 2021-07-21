from kivy.uix.widget import Widget
from kivy.garden.graph import Graph, MeshLinePlot
from math import sin, cos
from kivy.clock import Clock


class SetGraph(Widget):
    def __init__(self, **kwargs):
        super(SetGraph, self).__init__(**kwargs)

        self.color_red = [1, 0, 0, 1]
        self.color_yellow = [1, 1, 0, 1]

        self.update_graph_time = 1 / 10

        self.plot1 = MeshLinePlot(color=self.color_red)
        self.plot2 = MeshLinePlot(color=self.color_yellow)
        self.max_x_plot = 0


    def start(self):
        '''запуск обновления графика'''
        Clock.unschedule(self.update_graph)
        Clock.schedule_interval(self.update_graph, self.update_graph_time)

    def stop(self):
        Clock.unschedule(self.update_graph)

    def update_points(self):
        pass

    def update_xaxis(self):
        if self.max_x_plot >= 100:
            self.ids["graph_main"].xmax += 1
            self.ids["graph_main"].xmin += 1

    def update_yaxis(self):
        pass

    def update_graph(self, *args):
        self.plot1.points = [(x, sin(x / 10.)) for x in range(0, self.max_x_plot)]
        self.plot2.points = [(x, cos(x / 4)) for x in range(0, self.max_x_plot)]
        self.max_x_plot += 1
        self.graph_main.add_plot(self.plot1)
        self.graph_main.add_plot(self.plot2)
        self.update_xaxis()

    def clear_graph(self):
        self.plot1.points = []
        self.plot2.points = []
        self.max_x_plot = 0
