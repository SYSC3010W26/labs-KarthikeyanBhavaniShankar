# lab3-firebase.py

import pyrebase
import time
from datetime import datetime
import random

firebaseConfig = {
    "apiKey": "AIzaSyCfhpUXtm-FY6409LYRIKAheA8C1WasN88",
    "authDomain": "sysc3010-lab3-karthikeya-14579.firebaseapp.com",
    "databaseURL": "https://sysc3010-lab3-karthikeya-14579-default-rtdb.firebaseio.com/",
    "projectId": "sysc3010-lab3-karthikeya-14579",
    "storageBucket": "sysc3010-lab3-karthikeya-14579.appspot.com",
    "messagingSenderId": "unused",
    "appId": "unused"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

user = auth.sign_in_anonymous()

print("Connected to Firebase.")
print("Uploading sensor data every 5 seconds...")

while True:
    data = {
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "pressure": round(random.uniform(980.0, 1020.0), 2)
    }

    db.child("karthikeyanpi").push(data, user["idToken"])
    print("Uploaded:", data)

    time.sleep(5)

