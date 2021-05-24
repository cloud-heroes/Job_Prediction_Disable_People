import pyrebase

config = {
       "apiKey": "AIzaSyB3htC9IrXYXueaGAGHSZ_uKS76WauFHqY",
    "authDomain": "job-pred.firebaseapp.com",
    "databaseURL": "https://job-pred-default-rtdb.firebaseio.com",
    "storageBucket": "job-pred.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# lx = []


def login1(email, password):
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        return True

    except:
        # print("Invalid email or password")
        return False


def userNameExtract(username):
    lx = []
    for i in str(username):
        if i == "@":
            break
        else:
            lx.append(i)

    result = "".join(lx)

    del lx

    return result


def signup1(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return True

    except:
        return False
