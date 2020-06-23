#!/usr/bin/python3

'''
UNSW COMP9900 20T2
Capstone Project
Team Salted Fish
Members
Xiaowei Zhou    z5108173
Keyu Yang       z5177443
Lisha Jing      z5243620
Nan Zhao        z5225777
Qingbei Wu      z5222641
'''

import json
from functools import wraps
from flask import Flask, request
from flask_restplus import Api, abort, fields, inputs, reqparse, marshal
from itsdangerous import JSONWebSignatureSerializer, BadSignature
import re

from db import create_conn
from auth_token import AuthToken
from util import check_email, CorsResource

from users.admin import Admin
from users.dreamer import Dreamer
from users.collaborator import Collaborator

app = Flask(__name__)
api = Api(app, authorizations={
    'API-KEY': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'AUTH_KEY'
    },
}, security='API-KEY', default='Dream_Matchmaker', title='Dream Matchmaker', description='Dream Matchmaker, a project posting and collaborator finding system')

# Auth Token
SECRET = "DREAM MATCHMAKER, POWERED BY TEAM SALTED FISH"
expires = 3600
auth = AuthToken(SECRET, expires)

# Auth decorator
def require_auth(f):
    @wraps(f)
    def func(*args, **kwarps):
        token = request.headers.get('AUTH_KEY')
        if not token:
            abort(401, 'Auth Token Missing')
        try:
            userinfo = auth.validate(token)
        except Exception as e:
            abort(401, e)
        return f(*args, **kwargs)

    return func

# Get Parsers

# Post Models
login_model = api.model('Login', {
    'email': fields.String(required=True, description='Your email address'),
    'password': fields.String(required=True, description='Your password', min_length=8),
    'role': fields.String(required=True, description='Admin, Dreamer, Collaborator', enum=['Admin','Dreamer','Collaborator'])
})

dreamer_register_model = api.model('Dreamer_Register', {
    'name': fields.String(required=True, description='Your name'),
    'email': fields.String(required=True, description='Your email address'),
    'password': fields.String(required=True, description='Your password', min_length=8),
    'repeat_password': fields.String(required=True, description='Repeat your password', min_length=8),
    'phone_no': fields.String(required=False, description='Phone number (optional)')
})

collaborator_register_model = api.model('Collaborator_Register', {
    'name': fields.String(required=True, description='Your name'),
    'email': fields.String(required=True, description='Your email address'),
    'password': fields.String(required=True, description='Your password', min_length=8),
    'repeat_password': fields.String(required=True, description='Repeat your password', min_length=8),
    'phone_no': fields.String(required=False, description='Phone number (optional)'),
    'education': fields.Integer(required=False, description='Education, 1=Other, 2=Bachelor, 3=Master, 4=PhD'),
    'skills': fields.String(required=False, description='skills(as integer) and experience (in years). Format: skill:exp,skill:exp,skill:exp,...', example='1:3,2:2,3:1')
})


@api.route('/collaborator/register')
class CollaboratorRegister(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Register Failed')
    @api.doc(description='Register a new collaborator')
    @api.expect(collaborator_register_model, validate=True)
    def post(self):
        register_info = request.json
        name = register_info['name']

        email = register_info['email']
        if not check_email(email):
            return {'message': 'Email not valid.'}, 400

        if Collaborator.is_email_exist(conn, email):
            return {'message': 'Email already registered.'}, 400

        password = register_info['password']
        if password != register_info['repeat_password']:
            return {'message': 'Passwords not match.'}, 400

        try:
            phone_no = register_info['phone_no']
        except:
            phone_no = ''

        try:
            education = register_info['education']
        except:
            education = -1

            skill_dict = {}
        try:
            skill_exp_pairs = register_info['skills'].split(',')
            for str in skill_exp_list:
                skill_exp = str.split(':')
                skill_dict[skill_exp[0]]=skill_exp[1]
        except:
            skill_dict = {}

        Collaborator(name, email, password_plain=password, phone_no=phone_no, education=education, skill_dict=skill_dict).commit(conn)

        return {'message': 'Register success'}, 200

@api.route('/dreamer/register')
class DreamerRegister(CorsResource):
    @api.response(200, 'Success')
    @api.response(400, 'Register Failed')
    @api.doc(description='Register a new dreamer')
    @api.expect(dreamer_register_model, validate=True)
    def post(self):
        register_info = request.json
        name = register_info['name']

        email = register_info['email']
        if not check_email(email):
            return {'message': 'Email not valid.'}, 400

        if Dreamer.is_email_exist(conn, email):
            return {'message': 'Email already registered.'}, 400

        password = register_info['password']
        if password != register_info['repeat_password']:
            return {'message': 'Passwords not match.'}, 400

        try:
            phone_no = register_info['phone_no']
        except:
            phone_no = ''

        Dreamer(name, email, password_plain=password, phone_no=phone_no).commit(conn)

        return {'message': 'Register success'}, 200

@api.route('/login')
class Login(CorsResource):
    @api.response(200, 'Success')
    @api.response(401, 'Login Failed')
    @api.doc(description='Login with email and password, receive an auth token')
    @api.expect(login_model, validate=True)
    def post(self):
        login_info = request.json
        email = login_info['email']
        password = login_info['password']
        # try login based on role
        role = login_info['role']
        if role == 'Admin':
            user = Admin.login(conn, email, password)
        elif role == 'Dreamer':
            user = Dreamer.login(conn, email, password)
        elif role == 'Collaborator':
            user = Collaborator.login(conn, email, password)
        # login failed
        if user is None:
            return {'message': 'Login failed for incorrect credentials.'}, 401
        else:
            token = auth.token(user).decode()
            return {'token': token}, 200


if __name__ == '__main__':
    conn = create_conn()
    app.run(debug=True)
