#!/usr/bin/python3

import re
from flask_restplus import Resource

def check_email(email):
    pattern = '^[\w-]+@[\w-]+\.[\w-]+$'
    vaild = re.findall(pattern,email)
    return len(vaild)

class CorsResource(Resource):
    def options(self):
        return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
                                     'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
                                     'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With, Auth_Key'
                                    }
