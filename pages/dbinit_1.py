import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

new_ref = db.collection('user_data').document('ann')
new_ref.set({
    'emailid' : 'a@a.com',
    'username' : 'aa'
})

class db():
    def __init__(self):
        cred = credentials.Certificate("pages\quizapp-76c06s-firebase-adminsdk-z37mu-93f863e1f6.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
    