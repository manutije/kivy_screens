import bcrypt
from pymongo import MongoClient


def create_usr(name, password,email):
    hashed_password =bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    client = MongoClient("mongodb+srv://screens:1235@screens.jt6a7.mongodb.net/Users?retryWrites=true&w=majority")
    db = client.Users
    collection = db.users
    usr = {"username": name, 
        "password": hashed_password, 
        "email": email}
    collection.insert_one(usr)
    
def login_usr(name, password):
    
    client = MongoClient("mongodb+srv://screens:1235@screens.jt6a7.mongodb.net/Users?retryWrites=true&w=majority")
    db = client.Users
    collection = db.users
    myquery = { "username": name }
    try:
        mydoc = collection.find(myquery)
        for x in mydoc:
            pas =x['password']

        if bcrypt.checkpw(password.encode(), pas):
            return True
        else:
            return False
    except:
        return False

