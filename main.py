from datetime import datetime

import kivymd.uix.list
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDTimePicker, MDDatePicker
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, IconRightWidget, ThreeLineAvatarIconListItem, \
    ThreeLineIconListItem, TwoLineAvatarListItem, OneLineIconListItem, TwoLineIconListItem, CheckboxRightWidget
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import IRightBodyTouch
from OspApp.myfirebase import MyFirebase
from helpers import sign_up_helper, \
    log_in_helper, start_app_menu_helper
from menu_screen import menu_screen_helper


Window.size = (300, 500)


class OSPApp(MDApp):
    def change_screen(self, name):
        self.screen_manager.current = name

    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.myfirebase = MyFirebase()
        self.start_screen = Builder.load_string(start_app_menu_helper)
        self.sign_up_screen = Builder.load_string(sign_up_helper)
        self.log_in_screen = Builder.load_string(log_in_helper)
        self.menu_screen = Builder.load_string(menu_screen_helper)
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
        if self.username.text == "":
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

    def sign_in(self, email_address, password):
        if self.myfirebase.sign_in(email_address, password):
            self.screen_manager.switch_to(self.menu_screen)
            self.make_third_screen()

        else:
            # dopisac obsługe złych danych
            print("Incorrect data")

    def nawigation_draw(self):
        print("nawigation draw")

#dopisane
#obsługa kalendarza i zegara
    def on_save_data_picker(self, value):
        self.current_button_id.text = str(value)

    def on_cancel_data_picker(self, instance, value):
        print(instance, value)

    def show_date_picker(self, id):
        self.current_button_id = id
        date_dialog = MDDatePicker(self.on_save_data_picker)
        date_dialog.open()

    def show_time_picker(self,id):
        self.current_button_id = id
        time_dialog = MDTimePicker()
        time_dialog.set_time(datetime.now())
        time_dialog.bind(time=self.on_save_time_picker)
        time_dialog.open()

    def on_save_time_picker(self, instance, value):
        self.current_button_id.text = str(value)

    def on_cancel_time_picker(self, instance, value):
        print(instance, value)

#tworzenie listy załogi na 3 screen
    def make_third_screen(self):
        for member in self.myfirebase.get_crew_members():
            permissions = ""
            if member[1]: permissions += "dow. akcji, "
            if member[2]: permissions += "kierowca, "
            if member[3]: permissions += "dow. sekcji"
            to_add = ThreeLineIconListItem(text=member[0], secondary_text="Uprawnienia:", tertiary_text=permissions)
            to_add.tertiary_font_style = 'Caption'
            to_add.secondary_font_style = 'Caption'
            to_add.add_widget(IconLeftWidget(icon='fire'))
            self.menu_screen.ids.crew_members.add_widget(to_add)

#tworzenie wyskakujacej listy załogi na 1 screen
#nie działa on_action czyli jak sie kliknie chcebox to sie nic nie dzieje
    def show_members_with_permission(self, permission):
        items =[]
        _touchable_widgets = ListProperty()
        for member in self.myfirebase.get_members_with_permission(permission):
            item = OneLineIconListItem(text=member)
            check = CheckboxRightWidget()
            check.active = False
            check.on_active(self.on_active())
            item.add_widget(check)
            items.append(item)

        self.dialog = MDDialog(
            title="Wybierz załoge",
            type="simple",
            items=items,
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color
                ),
                MDFlatButton(
                    text="ACCEPT", text_color=self.theme_cls.primary_color
                ),
            ],
        )

        self.dialog.size_hint = 1, None
        self.dialog.open()

    def on_active(self):
        print("DUUDUD")

if __name__ == '__main__':
    OSPApp().run()
