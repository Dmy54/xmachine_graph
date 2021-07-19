from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from matplotlib import pyplot as plt
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.garden.graph import Graph, MeshLinePlot
from math import sin, cos
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty
import numpy as np


class SetGraph(Widget):
    def __init__(self, **kwargs):
        super(SetGraph, self).__init__(**kwargs)
        # self.graph_test = ObjectProperty(None)
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
            self.ids["graph_test"].xmax += 1
            self.ids["graph_test"].xmin += 1

    def update_yaxis(self):
        pass

    def update_graph(self, *args):
        self.plot1.points = [(x, sin(x / 10.)) for x in range(0, self.i)]
        self.plot2.points = [(x, cos(x / 4)) for x in range(0, self.i)]
        self.i += 1
        self.graph_test.add_plot(self.plot1)
        self.graph_test.add_plot(self.plot2)
        self.update_xaxis()


class MVPPage(Widget):

    def build(self):
        disp = SetGraph()
        return self

class MainApp(App):
    def build(self):
        return MVPPage().build()



# plt.plot([1, 23, 2, 4])
# plt.ylabel('some numbers')
#
#
# class MainGraph(FigureCanvasKivyAgg):
#     def __init__(self, **kwargs):
#         super().__init__(plt.gcf(), **kwargs)
#
#     def update(self, *args):
#         plt.plot(self.line, self.line)
#         self.i += 1
#         self.line.append(self.i)
#         canvas.draw_idle()
#
#




#
# fig, ax = plt.subplots()
# canvas = fig.canvas
#
# class MainApp(App):
#     def build(self):
#         box = BoxLayout()
#         self.i = 0
#         self.line = [self.i]
#         box.add_widget(canvas)
#         plt.show()
#         Clock.schedule_interval(self.update, 1)
#         return box
#
#     def update(self, *args):
#         plt.plot(self.line, self.line)
#         self.i += 1
#         self.line.append(self.i)
#         canvas.draw_idle()

MainApp().run()