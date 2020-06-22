#!/usr/bin/python3

import hashlib

def sha256(hash_string):
    m = hashlib.sha256()
    m.update(hash_string.encode())
    return m.hexdigest()
