# lab3-firebase-read.py
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyCfhpUXtm-FY6409LYRIKAheA8C1WasN88",
    "authDomain": "sysc3010-lab3-karthikeya-14579.firebaseapp.com",
    "databaseURL": "https://sysc3010-lab3-karthikeya-14579-default-rtdb.firebaseio.com/",
    "projectId": "sysc3010-lab3-karthikeya-14579",
    "storageBucket": "sysc3010-lab3-karthikeya-14579.appspot.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_anonymous()

print("Reading data from Firebase...\n")


data = db.child("karthikeyanpi").get(user["idToken"])
for key, value in data.val().items():
    print("Entry ID:", key)
    print(value)
    print("-" * 40)




