from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.tab import MDTabsBase

from menu_screen_class import MenuScreen
from myfirebase import MyFirebase
from start_screen_class import StartScreen


class OSPApp(MDApp):

    def __init__(self):
        super().__init__()
        self.myfirebase = MyFirebase()
        self.dialog = MDDialog()
        self.report = ""
        self.theme_cls.primary_palette = 'Red'
        self.start_screen = StartScreen(self)
        self.menu_screen = MenuScreen(self)
        self.screen_manager = ScreenManager()

    def build(self):
        self.screen_manager.switch_to(self.start_screen.start_screen)
        return self.screen_manager

    def change_screen(self, name):
        self.screen_manager.current = name

    def change_to_start(self):
        self.screen_manager.switch_to(self.start_screen.start_screen)

    def change_to_login(self):
        self.start_screen.make_login()
        self.screen_manager.switch_to(self.start_screen.log_in_screen)

    def change_to_second_menu(self):
        self.screen_manager.switch_to(self.menu_screen.screen)

    def change_to_sign_up(self):
        self.screen_manager.switch_to(self.start_screen.sign_up_screen)

    def change_to_log(self, obj):
        self.screen_manager.switch_to(self.start_screen.log_in_screen)
        self.dialog.dismiss()

    def show_snackbar(self, text):
        Snackbar(
            text=text,
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=(Window.width - (dp(10) * 2)) / Window.width
        ).open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

class Tab1(MDFloatLayout, MDTabsBase):
    pass
