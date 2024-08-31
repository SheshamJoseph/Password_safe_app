from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from app.views import MainScreen


class PasswordSafeApp(MDApp):
    def build(self):
        sm = ScreenManager()
        # sm.add_widget(MainScreen(name="main"))
        sm.add_widget(MainScreen())
        # other screens
        return sm


if __name__ == "__main__":
    PasswordSafeApp().run()
