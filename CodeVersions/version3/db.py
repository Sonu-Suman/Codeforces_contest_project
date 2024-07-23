import random
import pyrebase
import webbrowser
import Secerets
import smtplib

firebaseConfig = {'apiKey': "AIzaSyDsgfNoL4jeWbWxWDWOkh9LFHh_8EsgDIc",
                  'authDomain': "codeforcescontest-21b95.firebaseapp.com",
                  'projectId': "codeforcescontest-21b95",
                  'storageBucket': "codeforcescontest-21b95.appspot.com",
                  'databaseURL': "https://codeforcescontest-21b95-default-rtdb.firebaseio.com",
                  'messagingSenderId': "591689518159",
                  'appId': "1:591689518159:web:b092ebcfb3dbece588ae3a",
                  'measurementId': "G-XVTC7QM72L"}

firebase = pyrebase.initialize_app(firebaseConfig)


# =========================================SIGN IN & SIGN UP= AUTHENTICATION=======================================================
class SignInAndSignUp:
    def __init__(self):
        self.auth = firebase.auth()

    def login(self, email, password):
        self.auth.sign_in_with_email_and_password(email, password)
        return self.auth.current_user['localId']


    def signin(self, email, password):
        self.auth.create_user_with_email_and_password(email, password)


    def save_random_id(self, global_user_id, user_name, user_id, email):
        self.db = firebase.database()
        self.db.child('User_Id').child(f'{global_user_id}').child("Name").set(user_name)
        self.db.child('User_Id').child(f'{global_user_id}').child("Id").set(user_id)
        self.db.child("User_Id").child(f'{global_user_id}').child("Email").set(email)


    def get_user_id(self, global_user_id):
        self.db = firebase.database()
        id = self.db.child("User_Id").child(global_user_id).get()
        return [id.query_key, id.val()['Id'], id.val()['Email'], id.val()['Name']]

    def saving_email(self, email):
        self.db = firebase.database()
        get_random_id = random.randint(100, 10000000)
        email = self.db.child("User_email").child(f"{get_random_id}").set(email)

        content = "Hii , I'm Aparajita Suman.\nThank you for joining with us. This email is a confirmation email from Codeforces Problem Application.\n\n" \
                  "\tFrom now you'll get the notifications whenever we bring any new updates in our application.\n\t\tYou'll get to know about the questions that" \
                  " we'll adding and all short's of thing which will help you with you learning and overall improve your experience on our application."

        self.send_Email(f'{email}', content)
        # print("Executed Successfully")


    def send_Email(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('sk8282544@gmail.com', f'{Secerets.EMAIL_PASSWORD}')
        server.sendmail('sk8282544@gmail.com', to, content)
        server.close()


class Store:
    def __init__(self):
        self.storage = firebase.storage()

    def save_questions(self, personal_user_id, folder_for_this, on_cloud_filename, file):
        self.storage.child("Users").child(personal_user_id).child("Questions").child(folder_for_this).child(on_cloud_filename).put(file)


    def save_imp_link(self, user_id, link_name, link):
        self.db = firebase.database()
        self.db.child("Users").child(user_id).child("Link").child(link_name).set(link)


class Searching:
    def __init__(self):
        self.db = firebase.database()

    def get_link_page(self, user_id, link_name):
        result = self.db.child("Users").child(user_id).child("Link").get()
        webbrowser.open(result.val()[link_name])

        # print("S========", result.val()[link_name])
        # for i in result:
        #     print(i.val())


    def question(self, user_id, question_tag, question_name):
        self.storage = firebase.storage()
        result = self.storage.child("Users").child(user_id).child("Questions").child(question_tag).child(question_name).get_url(None)
        # print(result)
        webbrowser.open(result)


# if __name__ == "__main__":
#     s = SignInAndSignUp()
#     print(s.get_user_id("Aparajita Suman"))