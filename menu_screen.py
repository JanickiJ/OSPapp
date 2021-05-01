from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem, TwoLineIconListItem, IconLeftWidget, TwoLineAvatarListItem

menu_screen_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        size_hint:1,0.15
                        pos_hint:{'center_x': .5, 'center_y': .075}
                        title: "OSP CZCHÓW"
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation: 20
                    BoxLayout:
                        id:tabox
                        orientation:'vertical'
                        size_hint:1,0.125
                        pos_hint:{'center_x': .5, 'center_y': .225}
                        MDTabs:
                            id: tabs
                            tab_display_mode: 'text'
                            MDTabsBase:
                                id: rap_tab
                                name: 'raport'
                                text: "Nowy raport"
                            MDTabsBase:
                                id: idc_tab
                                name: 'idc'
                                text: "Dupa" 
                            MDTabsBase:
                                id: mem_tab
                                name: 'members'
                                text: "Członkowie"
                    MDCard:
                        Carousel:
                            id: carousel
                            MDFloatLayout:
                                id: add_report
                                ScrollView:
                                    MDList:
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
                                            IconLeftWidget:
                                                icon: "fire"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                id: type_of_event
                                                hint_text: 'Rodzaj zdarzenia'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5} 
                                                
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "account-star-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                hint_text: 'Dowódca sekcji'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}
                                            MDIconButton:
                                                icon: "format-list-bulleted"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: app.show_members_with_permission(3)
                                                                                             
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "account-cog-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                hint_text: 'Dowódca akcji'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}
                                            MDIconButton:
                                                icon: "format-list-bulleted"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: app.show_members_with_permission(1)                                                  
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "steering"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                hint_text: 'Kierowca'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}  
                                            MDIconButton:
                                                icon: "format-list-bulleted"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: app.show_members_with_permission(2)
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "account-group-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                hint_text: 'Sekcja'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}  
                                            MDIconButton:
                                                icon: "format-list-bulleted"
                                                pos_hint: {'center_x': .9, 'center_y': .5}
                                                on_release: app.show_members_with_permission(0)                                                
                                                                                        
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "account-alert-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                id: perpetrator
                                                hint_text: 'Sprawca'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}                                          
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "human-handsup"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                id: victim
                                                hint_text: 'Poszkodowany'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}                                          
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "information-outline"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDRaisedButton:
                                                id: departure_date
                                                text: "Szczegóły zdarzenia"
                                                pos_hint: {'center_x': .55, 'center_y': .5}
                                                on_release: app.show_details_dialog()
                                                size_hint: 0.5,None  
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
                                            IconLeftWidget:
                                                icon: "speedometer"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                id: odometer
                                                hint_text: 'Stan licznika'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}    
                                        OneLineListItem:
                                            IconLeftWidget:
                                                icon: "road"
                                                pos_hint: {'center_x': .1, 'center_y': .5}
                                            MDTextField:
                                                id: distance_to_event
                                                hint_text: 'Km. do miejsca zdarzenia'
                                                size_hint_x:0.6
                                                pos_hint: {'center_x':0.5,'center_y':0.5}       
                                        OneLineListItem:
                                MDFloatingActionButton:
                                    icon: "content-save"
                                    md_bg_color: app.theme_cls.primary_color
                                    pos_hint: {'center_x': .89, 'center_y': .09}
                                    #do napisania
                                    #on_release:app.myfirebase.add_report([])                                                                                                           
                            MDFloatLayout:
                                id: active_reports
                                ScrollView:
                                    MDList:
                                        id: active_reports_list
                                
                            MDFloatLayout:
                                ScrollView:
                                    MDList:
                                        id: crew_members                           
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                
                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: navigator_icon.height
            
                    MDIcon:
                        id: navigator_icon
                        icon: "fire"
                        font_size: "72sp"                        
                        theme_text_color: "Error"
                        halign: "center"
                    
    
                MDLabel:
                    text: "Osp Czchów"
                    font_style: "H5"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "Krakowska 43"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                MDLabel:
                    text: "osp@gmail.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Wyloguj"
                            IconLeftWidget:
                                icon: "logout"
                        OneLineIconListItem:
                            text: "Twórcy"
                            IconLeftWidget:
                                icon: "creation"
                                                      
"""


class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
