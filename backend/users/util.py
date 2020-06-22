#!/usr/bin/python3

import hashlib
import re

def sha256(hash_string):
    m = hashlib.sha256()
    m.update(hash_string.encode())
    return m.hexdigest()

def check_email(email):
    pattern = '^[\w-]+@[\w-]+\.[\w-]+$'
    vaild = re.findall(pattern,email)
    return len(vaild)
