from utils.GetEnv import GetEnv
from utils.Singleton import singleton
import firebase_admin
from firebase_admin import credentials, db

@singleton
class FirebaseDb:
    def __init__(self):
        cred = credentials.Certificate("./firebase-secrets.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': GetEnv().get("DATABASE_URL")
        })
        self.ref = db.reference("/")

    def add(self, childName, obj):
        self.ref.child(childName).push(obj)
    
    def getAllItems(self, childName):
        ret = {}
        for key, val in self.ref.child(childName).get().items():
            ret[key] = val
        return ret

    def deleteOrderedItem(self, childName, position):
        items = self.getAllItems(childName)
        pos = 1
        for item in items:
            if pos == position:
                removeItem = item
                self.ref.child(childName).child(removeItem).delete()
                return True
            pos += 1
        return False
        



if __name__ == "__main__":
    firebase = FirebaseDb()
    firebase.add('frases', 'fala aii')
    for key, val in firebase.ref.child('frases').get().items():
        print(val)
        