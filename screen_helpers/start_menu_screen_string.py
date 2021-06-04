start_menu_helper = """
MDScreen:
    name:'OSP App'
    MDFloatLayout:
        MDLabel:
            id: label
            text:f"[font=Arial]OSP App[/font]"
            markup:True
            pos_hint:{'center_y':0.75}
            halign:'center'
            theme_text_color:'Custom'
            text_color:1,0,0,1
            font_style:'H5'
        MDRaisedButton:
            id:button
            text: "Zaloguj się"
            size_hint_x: 0.8
            pos_hint: {'center_x':0.5,'center_y':0.3}
            md_bg_color:1,0,0,1
            on_press: app.change_to_login()
        MDLabel:
            id:aclabel
            text:'Nie masz konta?'
            pos_hint:{'center_x':0.70,'center_y':0.22}
            font_style:'Body2'
        MDTextButton:
            id:actext
            text:'Zarejestruj się'
            pos_hint:{'center_x':0.67,'center_y':0.22}
            font_style:'Body2'
            theme_text_color:'Custom'
            text_color:1,0,0,1
            on_press: app.change_to_signup()
"""
