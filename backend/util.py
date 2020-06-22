#!/usr/bin/python3

import re

def check_email(email):
    pattern = '^[\w-]+@[\w-]+\.[\w-]+$'
    vaild = re.findall(pattern,email)
    return len(vaild)
