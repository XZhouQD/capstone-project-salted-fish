#!/usr/bin/python3

from users.util import sha256

class Admin():
    def __init__(self, name, email, password_plain='', password_encrypted='', id='', create_time='', last_update=''):
        self.name = name
        self.email = email.lower()
        if password_encrypted == '':
            self.password_encrypted = sha256(password_plain)
        else:
            self.password_encrypted = password_encrypted
        self.id = id
        self.create_time = create_time
        self.last_update = last_update

    @staticmethod
    def login(conn, email, password_plain='', password_encrypted=''):
        email = email.lower()
        query = "select * from admin where email = \'" + email + "\';"
        result = conn.execute(query)
        if result.rowcount == 0:
            return None
        row = result.fetchone()
        if password_encrypted == '':
            enc_pass = sha256(password_plain)
        else:
            enc_pass = password_encrypted
        if enc_pass == row['password']:
            return Admin(row['name'], row['email'], password_encrypted=row['password'], id=row['ID'], create_time=row['create_time'], last_update=row['last_update']).info()
        return None
   
    @staticmethod
    def check_password(conn, email, password_plain='', password_encrypted=''):
        email = email.lower()
        query = "select * from admin where email = \'" + email + "\';"
        result = conn.execute(query)
        row = result.fetchone()
        if password_encrypted == '':
            enc_pass = sha256(password_plain)
        else:
            enc_pass = password_encrypted
        if enc_pass == row['password']:
            return True
        return False

    @staticmethod
    def commit_newpassword(conn, email,new_password):
        email = email.lower()
        query = "UPDATE admin set password_plain = new_password ,password_encrypted = sha256(new_password) where email = \'" + email + "\';"
        conn.execute(query)

    def info(self):
        return {'role': 'Admin', 'name': self.name, 'email': self.email, 'id': self.id, 'creation_time': self.create_time, 'last_update': self.last_update}

    def commit(self, conn):
        query = "INSERT INTO admin (name, email, password) VALUES (\'" + self.name + "\', \'" + self.email + "\', \'" + self.password_encrypted + "\') ON DUPLICATE KEY UPDATE `name`= \'" + self.name + "\', `password` = \'" + self.password_encrypted + "\';"
        conn.execute(query)
