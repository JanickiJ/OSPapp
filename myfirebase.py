import datetime
import requests
import json
from kivy.app import App
import pyrebase
import os

firebase_config = {
    "apiKey": "AIzaSyBXy9e5TqivFGRW_PqlXbEXH2xORqUhOzE",
    "authDomain": "ospapp-705a7.firebaseapp.com",
    "databaseURL": "https://ospapp-705a7-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "ospapp-705a7",
    "storageBucket": "ospapp-705a7.appspot.com",
    "messagingSenderId": "382392178612",
    "appId": "1:382392178612:web:0618ff5a3850db4cbcc4e1",
    "measurementId": "G-2Q32QZVTKK"
}

report_fields = ["departure_time", "departure_date", "arrival_time", "event_location", "type_of_event",
                 "section_commander", "action_commander", "driver", "section", "perpetrator",
                 "victim", "details", "return_date", "finished_action_time", "return_time",
                 "odometer", "distance_to_event"]
base_fields = {"departure_time":"Czas wyjazdu", "departure_date":"Data wyjazdu", "arrival_time":"Czas na miejscu",
				 "event_location":"Miejsce zdarzenia", "type_of_event":"Rodzaj zdarzenia",
                 "section_commander":"Dowódca sekcji", "action_commander":"Dowódca akcji", "driver":"Kierowca",
                  "section":"Sekcja", "perpetrator":"Sprawca",
                 "victim":"Poszkodowany", "details":"Szczegóły zdarzenia", "return_date":"Data powrotu",
                  "finished_action_time":"Godzina zakończenia", "return_time":"Godzina w remizie",
                 "odometer":"Stan licznika", "distance_to_event":"Km. do miejsca zdarzenia"}


