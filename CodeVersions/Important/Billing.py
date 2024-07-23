import urllib.request
import pyrebase



"""
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDsgfNoL4jeWbWxWDWOkh9LFHh_8EsgDIc",
  authDomain: "codeforcescontest-21b95.firebaseapp.com",
  projectId: "codeforcescontest-21b95",
  storageBucket: "codeforcescontest-21b95.appspot.com",
  messagingSenderId: "591689518159",
  appId: "1:591689518159:web:b092ebcfb3dbece588ae3a",
  measurementId: "G-XVTC7QM72L"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
"""






firebaseConfig = {'apiKey': "AIzaSyDsgfNoL4jeWbWxWDWOkh9LFHh_8EsgDIc",
                  'authDomain': "codeforcescontest-21b95.firebaseapp.com",
                  'projectId': "codeforcescontest-21b95",
                  'storageBucket': "codeforcescontest-21b95.appspot.com",
                  'databaseURL': "https://codeforcescontest-21b95-default-rtdb.firebaseio.com",
                  'messagingSenderId': "591689518159",
                  'appId': "1:591689518159:web:b092ebcfb3dbece588ae3a",
                  'measurementId': "G-XVTC7QM72L"}

firebase = pyrebase.initialize_app(firebaseConfig)




# =========================================for test ===========================================================
# ===============================================For Storage==========================================================
storage = firebase.storage()


filename = input("Enter the file name you want to upload: ")
cloudfilename = input("Enter the could file name you want to update: ")

# for uploading data
storage.child(cloudfilename).put(filename)

# For accessing from command line
print(storage.child(cloudfilename).get_url(None))

# Download the uploaded file
# storage.child(cloudfilename).download("", filename="download.txt")  # empty path for same directory
#
# # Reading file from cloud storage
# url = storage.child(cloudfilename).get_url(None)
#
# f = urllib.request.urlopen(url).read()
#
# print(f)

# =============================== For Real TIme Database============================================
# db = firebase.database()
#
# data = {'age': 21, "Address": "Bihar", "Name": "Aparajita Suman", 'Employee': False}

# Creating node in database-------------------------------------------
# # db.push(data)
# db.child("person").push(data)  # This is the good practice
#
# # Creating own id
# db.child("person").child("Myid").set(data)
#
# # Update realtime database---------------------
# db.child("person").child("Myid").update({"age": 20})
#
# # Updating those value in node which I don't know the id
# people = db.child("person").get()
#
# for person in people.each():
#     # print(person.val())
#     # print(person.key())
#     if person.val()['age'] == 20:
#         db.child("person").child(person.key()).update({'age': 18})
#
#
# # Deleting data in firebase=-----------------------------------
#
# # For deleting a element in node
# db.child("people").child("person").child('age').remove()
#
# # Deleting for node
# db.child('people').child('person').remove()

# ============================READ DATA========================================================================
"""
After adding this in Rule: for people
"people": {".indexOn": ['age', 'address', 'name', 'employed']}
"""

# people = db.child('person').order_by_child('name').equal_to('Aparajita Suman').get()
#
# for person in people.each():
#     print(person.val())
#
#
# # Age validation
# people = db.child('person').order_by_child('age').start_at(16).end_at(25).get()
#
# for person in people.each():
#     print(person.val())
#
#
# # For boolean value
# people = db.child('person').order_by_child('employee').equal_to(True).limit_to_first(1).get()
# for person in people.each():
#     print(person.val())