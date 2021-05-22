from datetime import datetime
import os
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDTimePicker, MDDatePicker
from kivymd.uix.list import IconLeftWidget, \
    ThreeLineIconListItem, OneLineIconListItem, CheckboxLeftWidget, OneLineAvatarIconListItem
from kivymd.uix.textfield import MDTextField
import json
from myfirebase import MyFirebase
from helpers import sign_up_helper, \
    log_in_helper, start_app_menu_helper
from menu_screen import menu_screen_helper
from update_report_screen import update_report_screen_helper
from kivymd.uix.label import MDLabel


class OSPApp(MDApp):

    def change_screen(self, name):
        self.screen_manager.current = name

    def build(self):
        self.chosen_members = []
        self.theme_cls.primary_palette = 'Red'
        self.myfirebase = MyFirebase()
        self.start_screen = Builder.load_string(start_app_menu_helper)
        self.sign_up_screen = Builder.load_string(sign_up_helper)
        self.log_in_screen = Builder.load_string(log_in_helper)
        self.menu_screen = Builder.load_string(menu_screen_helper)
        self.screen_manager = ScreenManager()
        self.screen_manager.switch_to(self.start_screen)
        return self.screen_manager

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
        anim = Animation(opacity=0, duration=0.5)
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

    def change_to_start(self):
        self.screen_manager.switch_to(self.start_screen)

    def change_to_login(self):
        e_mail_saved = ""
        password_saved = ""
        if os.stat('saved_password.txt').st_size != 0:
            with open('saved_password.txt') as saved_password_file:
                content = saved_password_file.read()
                json_content = json.loads(content)
                e_mail_saved, password_saved = json_content['email'], json_content['password']
        self.log_in_screen.ids['email_address'].text = e_mail_saved
        self.log_in_screen.ids['password'].text = password_saved
        self.screen_manager.switch_to(self.log_in_screen)

    def change_to_second_menu(self):
        self.screen_manager.switch_to(self.menu_screen)

    def change_to_signup(self):
        self.screen_manager.switch_to(self.sign_up_screen)

    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def navigation_draw(self):
        print("Navigation")

    def sign_in(self, email_address, password):
        if self.myfirebase.sign_in(email_address, password):
            self.log_in_screen.ids['message'].text = ""
            if self.log_in_screen.ids['save_password'].active:
                load_data = {'email': email_address, 'password': password}
                with open('saved_password.txt', 'w') as save_file:
                    json.dump(load_data, save_file)
            else:
                open('saved_password.txt', 'w').close()
            self.make_first_screen()
            self.make_third_screen()
            self.make_second_screen()

            self.screen_manager.switch_to(self.menu_screen)

    def nawigation_draw(self):
        print("nawigation draw")

    def on_save_data_picker(self, instance, value, date_range):
        self.current_button_id.text = str(value)

    def on_cancel_data_picker(self, instance, value):
        print(instance, value)

    def show_date_picker(self, id):
        self.current_button_id = id
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_data_picker, on_cancel=self.on_cancel_data_picker)
        date_dialog.open()

    def show_time_picker(self, id):
        self.current_button_id = id
        time_dialog = MDTimePicker()
        time_dialog.set_time(datetime.now())
        time_dialog.bind(on_save=self.on_save_time_picker, on_cancel=self.on_cancel_time_picker)
        time_dialog.open()

    def on_save_time_picker(self, instance, value):
        self.current_button_id.text = instance.ids._time_input.ids.hour.text + ":" + instance.ids._time_input.ids.minute.text

    def on_cancel_time_picker(self, instance, value):
        print(instance, value)

    def make_first_screen(self):
        self.menu_screen.ids.toolbar_name.title = self.myfirebase.get_name()
        self.menu_screen.ids.navi_name.text = self.myfirebase.get_name()
        self.menu_screen.ids.navi_address.text = self.myfirebase.get_address()
        self.menu_screen.ids.navi_email.text = self.myfirebase.get_email()

    def make_second_screen(self):
        self.menu_screen.ids.active_reports.clear_widgets()
        active_reports = self.myfirebase.get_active_reports()
        if active_reports:
            for i, report in enumerate(active_reports):
                to_add = OneLineAvatarIconListItem(text=report)
                to_add.add_widget(IconLeftWidget(icon='file-edit', on_release=self.edit_report))
                to_add.add_widget(MDIconButton(icon="trash-can-outline", pos_hint={'center_x': .85, 'center_y': .5},
                                               on_release=self.remove_report_dialog))
                self.menu_screen.ids.active_reports.add_widget(to_add)

    def make_third_screen(self):
        for member in self.myfirebase.get_crew_members():
            permissions = ""
            if member[1]: permissions += "dow. akcji, "
            if member[2]: permissions += "kierowca, "
            if member[3]: permissions += "dow. sekcji"
            if permissions == "": permissions += "brak"
            to_add = ThreeLineIconListItem(text=member[0], secondary_text="Uprawnienia:", tertiary_text=permissions)
            to_add.tertiary_font_style = 'Caption'
            to_add.secondary_font_style = 'Caption'
            to_add.add_widget(IconLeftWidget(icon='fire'))
            self.menu_screen.ids.crew_members.add_widget(to_add)

    def remove_report_dialog(self, obj):
        for list in self.menu_screen.ids.active_reports.children:
            if list.children[0] == obj:
                self.report = list.text

        self.dialog = MDDialog(
            text="Napewno chcesz usunąć raport?",
            buttons=[
                MDFlatButton(
                    text="USUŃ", text_color=self.theme_cls.primary_color, on_release=self.remove_report
                ),
                MDFlatButton(
                    text="ZACHOWAJ", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                ),
            ],
        )
        self.dialog.size_hint = 1, None
        self.dialog.open()

    def edit_report(self, obj):
        for list in self.menu_screen.ids.active_reports.children:
            if list.children[2].children[0] == obj:
                self.report = list.text
        update_report_screen = Builder.load_string(update_report_screen_helper)
        self.myfirebase.show_report(update_report_screen.ids.attributes_list, self.report)
        self.screen_manager.switch_to(update_report_screen)

    def remove_report(self, obj):
        self.myfirebase.remove_report(self.report)
        self.close_dialog(obj)
        self.make_second_screen()

    def show_members_with_permission(self, id, permission):
        self.items = []
        self.current_button_id = id
        _touchable_widgets = ListProperty()
        for member in self.myfirebase.get_members_with_permission(permission):
            item = OneLineIconListItem(text=member)
            check = CheckboxLeftWidget()
            if member in self.chosen_members:
                check.active = True
            else:
                check.active = False
            item.add_widget(check)
            self.items.append(item)

        self.dialog = MDDialog(
            title="Wybierz załoge",
            type="simple",
            items=self.items,
            buttons=[
                MDFlatButton(
                    text="WYCZYŚĆ", text_color=self.theme_cls.primary_color, on_release=self.clear_members
                ),
                MDFlatButton(
                    text="ZAPISZ", text_color=self.theme_cls.primary_color, on_release=self.accept_members
                ),
            ],
        )
        self.dialog.size_hint = 1, None
        self.dialog.open()

    def accept_members(self, obj):
        self.chosen_members.clear()
        for widget in self.dialog.items:
            if widget.children[0].children[0].active:
                self.chosen_members.append(widget.text)
        try:
            self.current_button_id.text = ",".join(self.chosen_members)
        except:
            pass
        self.close_dialog(obj)

    def clear_members(self, obj):
        for widget in self.dialog.items:
            widget.children[0].children[0].active = False
        self.chosen_members.clear()

    def show_snackbar(self, text):
        Snackbar(
            text=text,
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=(
                                Window.width - (dp(10) * 2)
                        ) / Window.width
        ).open()

    def reset_password(self, obj):
        if self.reset_textfield.text == "":
            self.dialog.dismiss()
            self.show_snackbar("Nie podano adresu e-mail")
            return
        self.myfirebase.reset_password(self.reset_textfield.text)
        self.dialog.dismiss()
        self.show_snackbar("E-mail został wysłany")

    def forgot_password(self):
        self.reset_textfield = MDTextField()
        self.reset_textfield.hint_text = "E-mail"
        self.dialog = MDDialog(
            title="Zresetuj hasło",
            type="custom",
            content_cls=self.reset_textfield,
            buttons=[
                MDFlatButton(
                    text="ANULUJ", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                ),
                MDFlatButton(
                    text="ZRESETUJ", text_color=self.theme_cls.primary_color, on_release=self.reset_password
                )
            ],
        )
        self.dialog.open()

    def switch_to_log(self, obj):
        self.screen_manager.switch_to(self.log_in_screen)
        self.dialog.dismiss()

    def verification_sent(self, email):
        self.dialog = MDDialog(
            title="Zweryfikuj swój e-mail",
            type="custom",
            content_cls=MDLabel(text=f"Link aktywacyjny został wysłany na twój adres e-mail: {email}"),
            buttons=[
                MDFlatButton(
                    text="ZALOGUJ SIĘ", text_color=self.theme_cls.primary_color, on_release=self.switch_to_log
                )
            ]
        )
        self.dialog.size_hint = 1, None
        self.dialog.open()

    def show_developers_info(self):
        three_line_list = ThreeLineIconListItem(text="Ania, Jakub",
                                                secondary_text="ospapp@gmail.com",
                                                tertiary_text="https://github.com/JanickiJ/OSPapp.git")
        three_line_list.add_widget(
            IconLeftWidget(icon='fire', text_color=self.theme_cls.primary_color, theme_text_color="Custom"))
        self.dialog = MDDialog(
            title="Twórcy aplikacji",
            type="custom",
            content_cls=three_line_list,
            buttons=[
                MDFlatButton(
                    text="OK", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                )
            ]
        )
        self.dialog.size_hint = 1, None
        self.dialog.open()

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        if tab_text == "Nowy raport":
            i = 0
        elif tab_text == "Aktywne raporty":
            i = 1
        else:
            i = 2
        self.menu_screen.ids.carousel.load_slide(self.menu_screen.ids.carousel.slides[i])

    def on_index(self, instance, value):
        self.menu_screen.ids['tabs'].ids.carousel.load_slide(self.menu_screen.ids['tabs'].ids.carousel.slides[value])


class Tab1(MDFloatLayout, MDTabsBase):
    pass


if __name__ == '__main__':
    OSPApp().run()
