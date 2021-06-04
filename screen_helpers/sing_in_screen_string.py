sing_in_helper = """
MDScreen:
    name:'Login Page'
    on_enter:
        app.anim(back)
        app.anim1(back1)
        app.icons(icon)
        app.text(label)
    MDFloatLayout:
        MDFloatLayout:
            id: back
            size_hint_y:0.6
            pos_hint: {'center_y':1.8}
            radius: [0,0,0,40]
            canvas:
                Color:
                    rgb: (1,0,0,1)
                Rectangle:
                    size: self.size
                    pos: self.pos
        MDFloatLayout:
            id: back1
            size_hint_y:0.6
            pos_hint: {'center_y':1.8}
            radius: [0,0,0,40]
            canvas:
                Color:
                    rgb: (1,0,0,1)
                Ellipse:
                    size: self.size
                    pos: self.pos
        MDIconButton:
            id: back_button
            icon:"arrow-left"
            theme_text_color: "Custom"
            text_color:1,1,1,1
            pos_hint:{"center_x": .05, "center_y": .97}
            on_release:app.change_to_start()
        MDIconButton:
            id: icon
            icon: 'account-circle'
            pos_hint:{'center_x':0.5,'center_y':0.8}
            user_font_size:'60sp'
            theme_text_color:'Custom'
            text_color:1,1,1,1
        MDLabel:
            id: label
            text:f"[font=Arial]Logowanie[/font]"
            markup:True
            pos_hint:{'center_y':0.75}
            halign:'center'
            theme_text_color:'Custom'
            text_color:1,1,1,1
            font_style:'H5'
            opacity:0
        MDTextField:
            id:email_address
            hint_text:'Wprowadź e-mail'
            size_hint_x:0.8
            pos_hint:{'center_x':0.5,'center_y':0.46}
            current_hint_text_color:0,0,0,1
            color_mode:'custom'
            line_color_focus:1,0,0,1
        MDTextField:
            id:password
            hint_text:'Wprowadź hasło'
            size_hint_x:0.8
            pos_hint:{'center_x':0.5,'center_y':0.34}
            current_hint_text_color:0,0,0,1
            password:True
            color_mode:'custom'
            line_color_focus:1,0,0,1
        MDRaisedButton:
            text:'Zaloguj się'
            pos_hint:{'center_x':0.5,'center_y':0.2}
            size_hint_x:0.5
            md_bg_color:1,0,0,1
            on_release:app.sign_in(email_address.text,password.text)
        Check:
            id:save_password
            active:True
            pos_hint:{'center_x':.2,'center_y':0.29}
            theme_text_color:'Custom'
            color:(1,0,0,1)
        MDLabel:
            text:"Zapamiętaj hasło"
            pos_hint:{'center_x':.75,'center_y':0.29}
            font_size:'15sp'
        MDLabel:
            id:message
            color:(1,0,0,1)
            size_hint:0.8,0.1
            pos_hint:{'center_x':0.5,'center_y':0.3}
        MDTextButton:
            text:'Zapomniałeś hasła?'
            pos_hint:{'center_x':0.5,'center_y':0.13}
            font_style:'Body2'
            theme_text_color:'Custom'
            text_color:1,0,0,1
            on_release: app.forgot_password()
        MDLabel:
            id:message
            color:(1,0,0,1)
            size_hint:0.8,0.1
            pos_hint:{'center_x':0.55,'center_y':0.3}
<Check@CheckBox>:
    size_hint:None,None
    size: dp(48),dp(48)
"""