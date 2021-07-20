from kivy.app import App
from gui.pages.MVP.MVPPage import MVPPage


class MainApp(App):
    def build(self):
        return MVPPage().build()


MainApp().run()
