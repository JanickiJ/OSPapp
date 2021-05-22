sign_up_helper = """
MDScreen:
    MDFloatLayout:
        MDCard:
            pos_hint: { 'center_x':0.5, 'center_y':0.5}
            Carousel:
                id: slide
                MDFloatLayout:
                    MDTextField:
                        id: team_name
                        hint_text: 'Nazwa załogi'
                        required: True
                        helper_text_mode: "on_error"
                        helper_text: "Pole jest wymagane"
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.48}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                    MDTextField:   
                        id: email_address 
                        hint_text: 'Adres e-mail'
                        required: True
                        helper_text_mode: "on_error"
                        helper_text: "Pole jest wymagane"
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.36}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                    MDRaisedButton:
                        text: "DALEJ"
                        size_hint_x: 0.8
                        pos_hint: {'center_x':0.5,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.next()
                MDFloatLayout:
                    MDTextField:
                        id: address
                        hint_text: 'Adres'
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.48}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                    MDTextField:
                        id:phone_number
                        hint_text: 'Numer telefonu'
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.36}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                    MDRaisedButton:
                        text: "WSTECZ"
                        size_hint_x: 0.39
                        pos_hint: {'center_x':0.3,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.previous()
                    MDRaisedButton:
                        text: "DALEJ"
                        size_hint_x: 0.39
                        pos_hint: {'center_x':0.7,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.next1()
                MDFloatLayout:
                    MDTextField:
                        id:password
                        hint_text: 'Hasło'
                        required: True
                        helper_text_mode: "on_error"
                        helper_text: "Pole jest wymagane"
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.48}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                        password: True
                    MDTextField:    
                        id: repeat_password
                        hint_text: 'Powtórz hasło'
                        required: True
                        helper_text_mode: "on_error"
                        helper_text: "Pole jest wymagane"
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.36}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                        password: True
                    MDRaisedButton:
                        text: "WSTECZ"
                        size_hint_x: 0.39
                        pos_hint: {'center_x':0.3,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.previous1()
                    MDLabel:
                        id:message
                        color:(1,0,0,1)
                        size_hint:0.8,0.1
                        pos_hint:{'center_x':0.55,'center_y':0.3}
                    MDRaisedButton:
                        text: "ZATWIERDŹ"
                        size_hint_x: 0.39
                        pos_hint: {'center_x':0.7,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.myfirebase.sign_up(team_name.text,email_address.text,address.text,phone_number.text,password.text,repeat_password.text)
        MDLabel:
            text: 'Rejestracja'
            bold: True
            pos_hint: {'center_x':0.67,'center_y':0.9}
            font_style: 'H4'
        MDIconButton:
            id: back_button
            icon:"arrow-left"
            theme_text_color: "Custom"
            text_color:0,0,0,1
            pos_hint:{"center_x": .05, "center_y": .97}
            on_release:app.change_to_start()
        MDLabel:
            id: Name
            text: 'Nazwa'
            pos_hint:{'center_x':0.6,'center_y':0.75}
            font_style:'H6'
            theme_text_color:'Custom'
            text_color:1,0,0,1
        MDIconButton:
            id: name
            icon:'numeric-1-circle'
            pos_hint:{'center_x':0.2,'center_y':0.69}
            user_font_size: '35sp'
            theme_text_color:'Custom'
            text_color:1,0,0,1
        MDProgressBar:
            id: progress
            size_hint_x:0.15
            pos_hint: {'center_x':0.35,'center_y':0.69}
        MDLabel:
            id: Contact
            text: 'Kontakt'
            pos_hint:{'center_x':0.88,'center_y':0.75}
            font_style:'H6'
            theme_text_color:'Custom'
            text_color:1,0,0,1
        MDIconButton:
            id: contact
            icon:'numeric-2-circle'
            pos_hint:{'center_x':0.5,'center_y':0.69}
            user_font_size: '35sp'
            theme_text_color:'Custom'
            text_color:1,0,0,1
        MDProgressBar:
            id:progress1
            size_hint_x:0.15
            pos_hint: {'center_x':0.65,'center_y':0.69}
        MDLabel:
            id: Submit
            text: 'Hasło'
            pos_hint:{'center_x':1.2,'center_y':0.75}
            font_style:'H6'
            theme_text_color:'Custom'
            text_color:1,0,0,1
        MDIconButton:
            id: submit
            icon:'numeric-3-circle'
            pos_hint:{'center_x':0.8,'center_y':0.69}
            user_font_size: '35sp'
            theme_text_color:'Custom'
            text_color:1,0,0,1      
"""
log_in_helper = """
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

start_app_menu_helper = """
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
            pos_hint:{'center_x':0.85,'center_y':0.22}
            font_style:'Body2'
        MDTextButton:
            id:actext
            text:'Zarejestruj się'
            pos_hint:{'center_x':0.57,'center_y':0.22}
            font_style:'Body2'
            theme_text_color:'Custom'
            text_color:1,0,0,1
            on_press: app.change_to_signup()
"""