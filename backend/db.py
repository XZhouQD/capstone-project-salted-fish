#!/usr/bin/python3
import yaml
from sqlalchemy import create_engine

def create_conn():
    f = open('db.config', 'r', encoding='utf-8')
    config = yaml.load(f.read(), Loader=yaml.FullLoader)
    full_address = f"mysql+pymysql://{config['MySQL']['Username']}:{config['MySQL']['Password']}@{config['MySQL']['Address']}:{config['MySQL']['Port']}/{config['MySQL']['Database']}"
    #engine = create_engine('mysql+pymysql://comp9900:not_tasty@ali.x-zhou.com:3306/salted_fish')
    engine = create_engine(full_address)
    conn = engine.connect()
    return conn

