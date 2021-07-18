#from di.GlobalObjects import getEnv
import os
import firebase_admin
from firebase_admin import credentials, db

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class FirebaseDb:
    def __init__(self):
        cred = credentials.Certificate("../firebase-secrets.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': os.getenv("DATABASE_URL")
        })
        self.ref = db.reference("/")

    def add(self, childName, obj):
        self.ref.child(childName).push(obj)
    
    def getAllItems(self, childName):
        ret = {}
        for key, val in self.ref.child(childName).get().items():
            ret[key] = val
        return ret
            

if __name__ == "__main__":
    firebase = FirebaseDb()
    firebase.add('frases', 'fala aii')
    for key, val in firebase.ref.child('frases').get().items():
        print(val)
        