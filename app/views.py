from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("kivy_config/kv/views.kv")


class MainScreen(Screen):
    def __init__(self):
        super().__init__()
