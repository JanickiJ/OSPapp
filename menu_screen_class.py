from kivy.lang import Builder
from screen_helpers.menu_screen_string import menu_screen_helper


class MenuScreen:
    def __init__(self, screen):
        self.screen = Builder.load_string(menu_screen_helper)


    def on_tab_switch(self, *args):
        if args[3] == "Nowy raport":
            i = 0
        elif args[3] == "Aktywne raporty":
            i = 1
        else:
            i = 2
        self.screen.ids.carousel.load_slide(self.screen.ids.carousel.slides[i])
