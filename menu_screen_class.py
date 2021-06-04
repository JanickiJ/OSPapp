from datetime import datetime

from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineIconListItem, IconLeftWidget, OneLineAvatarIconListItem, OneLineIconListItem, \
    CheckboxLeftWidget
from kivymd.uix.picker import MDTimePicker, MDDatePicker

from screen_helpers.menu_screen_string import menu_screen_helper
from screen_helpers.update_report_screen_string import update_report_screen_helper


class MenuScreen:
    def __init__(self, app):
        self.current_button_id = None
        self.app = app
        self.screen = Builder.load_string(menu_screen_helper)
        self.update_screen = Builder.load_string(update_report_screen_helper)
        self.chosen_members = []

    def on_tab_switch(self, *args):
        if args[3] == "Nowy raport":
            i = 0
        elif args[3] == "Aktywne raporty":
            i = 1
        else:
            i = 2
        self.screen.ids.carousel.load_slide(self.screen.ids.carousel.slides[i])

    def on_index(self, instance, value):
        self.screen.ids['tabs'].ids.carousel.load_slide(self.screen.ids['tabs'].ids.carousel.slides[value])

    def show_developers_info(self):
        three_line_list = ThreeLineIconListItem(text="Ania, Jakub",
                                                secondary_text="ospapp@gmail.com",
                                                tertiary_text="https://github.com/JanickiJ/OSPapp.git")
        three_line_list.add_widget(
            IconLeftWidget(icon='fire', text_color=self.app.theme_cls.primary_color, theme_text_color="Custom"))
        self.app.dialog = MDDialog(
            title="Twórcy aplikacji",
            type="custom",
            content_cls=three_line_list,
            buttons=[
                MDFlatButton(
                    text="OK", text_color=self.app.theme_cls.primary_color, on_release=self.app.close_dialog
                )
            ]
        )
        self.app.dialog.size_hint = 1, None
        self.app.dialog.open()

    def make_first_screen(self):
        self.screen.ids.toolbar_name.title = self.app.myfirebase.get_name()
        self.screen.ids.navi_name.text = self.app.myfirebase.get_name()
        self.screen.ids.navi_address.text = self.app.myfirebase.get_address()
        self.screen.ids.navi_email.text = self.app.myfirebase.get_email()

    def make_second_screen(self):
        self.screen.ids.active_reports.clear_widgets()
        active_reports = self.app.myfirebase.get_active_reports()
        if active_reports:
            for i, report in enumerate(active_reports):
                to_add = OneLineAvatarIconListItem(text=report)
                to_add.add_widget(IconLeftWidget(icon='file-edit', on_release=self.edit_report))
                to_add.add_widget(MDIconButton(icon="trash-can-outline", pos_hint={'center_x': .8, 'center_y': .5},
                                               on_release=self.remove_report_dialog))
                self.screen.ids.active_reports.add_widget(to_add)

    def make_third_screen(self):
        for member in self.app.myfirebase.get_crew_members():
            permissions = ""
            if member[1]: permissions += "dow. akcji, "
            if member[2]: permissions += "kierowca, "
            if member[3]: permissions += "dow. sekcji"
            if permissions == "": permissions += "brak"
            to_add = ThreeLineIconListItem(text=member[0], secondary_text="Uprawnienia:", tertiary_text=permissions)
            to_add.tertiary_font_style = 'Caption'
            to_add.secondary_font_style = 'Caption'
            to_add.add_widget(IconLeftWidget(icon='fire'))
            self.screen.ids.crew_members.add_widget(to_add)

    def remove_report_dialog(self, obj):
        for l in self.screen.ids.active_reports.children:
            if l.children[0] == obj:
                self.app.report = l.text

        self.app.dialog = MDDialog(
            text="Napewno chcesz usunąć raport?",
            buttons=[
                MDFlatButton(
                    text="USUŃ", text_color=self.app.theme_cls.primary_color, on_release=self.remove_report
                ),
                MDFlatButton(
                    text="ZACHOWAJ", text_color=self.app.theme_cls.primary_color, on_release=self.app.close_dialog
                ),
            ],
        )
        self.app.dialog.size_hint = 1, None
        self.app.dialog.open()

    def remove_report(self, obj):
        self.app.myfirebase.remove_report(self.app.report)
        self.app.close_dialog(obj)
        self.make_second_screen()

    def show_members_with_permission(self, id, permission):
        self.items = []
        self.current_button_id = id
        _touchable_widgets = ListProperty()
        for member in self.app.myfirebase.get_members_with_permission(permission):
            item = OneLineIconListItem(text=member)
            check = CheckboxLeftWidget()
            if member in self.chosen_members:
                check.active = True
            else:
                check.active = False
            item.add_widget(check)
            self.items.append(item)

        self.app.dialog = MDDialog(
            title="Wybierz załoge",
            type="simple",
            items=self.items,
            buttons=[
                MDFlatButton(
                    text="WYCZYŚĆ", text_color=self.app.theme_cls.primary_color, on_release=self.clear_members
                ),
                MDFlatButton(
                    text="ZAPISZ", text_color=self.app.theme_cls.primary_color, on_release=self.accept_members
                ),
            ],
        )
        self.app.dialog.size_hint = 1, None
        self.app.dialog.open()

    def clear_members(self, obj):
        for widget in self.app.dialog.items:
            widget.children[0].children[0].active = False
        self.chosen_members.clear()

    def accept_members(self, obj):
        self.chosen_members.clear()
        for widget in self.app.dialog.items:
            if widget.children[0].children[0].active:
                self.chosen_members.append(widget.text)
        try:
            self.current_button_id.text = ",".join(self.chosen_members)
        except:
            pass
        self.app.close_dialog(obj)

    def edit_report(self, obj):
        for l in self.app.menu_screen.screen.ids.active_reports.children:
            if l.children[2].children[0] == obj:
                self.app.report = l.text
        update_report_screen = Builder.load_string(update_report_screen_helper)
        self.app.myfirebase.show_report(update_report_screen.ids.attributes_list, self.app.report)
        self.app.screen_manager.switch_to(update_report_screen)

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