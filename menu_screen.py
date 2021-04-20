from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem


menu_screen_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "OSP CZCHÓW"
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                    MDTabs:
                        size_hint: (1, .1)
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                    MDCard:
                        Carousel:
                            id: carousel
                            MDFloatLayout:
                                MDTextField:
                                    id: team_name
                                    hint_text: 'Ekran1'
                                    size_hint_x:0.8
                                    pos_hint: {'center_x':0.5,'center_y':0.48}
                                    current_hint_text_color:0,0,0,1
                                    color_mode:'custom'
                                    line_color_focus:1,0,0,1
                            MDFloatLayout:
                                md_bg_color: app.theme_cls.primary_color
                                MDTextField:
                                    id: team_name
                                    hint_text: 'Ekran2'
                                    size_hint_x:0.8
                                    pos_hint: {'center_x':0.5,'center_y':0.48}
                                    current_hint_text_color:0,0,0,1
                                    color_mode:'custom'
                                    line_color_focus:1,0,0,1
                            MDFloatLayout:
                                MDTextField:
                                    id: team_name
                                    hint_text: 'Ekran3'
                                    size_hint_x:0.8
                                    pos_hint: {'center_x':0.5,'center_y':0.48}
                                    current_hint_text_color:0,0,0,1
                                    color_mode:'custom'
                                    line_color_focus:1,0,0,1
                                        
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
  



<Tab>

    MDIconButton:
        id: icon
        icon: root.icon
        user_font_size: "48sp"
        pos_hint: {"center_x": .5, "center_y": .5}                                                                        
"""


class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()