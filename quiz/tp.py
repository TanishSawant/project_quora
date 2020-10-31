import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("pages\quizapp-76c06s-firebase-adminsdk-z37mu-93f863e1f6.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
print("connected!!")

def getDb():
    return db


def getQuestions():
    ref = db.collection('user_data').document('userTanish1').collection('questions')
    questions = ref.stream()
    for question in questions:
        print(question.to_dict()['score'])
    
    #return list(questions)

getQuestions()