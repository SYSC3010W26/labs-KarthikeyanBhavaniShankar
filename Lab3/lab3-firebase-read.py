# lab3-firebase-read.py
# SYSC 3010 – Lab 3
# Read data back from Firebase Realtime Database

import pyrebase

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyCfhpUXtm-FY6409LYRIKAheA8C1WasN88",
    "authDomain": "sysc3010-lab3-karthikeya-14579.firebaseapp.com",
    "databaseURL": "https://sysc3010-lab3-karthikeya-14579-default-rtdb.firebaseio.com/",
    "projectId": "sysc3010-lab3-karthikeya-14579",
    "storageBucket": "sysc3010-lab3-karthikeya-14579.appspot.com"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Anonymous login
user = auth.sign_in_anonymous()

print("Reading data from Firebase...\n")

# Read data under your node
data = db.child("karthikeyanpi").get(user["idToken"])

# Print all entries
for key, value in data.val().items():
    print("Entry ID:", key)
    print(value)
    print("-" * 40)
# lab3-firebase-read.py
# SYSC 3010 – Lab 3
# Read data back from Firebase Realtime Database

import pyrebase

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyCfhpUXtm-FY6409LYRIKAheA8C1WasN88",
    "authDomain": "sysc3010-lab3-karthikeya-14579.firebaseapp.com",
    "databaseURL": "https://sysc3010-lab3-karthikeya-14579-default-rtdb.firebaseio.com/",
    "projectId": "sysc3010-lab3-karthikeya-14579",
    "storageBucket": "sysc3010-lab3-karthikeya-14579.appspot.com"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Anonymous login
user = auth.sign_in_anonymous()

print("Reading data from Firebase...\n")

# Read data under your node
data = db.child("karthikeyanpi").get(user["idToken"])

# Print all entries
for key, value in data.val().items():
    print("Entry ID:", key)
    print(value)
    print("-" * 40)
# lab3-firebase-read.py
# SYSC 3010 – Lab 3
# Read data back from Firebase Realtime Database

import pyrebase

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyCfhpUXtm-FY6409LYRIKAheA8C1WasN88",
    "authDomain": "sysc3010-lab3-karthikeya-14579.firebaseapp.com",
    "databaseURL": "https://sysc3010-lab3-karthikeya-14579-default-rtdb.firebaseio.com/",
    "projectId": "sysc3010-lab3-karthikeya-14579",
    "storageBucket": "sysc3010-lab3-karthikeya-14579.appspot.com"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Anonymous login
user = auth.sign_in_anonymous()

print("Reading data from Firebase...\n")

# Read data under your node
data = db.child("karthikeyanpi").get(user["idToken"])

# Print all entries
for key, value in data.val().items():
    print("Entry ID:", key)
    print(value)
    print("-" * 40)
# lab3-firebase-read.py
# SYSC 3010 – Lab 3
# Read data back from Firebase Realtime Database

import pyrebase

# Firebase configuration
firebaseConfig = {
    "apiKey": "AIzaSyCfhpUXtm-FY6409LYRIKAheA8C1WasN88",
    "authDomain": "sysc3010-lab3-karthikeya-14579.firebaseapp.com",
    "databaseURL": "https://sysc3010-lab3-karthikeya-14579-default-rtdb.firebaseio.com/",
    "projectId": "sysc3010-lab3-karthikeya-14579",
    "storageBucket": "sysc3010-lab3-karthikeya-14579.appspot.com"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Anonymous login
user = auth.sign_in_anonymous()

print("Reading data from Firebase...\n")

# Read data under your node
data = db.child("karthikeyanpi").get(user["idToken"])

# Print all entries
for key, value in data.val().items():
    print("Entry ID:", key)
    print(value)
    print("-" * 40)

