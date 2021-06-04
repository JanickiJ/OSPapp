import json
import os

from kivy.animation import Animation
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from screen_helpers.sign_in_screen_string import sign_in_helper
from screen_helpers.sign_up_screen_string import sign_up_helper
from screen_helpers.start_menu_screen_string import start_menu_helper


class StartScreen:
    def __init__(self, app):
        self.app = app
        self.start_screen = Builder.load_string(start_menu_helper)
        self.sign_up_screen = Builder.load_string(sign_up_helper)
        self.log_in_screen = Builder.load_string(sign_in_helper)

    def make_login(self):
        e_mail_saved = ""
        password_saved = ""
        if os.stat('app_data/saved_password.txt').st_size != 0:
            with open('app_data/saved_password.txt') as saved_password_file:
                content = saved_password_file.read()
                json_content = json.loads(content)
                e_mail_saved, password_saved = json_content['email'], json_content['password']
        self.log_in_screen.ids['email_address'].text = e_mail_saved
        self.log_in_screen.ids['password'].text = password_saved

    def sign_in(self, email_address, password):
        if self.app.myfirebase.sign_in(email_address, password):
            self.log_in_screen.ids['message'].text = ""
            if self.log_in_screen.ids['save_password'].active:
                load_data = {'email': email_address, 'password': password}
                with open('app_data/saved_password.txt', 'w') as save_file:
                    json.dump(load_data, save_file)
            else:
                open('app_data/saved_password.txt', 'w').close()
            self.app.menu_screen.make_first_screen()
            self.app.menu_screen.make_third_screen()
            self.app.menu_screen.make_second_screen()

            self.app.screen_manager.switch_to(self.app.menu_screen.screen)

    def reset_password(self, obj):
        if self.reset_textfield.text == "":
            self.app.close_dialog(obj)
            self.app.show_snackbar("Nie podano adresu e-mail")
        else:
            self.app.myfirebase.reset_password(self.reset_textfield.text)
            self.app.close_dialog(obj)
            self.app.show_snackbar("E-mail został wysłany")

    def forgot_password(self):
        self.reset_textfield = MDTextField()
        self.reset_textfield.hint_text = "E-mail"
        self.app.dialog = MDDialog(
            title="Zresetuj hasło",
            type="custom",
            content_cls=self.reset_textfield,
            buttons=[
                MDFlatButton(
                    text="ANULUJ", text_color=self.app.theme_cls.primary_color, on_release=self.app.close_dialog
                ),
                MDFlatButton(
                    text="ZRESETUJ", text_color=self.app.theme_cls.primary_color, on_release=self.reset_password
                )
            ],
        )
        self.app.dialog.open()

    def verification_sent(self, email):
        self.app.dialog = MDDialog(
            title="Zweryfikuj swój e-mail",
            type="custom",
            content_cls=MDLabel(text=f"Link aktywacyjny został wysłany na twój adres e-mail: {email}"),
            buttons=[
                MDFlatButton(
                    text="ZALOGUJ SIĘ", text_color=self.app.theme_cls.primary_color, on_release=self.app.change_to_log
                )
            ]
        )
        self.app.dialog.size_hint = 1, None
        self.app.dialog.open()

    def log_animation(self, *args):
        up_animation = Animation(pos_hint={'center_y': 1.16})
        up_animation.start(args[0])
        down_animation = Animation(pos_hint={'center_y': 0.85})
        down_animation.start(args[1])
        icon_animation = Animation(pos_hint={'center_y': 0.8})
        icon_animation += Animation(pos_hint={'center_y': 0.85})
        icon_animation.start(args[2])
        text_animation = Animation(opacity=0, duration=0.5)
        text_animation += Animation(opacity=1)
        text_animation.start(args[3])

    def sing_up_next_1(self):
        self.sign_up_screen.ids.slide.load_next(mode="next")
        self.sign_up_screen.ids.progress.value = 100
        self.sign_up_screen.ids.name.icon = 'check-decagram'

    def sing_up_next_2(self):
        self.sign_up_screen.ids.slide.load_next(mode="next")
        self.sign_up_screen.ids.progress1.value = 100
        self.sign_up_screen.ids.contact.icon = 'check-decagram'

    def sing_up_previous_1(self):
        self.sign_up_screen.ids.slide.load_previous()
        self.sign_up_screen.ids.progress.value = 0
        self.sign_up_screen.ids.name.icon = 'numeric-1-circle'

    def sing_up_previous_2(self):
        self.sign_up_screen.ids.slide.load_previous()
        self.sign_up_screen.ids.progress1.value = 0
        self.sign_up_screen.ids.contact.icon = 'numeric-2-circle'