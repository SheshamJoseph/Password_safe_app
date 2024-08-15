from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    """docstring for MainApp"""

    def build(self):
        return MDLabel(text="Hello world!", halign="center")


if __name__ == "__main__":
    MainApp().run()
