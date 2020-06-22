#!/usr/bin/python3

from sqlalchemy import create_engine

def create_conn():
    engine = create_engine('mysql+pymysql://comp9900:not_tasty@ali.x-zhou.com:3306/salted_fish')
    conn = engine.connect()
    return conn

