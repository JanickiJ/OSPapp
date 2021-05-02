import datetime

import requests
import json
from kivy.app import App
import pyrebase

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


class MyFirebase():

    def __init__(self):
        self.wak = firebase_config["apiKey"]
        self.firebase = pyrebase.initialize_app(firebase_config)
        self.db = self.firebase.database()
        self.auth = self.firebase.auth()
        self.localId = None
        self.crew_members = None
        self.account_data = None
        self.reports = None

    def authentication(self, email, password):
        try:
            self.localId = self.auth.sign_in_with_email_and_password(email, password)["localId"]
            self.crew_members = self.db.child("Brigades").child(self.localId).child("crew_members").get().val()
            self.account_data = self.db.child("Brigades").child(self.localId).child("account_data").get().val()
            self.reports = self.db.child("Brigades").child(self.localId).child("reports").get().val()
            print(self.reports)
        except:
            print("Invalid email or password")

    def sign_up(self, team_name, email_address, address, phone_number, password):
        app = App.get_running_app()
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.wak
        signup_payload = {"team_name": team_name, "email": email_address, "address": address, "phone": phone_number,
                          "password": password, "returnSecureToken": True}
        sign_up_request = requests.post(signup_url, data=signup_payload)
        sign_up_data = json.loads(sign_up_request.content.decode())
        if not sign_up_request.ok:
            error_message = sign_up_data["error"]['message']
            app.sign_up_screen.ids['message'].text = error_message
        if sign_up_request.ok:
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
            my_data = '{"account_data":{"email":"","name":"","address":""},"crew_members":"","reports":""}'
            post_request = requests.patch(
                "https://ospapp-705a7-default-rtdb.europe-west1.firebasedatabase.app/Brigades/" + localId + ".json?auth=" + idToken,
                data=my_data)
            print(post_request.ok)
            print(json.loads(post_request.content.decode()))

    def sign_in(self, email, password):
        print(email, password)
        self.authentication("haslo@gmail.com", "123456")
        confirmed = True
        return confirmed

    def get_name(self):
        return self.account_data["name"]

    def get_email(self):
        return self.account_data["email"]

    def get_address(self):
        return self.account_data["address"]

    def get_active_reports(self):
        return self.db.child("Brigades").child(self.localId).child("reports").get().val().keys()

    def get_crew_members(self):
        crew_member_list = []
        for member, permissions in self.crew_members.items():
            crew_member_list.append([member])
            for permission in permissions.values():
                if permission == 'True':
                    crew_member_list[-1].append(True)
        return crew_member_list

    def get_members_with_permission(self, permission):
        if permission == 0:
            return [member[0] for member in self.get_crew_members()]
        else:
            return [member[0] for member in self.get_crew_members() if member[permission]]

    # do napisania
    def upgrade_report(self):
        pass

    def remove_report(self, id):
        print(self.db.child("Brigades").child(self.localId).child("reports").child(id).remove())

    def add_report(self, attributes_list):
        data_fields = dict()
        for i, child in enumerate(attributes_list.children):
            field_name = report_fields[-i]
            if field_name == "event_details":
                data_fields[field_name] = child.text
            elif field_name == "section":
                data_fields[field_name] = child.children[1].text.split(",")
            else:
                try:
                    data_fields[field_name] = child.children[1].text
                except:
                    continue
        report_id = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
        self.db.child("Brigades").child(self.localId).child("reports").child(report_id).set(data_fields)
