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
                        on_release:app.start_screen.sing_up_next_1()
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
                        on_release:app.start_screen.sing_up_previous_2()
                    MDRaisedButton:
                        text: "DALEJ"
                        size_hint_x: 0.39
                        pos_hint: {'center_x':0.7,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.start_screen.sing_up_next_2()
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
                        on_release:app.start_screen.sing_up_previous_2()
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