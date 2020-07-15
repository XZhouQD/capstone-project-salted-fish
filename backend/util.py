#!/usr/bin/python3

import re
from flask_restplus import Resource

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(file):
    return '.' in file and file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_email_local(local):
    pattern = '^([a-zA-Z0-9]([-]*[a-zA-Z0-9])*[\\.])*[a-zA-Z0-9]([-]*[a-zA-Z0-9])*$'
    valid = re.findall(pattern, local)
    return len(valid)

def check_email_domain(domain):
    pattern = '^([a-zA-Z0-9]([-]*[a-zA-Z0-9])*[\\.])+[a-zA-Z0-9]([-]*[a-zA-Z0-9])*$'
    valid = re.findall(pattern, domain)
    return len(valid)

def check_email(email):
    email_split = email.split('@', 1)
    return check_email_local(email_split[0]) and check_email_domain(email_split[1])

class CorsResource(Resource):
    def options(self):
        return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
                                     'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
                                     'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With, Auth_Key'
                                    }
