from kivy.app import App
from kivy.uix.widget import Widget
from matplotlib import pyplot as plt
from kivy.garden.matplotlib import FigureCanvasKivyAgg
import numpy as np


class MVPPage(Widget):
    def graph_builder(self):
        signal = [7, 89.6, 45.-56.34]

        signal = np.array(signal)

        # this will plot the signal on graph
        plt.plot(signal)

        # setting x label
        plt.xlabel('Time(s)')

        # setting y label
        plt.ylabel('signal (norm)')
        plt.grid(True, color='lightgray')

        return FigureCanvasKivyAgg(plt.gcf())



class MainApp(App):
    def build(self):
        return MVPPage().graph_builder()


MainApp().run()