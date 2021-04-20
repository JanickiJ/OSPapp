import requests
import json
from kivy.app import App


class MyFirebase():
    wak = "AIzaSyBXy9e5TqivFGRW_PqlXbEXH2xORqUhOzE"

    def sign_up(self, team_name, email_address, address, phone_number, password):
        app = App.get_running_app()
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + self.wak
        signup_payload = {"team_name": team_name, "email": email_address, "address": address, "phone": phone_number,
                          "password": password, "returnSecureToken": True}
        sign_up_request = requests.post(signup_url, data=signup_payload)
        sign_up_data = json.loads(sign_up_request.content.decode())
        if sign_up_request.ok == False:
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

    def sign_in(self, email_address, password):
        print(email_address, password)
