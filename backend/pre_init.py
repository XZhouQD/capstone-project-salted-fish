#!/usr/bin/python3

'''
IMPORTANT:
This script will drop all tables in database and re-create it, which means
that all existing data will be deleted.
Use with CAUTION!
'''

from db import create_conn

conn = create_conn()

# admin table
query = 'drop table if exists admin;'
conn.execute(query)
query = 'CREATE TABLE admin (ID INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(50) DEFAULT NULL, email VARCHAR(256) DEFAULT NULL, password VARCHAR(64), create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (`id`));'
conn.execute(query)