class MyFirebase():

    def __init__(self):
        self.wak = firebase_config["apiKey"]
        self.firebase = pyrebase.initialize_app(firebase_config)
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()
        self.localId = None
        self.dbId = None
        self.crew_members = None
        self.account_data = None
        self.reports = None

    def authentication(self, email, password):
        app = App.get_running_app()
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            self.localId = user["localId"]
            self.refreshtoken = user["refreshToken"]
            with open('refresh_token.txt', 'w') as file:
                file.write(self.refreshtoken)
            self.dbId = self.db.child("Brigades").child(self.localId).child("dbId").get().val()
            if self.dbId:
                self.localId = self.dbId
            self.crew_members = self.db.child("Brigades").child(self.localId).child("crew_members").get().val()
            self.account_data = self.db.child("Brigades").child(self.localId).child("account_data").get().val()
            self.reports = self.db.child("Brigades").child(self.localId).child("reports").get().val()
            #to_remove=[]
            #for report, items in self.reports.items():
            	#if items['is_completed']==True:
            		#to_remove.append(report)
            #for item in to_remove:
            	#self.reports.pop(item)
        except:
            app.log_in_screen.ids['message'].text = "Nieprawidłowy login lub hasło"
            return False
        return True

    def sign_up(self, team_name, email_address, address, phone_number, password, password_repeated):

        app = App.get_running_app()
        if password != password_repeated:
            app.sign_up_screen.ids['message'].text = "Hasła nie są identyczne"
            return
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.wak
        signup_payload = {"team_name": team_name, "email": email_address, "address": address, "phone": phone_number,
                          "password": password, "returnSecureToken": True}
        sign_up_request = requests.post(signup_url, data=signup_payload)
        sign_up_data = json.loads(sign_up_request.content.decode())
        if not sign_up_request.ok:
            error_message = sign_up_data["error"]['message']
            app.sign_up_screen.ids['message'].text = error_message

        else:
            refresh_token = sign_up_data['refreshToken']
            localId = sign_up_data['localId']
            idToken = sign_up_data['idToken']
            # save refresh token in a file
            with open("refresh_token.txt", "w") as f:
                f.write(refresh_token)
            # save localid to a variable
            app.local_id = localId
            # save idtoken to variable
            app.id_token = idToken
            # create new key in database from localid
            my_data = {'account_data': {'email': email_address, 'name': team_name, 'address': address},
                       'crew_members': {}, 'reports': {}}
            print(my_data)
            data = json.dumps(my_data)
            print(data)
            post_request = requests.patch(
                "https://ospapp-705a7-default-rtdb.europe-west1.firebasedatabase.app/Brigades/" + localId + ".json?auth=" + idToken,
                data=data)
            print(localId)
            self.auth.send_email_verification(app.id_token)
            app.verification_sent(email_address)

    def sign_in(self, email, password):
        return self.authentication(email, password)

    def show_report(self, attributes_list, report):
        data_fields = self.reports[report]
        for i, child in enumerate(attributes_list.children):
            field_name = report_fields[-(i+1)]
            if field_name == "section":
            	if data_fields[field_name]=="":
            		child.children[1].text = base_fields[field_name]
            	else:
            		child.children[1].text = ",".join(data_fields[field_name])
            else:
                try:
                	if data_fields[field_name]=="":
                		child.children[1].text = base_fields[field_name]
                	else:
                		child.children[1].text = str(data_fields[field_name])
                except:
                    continue

    def update_report(self, attributes_list, id):
        self.remove_report(id)
        self.add_report(attributes_list, id)

    def remove_report(self, id):
        self.db.child("Brigades").child(self.localId).child("reports").child(id).remove()
        self.reports = self.db.child("Brigades").child(self.localId).child("reports").get().val()

    def add_report(self, attributes_list, id=datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')):
        data_fields = dict()
        for i, child in enumerate(attributes_list.children):
            field_name = report_fields[-(i+1)]
            if field_name == "section":
            	if child.children[1].text==base_fields[field_name]:
            		data_fields[field_name]=""
            	else:
            		data_fields[field_name] = child.children[1].text.split(",")
            else:
                try:
                	if child.children[1].text==base_fields[field_name]:
                		data_fields[field_name]=""
                	else:
                		data_fields[field_name] = child.children[1].text
                except:
                    continue

        data_fields['is_completed']=False
        self.db.child("Brigades").child(self.localId).child("reports").child(id).set(data_fields)
        self.reports = self.db.child("Brigades").child(self.localId).child("reports").get().val()

    def get_name(self):
        return self.account_data["name"]

    def get_email(self):
        return self.account_data["email"]

    def get_address(self):
        return self.account_data["address"]

    def get_active_reports(self):
        if self.reports:
            return self.db.child("Brigades").child(self.localId).child("reports").get().val().keys()
        return []

    def get_crew_members(self):
        crew_member_list = []
        if self.crew_members:
            for member, attributes in self.crew_members.items():
                crew_member_list.append([str(attributes['name']+' '+str(attributes['last_name']))])
                if attributes['action_commander']==True:
                    crew_member_list[-1].append(True)
                else:
                    crew_member_list[-1].append(False)
                if attributes['driver']==True:
                    crew_member_list[-1].append(True)
                else:
                    crew_member_list[-1].append(False)
                if attributes['section_commander']==True:
                    crew_member_list[-1].append(True)
                else:
                    crew_member_list[-1].append(False)
            print(crew_member_list)
        return crew_member_list

    def get_members_with_permission(self, permission):
        if permission == 0:
            return [member[0] for member in self.get_crew_members()]
        else:
            return [member[0] for member in self.get_crew_members() if member[permission]]

    def get_field(self, report, field):
        return self.reports[report][field]

    def reset_password(self, email):
        self.auth.send_password_reset_email(email)

    def log_out(self):
        app = App.get_running_app()
        self.localId = None
        self.crew_members = None
        self.account_data = None
        self.reports = None
        e_mail_saved = ""
        password_saved = ""
        if os.stat('saved_password.txt').st_size != 0:
            with open('saved_password.txt', 'r') as saved_password_file:
                content = saved_password_file.read()
                json_content = json.loads(content)
                e_mail_saved, password_saved = json_content['email'], json_content['password']
        app.log_in_screen.ids['email_address'].text = e_mail_saved
        app.log_in_screen.ids['password'].text = password_saved
        open('refresh_token.txt', 'w').close()
        app.screen_manager.switch_to(app.log_in_screen)
