
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
def userfind():
    cred = credentials.Certificate
    cred = credentials.Certificate("codingpotato-6daf2-firebase-adminsdk-xus8a-0ee585eb0c.json")
    firebase_admin.initialize_app(cred)
    # Use the application default credentials
    # cred = credentials.ApplicationDefault()
    # firebase_admin.initialize_app(cred, {
    #     'projectId': codingpotato-6daf2,
    # })
    #
    db = firestore.client()
    print(db)
    users_ref = db.collection(u'area')
    docs = users_ref.stream()
    print(docs)
    for doc in docs:
        print(u'{}=>{}'.format(doc.id, doc.to_dict()))