username_helper = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "fire-truck"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300   
"""
list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container           
"""
screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["clock", lambda x: app.navigation_draw()]]
            elevation: 8
        MDLabel:
            text: 'Hello world'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                title: 'Help'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                icon: 'fire-truck'
                on_action_button: app.navigation_draw()
"""
navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo Application'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    Widget:

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'cute.jpg'
                MDLabel:
                    text: '   OSP Kraków'
                    font_style: 'Subtitle1'
                    size_hint_y:None
                    height: self.texture_size[1]
                MDLabel:
                    text: '   ospkrakow@gmail.com'
                    font_style: 'Caption'    
                    size_hint_y:None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:
                            text: 'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'

"""
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
                        hint_text: 'Team Name'
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.48}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                    MDTextField:   
                        id: email_address 
                        hint_text: 'Email Address'
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.36}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                    MDRaisedButton:
                        text: "NEXT"
                        size_hint_x: 0.8
                        pos_hint: {'center_x':0.5,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.next()
                MDFloatLayout:
                    MDTextField:
                        id: address
                        hint_text: 'Adress'
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.48}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                    MDTextField:
                        id:phone_number
                        hint_text: 'Phone Number'
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.36}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                    MDRaisedButton:
                        text: "PREVIOUS"
                        size_hint_x: 0.39
                        pos_hint: {'center_x':0.3,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.previous()
                    MDRaisedButton:
                        text: "NEXT"
                        size_hint_x: 0.39
                        pos_hint: {'center_x':0.7,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.next1()
                MDFloatLayout:
                    MDTextField:
                        id:password
                        hint_text: 'Password'
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.48}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                        password: True
                    MDTextField:    
                        id: repeat_password
                        hint_text: 'Confirm Password'
                        size_hint_x:0.8
                        pos_hint: {'center_x':0.5,'center_y':0.36}
                        current_hint_text_color:0,0,0,1
                        color_mode:'custom'
                        line_color_focus:1,0,0,1
                        password: True
                    MDRaisedButton:
                        text: "PREVIOUS"
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
                        text: "SUBMIT"
                        size_hint_x: 0.39
                        pos_hint: {'center_x':0.7,'center_y':0.2}
                        md_bg_color:1,0,0,1
                        on_release:app.myfirebase.sign_up(team_name.text,email_address.text,address.text,phone_number.text,password.text)

        MDLabel:
            text: 'SignUp Form'
            bold: True
            pos_hint: {'center_x':0.67,'center_y':0.9}
            font_style: 'H4'
        MDLabel:
            id: Name
            text: 'Name'
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
            text: 'Contact'
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
            text: 'Submit'
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
            id: icon
            icon: 'account-circle'
            pos_hint:{'center_x':0.5,'center_y':0.8}
            user_font_size:'60sp'
            theme_text_color:'Custom'
            text_color:1,1,1,1
        MDLabel:
            id: label
            text:f"[font=Arial]Login Page[/font]"
            markup:True
            pos_hint:{'center_y':0.75}
            halign:'center'
            theme_text_color:'Custom'
            text_color:1,1,1,1
            font_style:'H5'
            opacity:0
        MDTextField:
            id:email_address
            hint_text:'Enter Your Email'
            size_hint_x:0.8
            pos_hint:{'center_x':0.5,'center_y':0.46}
            current_hint_text_color:0,0,0,1
            color_mode:'custom'
            line_color_focus:1,0,0,1
        MDTextField:
            id:password
            hint_text:'Enter Your Password'
            size_hint_x:0.8
            pos_hint:{'center_x':0.5,'center_y':0.34}
            current_hint_text_color:0,0,0,1
            password:True
            color_mode:'custom'
            line_color_focus:1,0,0,1
        MDRaisedButton:
            text:'Login'
            pos_hint:{'center_x':0.5,'center_y':0.2}
            size_hint_x:0.5
            md_bg_color:1,0,0,1
            on_release:app.sign_in(email_address.text,password.text)
        MDLabel:
            text:'Did you'
            pos_hint:{'center_x':0.672,'center_y':0.1}
            font_style:'Body2'
        MDTextButton:
            text:'forget your password?'
            pos_hint:{'center_x':0.58,'center_y':0.1}
            font_style:'Body2'
            theme_text_color:'Custom'
            text_color:1,0,0,1
"""
screen_change_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current= 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current= 'upload'
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Anna'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current= 'menu'
<UploadScreen>:
    name: 'upload'
    MDLabel:
        text: 'Lets upload some files'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current= 'menu'
"""
start_app_menu_helper = """
MDScreen:
    name:'OSP App'
    on_enter:
        app.text(label)
        app.text(button)
        app.text(aclabel)
        app.text(actext)
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
            opacity:0
        MDRaisedButton:
            id:button
            text: "Sign In"
            size_hint_x: 0.8
            pos_hint: {'center_x':0.5,'center_y':0.3}
            md_bg_color:1,0,0,1
            opacity:0
            on_press: app.change_to_login()
        MDLabel:
            id:aclabel
            text:'Need an account?'
            pos_hint:{'center_x':0.672,'center_y':0.22}
            font_style:'Body2'
            opacity:0
        MDTextButton:
            id:actext
            text:'Sign Up'
            pos_hint:{'center_x':0.65,'center_y':0.22}
            font_style:'Body2'
            theme_text_color:'Custom'
            text_color:1,0,0,1
            opacity:0
            on_press: app.change_to_signup()
"""