import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("src/snthelpdesk-firebase-adminsdk-npbwg-c515bf9e11.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
increment = firestore.Increment(1)

class firebase():

    # Регистрация пользователя (Записываем в базу)
    def createUser(user_id, first_name, last_name, username_link, username, phone,orgname):
        users = db.collection("clients").document(f"{user_id}")

        users.set({
            'user_id' : f'{user_id}',
            'first_name' : f'{first_name}',
            'last_name' : f'{last_name}',
            'username_link' : f'{username_link}',
            'username' : f'{username}',
            'phone' : f'{phone}',
            'orgname' : f'{orgname}'
        })

    # Проверка регистрации пользователя
    def regCheck(user_id):
        users = db.collection("clients").document(f"{user_id}")

        reg = users.get()
        if reg.exists:
            return True
        else:
            return False


    # Перезаписываем имя пользователя в БД
    def updateUserName(username,user_id):
        users = db.collection("clients").document(f"{user_id}")

        users.update({
            'username' : f'{username}'
        })

    # Перезаписываем номер телефона пользователя в БД
    def updateUserPhone(phone,user_id):
        users = db.collection("clients").document(f"{user_id}")

        users.update({
            'phone' : f'{phone}'
        })

    # Берем номер телефона пользователя из БД
    def getUserPhone(user_id):
        users = db.collection("clients").document(f"{user_id}")

        doc = users.get()
        phones = doc.to_dict()
        return phones["phone"]

    # Берем имя пользователя из БД
    def getUserName(user_id):
        users = db.collection("clients").document(f"{user_id}")

        doc = users.get()
        username = doc.to_dict()
        return username["username"]

    # Берем имя организации пользователя из БД
    def getOrgName(user_id):
        users = db.collection("clients").document(f"{user_id}")

        doc = users.get()
        org_name = doc.to_dict()
        return org_name["orgname"]

    # Создаем новый ID заявки пользователя из БД
    def getTiketId():
        tikets = db.collection("counts").document(f"tikets count")

        doc = tikets.get()
        tiket_id = doc.to_dict()

        tiket_count = tiket_id["next_tiket"] + 1

        tikets.update({
            'next_tiket' : tiket_count
        })

        return tiket_id["next_tiket"]

    # Регистрация заявки в БД
    def createTiket(user_id, user_name, username_link, phone, text, trello_id,tiket_id,date):

        users = db.collection("tikets").document(f"{tiket_id}")
        users.set({
            'user_id' : f'{user_id}',
            'username_link' : f'{username_link}',
            'username' : f'{user_name}',
            'phone' : f'{phone}',
            'text_tikets' : f'{text}',
            'trello_id' : f'{trello_id}',
            'created time' : f'{date}'
        })

    # Берем user_id по номеру заявки
    def getUserId(tiket_id):
        tiket_id = db.collection("tikets").document(f"{tiket_id}")

        doc = tiket_id.get()
        user_id = doc.to_dict()
        return user_id["user_id"]