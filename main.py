from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, ThreeLineListItem, ThreeLineAvatarListItem, OneLineListItem
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivymd.uix.datatables import MDDataTable
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from helpers import username_helper, list_helper, screen_helper, navigation_helper, sign_up_helper, \
    screen_change_helper, log_in_helper, start_app_menu_helper

from kivy.core.window import Window
import requests
import json
from myfirebase import MyFirebase

Window.size = (300, 500)


class OSPApp(MDApp):
    def change_screen(self, name):
        self.screen_manager.current = name

    def build(self):
        self.myfirebase = MyFirebase()
        self.start_screen = Builder.load_string(start_app_menu_helper)
        self.sign_up_screen = Builder.load_string(sign_up_helper)
        self.log_in_screen = Builder.load_string(log_in_helper)

        self.screen_manager = ScreenManager()
        self.screen_manager.switch_to(self.start_screen)
        # kv=Builder.load_string(sign_up_helper)
        return self.screen_manager
        # self.theme_cls.primary_palette = 'Red'
        # self.theme_cls.primary_palette="Yellow"
        # self.theme_cls.primary_hue="A700"
        # self.theme_cls.theme_style="Dark"
        # label=MDLabel(text='Hello World!',halign='center',theme_text_color='Custom',text_color=(142.0/255.0, 174/255.0, 165/255.0,1),
        # font_style='Caption')
        # icon_label=MDIcon(icon='fire-truck',halign='center')
        # screen=Screen()
        # btn_flat=MDRectangleFlatButton(text='Hello World!',pos_hint={'center_x':0.5,'center_y':0.5})
        # icon_button=MDFloatingActionButton(icon='fire-truck',pos_hint={'center_x':0.5,'center_y':0.5})
        # username=MDTextField(text='Enter username',pos_hint={'center_x':0.5,'center_y':0.5},size_hint_x=None,width=300)
        # self.username=Builder.load_string(username_helper)
        # button=MDRectangleFlatButton(text='Show',pos_hint={'center_x':0.5,'center_y':0.4},
        # on_release=self.show_data)
        # screen.add_widget(self.username)
        # screen.add_widget(button)
        # list_view=MDList()
        # for i in range (20):
        #     image=ImageLeftWidget(source="cute.jpg")
        #    items=ThreeLineAvatarListItem(text='Item '+str(i),secondary_text="Hello world",tertiary_text="Third text")
        #    items.add_widget(image)
        #    list_view.add_widget(items)
        # scroll=ScrollView()
        # scroll.add_widget(list_view)
        # screen.add_widget(scroll)
        # screen=Builder.load_string(list_helper)
        # screen = Screen()
        # table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                     size_hint=(0.9, 0.6),
        #                     check=True,
        #                     rows_num=10,
        #                     column_data=[
        #                         ("No.", dp(18)),
        #                         ("Food", dp(20)),
        #                         ("Calories", dp(20))
        #                     ],
        #                     row_data=[
        #                         ("1", "Burger", "300"),
        #                         ("2", "Oats", "300"),
        #                         ("3", "Oats", "300"),
        #                         ("4", "Oats", "300"),
        #                         ("5", "Oats", "300"),
        #                         ("6", "Oats", "300"),
        #                         ("7", "Oats", "300"),
        #                         ("8", "Oats", "300"),
        #                         ("9", "Oats", "300"),
        #                     ]
        #                     )
        # table.bind(on_check_press=self.check_press)
        # table.bind(on_row_press=self.row_press)
        # screen = Builder.load_string(sign_up)
        # return screen

    def anim(self, widget):
        anim = Animation(pos_hint={'center_y': 1.16})
        anim.start(widget)

    def anim1(self, widget):
        anim = Animation(pos_hint={'center_y': 0.85})
        anim.start(widget)

    def icons(self, widget):
        anim = Animation(pos_hint={'center_y': 0.8})
        anim += Animation(pos_hint={'center_y': 0.85})
        anim.start(widget)

    def text(self, widget):
        anim = Animation(opacity=0, duration=2)
        anim += Animation(opacity=1)
        anim.start(widget)

    def next(self):
        self.sign_up_screen.ids.slide.load_next(mode="next")
        self.sign_up_screen.ids.progress.value = 100
        self.sign_up_screen.ids.name.icon = 'check-decagram'
        self.sign_up_screen.ids.progress.color = 1, 0, 0, 1

    def next1(self):
        self.sign_up_screen.ids.slide.load_next(mode="next")
        self.sign_up_screen.ids.progress1.value = 100
        self.sign_up_screen.ids.progress1.color = 1, 0, 0, 1
        self.sign_up_screen.ids.contact.icon = 'check-decagram'

    def previous(self):
        self.sign_up_screen.ids.slide.load_previous()
        self.sign_up_screen.ids.name.text_color = 1, 0, 0, 1
        self.sign_up_screen.ids.Name.text_color = 1, 0, 0, 1
        self.sign_up_screen.ids.progress.value = 0
        self.sign_up_screen.ids.progress.color = 0, 0, 0, 1
        self.sign_up_screen.ids.name.icon = 'numeric-1-circle'

    def previous1(self):
        self.sign_up_screen.ids.slide.load_previous()
        self.sign_up_screen.ids.contact.text_color = 1, 0, 0, 1
        self.sign_up_screen.ids.Contact.text_color = 1, 0, 0, 1
        self.sign_up_screen.ids.progress1.value = 0
        self.sign_up_screen.ids.progress1.color = 0, 0, 0, 1
        self.sign_up_screen.ids.contact.icon = 'numeric-2-circle'

    def show_data(self, obj):
        if self.username.text is "":
            check_string = "Please enter a username"
        else:
            check_string = self.username.text + " does not exist"
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Username check', text=check_string, size_hint=(0.7, 1),
                               buttons=[close_button, more_button])

        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def change_to_login(self):
        self.screen_manager.switch_to(self.log_in_screen)

    def change_to_signup(self):
        self.screen_manager.switch_to(self.sign_up_screen)

    # def on_start(self):
    # for i in range(20):
    # items=OneLineListItem(text='Item '+str(i))
    # self.root.ids.container.add_widget(items)
    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def navigation_draw(self):
        print("Navigation")


if __name__ == '__main__':
    OSPApp().run()
