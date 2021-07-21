from kivy.app import App
from gui.pages.MVP.MVPPage import MVPPage
from gui.pages.Main.MainPage import MainPage


class MainApp(App):
    def build(self):
        return MainPage().build()


MainApp().run()
