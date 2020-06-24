#!/usr/bin/python3
from time import time
import jwt
from itsdangerous import SignatureExpired

class AuthToken:
    def __init__(self, secret, expire):
        self.secret = secret
        self.expire = expire

    def decode(self, token):
        return jwt.decode(token, self.secret, algorithm='HS256')

    def token(self, userinfo):
        info = {'email': userinfo['email'], 'id': userinfo['id'], 'role': userinfo['role'], 'time': time()}
        return jwt.encode(info, self.secret, algorithm='HS256')

    def validate(self, token):
        info = jwt.decode(token, self.secret, algorithm='HS256')
        if time() - info['time'] > self.expire:
            raise SignatureExpired("The token has been expired")
        return info

    def refresh(self, token):
        # refresh token time
        info = self.validate(token)
        info['time'] = time()
        return jwt.encode(info, self.secret, algorithm='HS256')
