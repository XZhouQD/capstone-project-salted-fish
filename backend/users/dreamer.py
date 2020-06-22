#!/usr/bin/python3

from users.util import sha256

class Dreamer():
    def __init__(self, name, email, password_plain='', password_encrypted='', id='', create_time='', last_update='', phone_no='', user_level=0, description=''):
        self.name = name
        self.email = email.lower()
        if password_encrypted == '':
            self.password_encrypted = sha256(password_plain)
        else:
            self.password_encrypted = password_encrypted
        self.id = id
        self.phone_no = phone_no
        self.user_level = user_level
        self.description = description
        self.create_time = create_time
        self.last_update = last_update
        self.level_text='Entry'
        if self.user_level >= 20: self.level_text='Expert'
        elif self.user_level >= 10: self.level_text='Professional'
        elif self.user_level >= 5: self.level_text='Senior'
        elif self.user_level >= 3: self.level_text='Medium'


    @staticmethod
    def login(conn, email, password_plain='', password_encrypted=''):
        email = email.lower()
        query = "select * from dreamer where email = \'" + email + "\';"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        if password_encrypted == '':
            enc_pass = sha256(password_plain)
        else:
            enc_pass = password_encrypted
        if enc_pass == row['password']:
            return Dreamer(row['name'], row['email'], password_encrypted=row['password'], id=row['ID'], create_time=row['create_time'], last_update=row['last_update'], phone_no=row['phone_no'], user_level=row['user_level'], description=row['description']).info()
        return None

    @staticmethod
    def is_email_exist(conn, email):
        email = email.lower()
        query = "select * from dreamer where email = \'" + email + "\';"
        result = conn.execute(query)
        return result.rowcount

    @staticmethod
    def getObject(conn, email):
        email = email.lower()
        query = "select * from dreamer where email = \'" + email + "\';"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        return Dreamer(row['name'], row['email'], password_encrypted=row['password'], id=row['ID'], create_time=row['create_time'], last_update=row['last_update'], phone_no=row['phone_no'], user_level=row['user_level'], description=row['description'])

    def info(self):
        return {'role': 'Dreamer', 'name': self.name, 'email': self.email, 'id': self.id, 'creation_time': self.create_time, 'last_update': self.last_update, 'phone_no': self.phone_no, 'user_level': self.level_text, 'description': self.description}

    def commit(self, conn):
        query = "INSERT INTO dreamer (name, email, password, phone_no, user_level, description) VALUES (\'" + self.name + "\', \'" + self.email + "\', \'" + self.password_encrypted + "\', \'" + self.phone_no + "\', " + str(self.user_level) + ", \'" + self.description + "\') ON DUPLICATE KEY UPDATE `name`= \'" + self.name + "\', `password` = \'" + self.password_encrypted + "\', `phone_no` = \'" + self.phone_no + "\', `user_level` = " + str(self.user_level) + ", `description` = \'" + self.description + "\';"
        conn.execute(query)
