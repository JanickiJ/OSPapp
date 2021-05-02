from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, TwoLineIconListItem, IconLeftWidget, TwoLineAvatarListItem

update_report_screen_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        id: toolbar_name
                        size_hint:1,0.15
                        pos_hint:{'center_x': .5, 'center_y': .075}
                        title: app.report
                        left_action_items: [["backburger", lambda x: app.change_to_second_menu()]]
                        elevation: 20

                    MDCard:
                        Carousel:
                            id: carousel
                            MDFloatLayout:
                                id: add_report
                                ScrollView:
                                    MDList:
                                        id: attributes_list
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "clock-start"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: departure_time
                                                text: "Czas wyjazdu"
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_time_picker(departure_time)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: departure_time.text = "Czas wyjazdu"


                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "calendar-arrow-right"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: departure_date
                                                text: "Data wyjazdu"
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_date_picker(departure_date)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: departure_date.text = "Data wyjazdu"


                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "clock-alert-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: arrival_time
                                                text: "Czas na miejscu"
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_time_picker(arrival_time)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: arrival_time.text = "Czas na miejscu"


                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "map-marker"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                id: event_location
                                                hint_text: 'Miejsce zdarzenia'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}
                                            MDIconButton:
                                                icon: "crosshairs-gps"
                                                pos_hint: {'center_x': .9, 'center_y': .5}


                                        OneLineListItem:
                                            MDTextField:
                                                id: type_of_event
                                                hint_text: 'Rodzaj zdarzenia'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5} 
                                            IconLeftWidget:
                                                icon: "fire"
                                                pos_hint: {'center_x': .1, 'center_y': .5}

                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "account-star-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: section_commander
                                                text: 'Dowódca sekcji'
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_members_with_permission(section_commander,3)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: 
                                                    section_commander.text = "Dowódca sekcji"
                                                    app.chosen_members.clear()

                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "account-cog-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: action_commander
                                                text: 'Dowódca akcji'
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_members_with_permission(action_commander,1)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: 
                                                    action_commander.text = "Dowódca akcji"
                                                    app.chosen_members.clear()                    

                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "steering"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: driver
                                                text: 'Kierowca'
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_members_with_permission(driver,2)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: 
                                                    driver.text = "Kierowca"
                                                    app.chosen_members.clear()                    
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "account-group-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: section
                                                text: 'Sekcja'
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_members_with_permission(section,0)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: 
                                                    section.text = "Sekcja"
                                                    app.chosen_members.clear()                                                 

                                        OneLineListItem:
                                            MDTextField:
                                                id: perpetrator
                                                hint_text: 'Sprawca'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5} 
                                            IconLeftWidget:
                                                icon: "account-alert-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}


                                        OneLineListItem:
                                            MDTextField:
                                                id: victim
                                                hint_text: 'Poszkodowany'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}   
                                            IconLeftWidget:
                                                icon: "human-handsup"
                                                pos_hint: {'center_x': .1, 'center_y': .5}

                                        MDTextFieldRect:
                                            id: details
                                            multiline: True
                                            hint_text: "Szczegóły zdarzenia"
                                            size_hint: 1, None                              

                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "calendar-arrow-left"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: return_date
                                                text: "Data powrotu"
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_date_picker(return_date)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: return_date.text = "Data powrotu"

                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "clock-end"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: finished_action_time
                                                text: "Godzina zakończenia"
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_time_picker(finished_action_time)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: finished_action_time.text = "Godzina zakończenia"

                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "clock-check-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: return_time
                                                text: "Godzina w remizie"
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_time_picker(return_time)
                                                size_hint: 0.5,None
                                            MDIconButton:
                                                icon: "trash-can-outline"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: return_time.text = "Godzina w remizie"

                                        OneLineListItem:
                                            MDTextField:
                                                id: odometer
                                                hint_text: 'Stan licznika'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5} 
                                            IconLeftWidget:
                                                icon: "speedometer"
                                                pos_hint: {'center_x': .1, 'center_y': .5}

                                        OneLineListItem:
                                            MDTextField:
                                                id: distance_to_event
                                                hint_text: 'Km. do miejsca zdarzenia'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}  
                                            IconLeftWidget:
                                                icon: "road"
                                                pos_hint: {'center_x': .1, 'center_y': .5}

                                        OneLineListItem:

                                MDFloatingActionButton:
                                    icon: "content-save"
                                    md_bg_color: app.theme_cls.primary_color
                                    pos_hint: {'center_x': .89, 'center_y': .09}
                                    on_release:
                                        app.myfirebase.update_report(attributes_list,app.report)
                                        app.show_snackbar("Zaktualizowano raport")    

"""


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
