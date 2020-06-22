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

import jwt
import json
from functools import wraps
from flask import Flask, request
from flask_restplus import fields, inputs, reqparse
from sqlalchemy import create_engine
from time import time
from itsdangerous import JSONWebSignatureSerializer, BadSignature, SignatureExpired
import re

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)