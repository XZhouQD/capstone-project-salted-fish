#!/usr/bin/python3

'''
IMPORTANT:
This script will drop all tables in database and re-create it, which means
that all existing data will be deleted.
Use with CAUTION!
'''

from db import create_conn

print("Start database pre initialisation")
conn = create_conn()
print("default database connection established")

print("clean all existing tables")

query = 'drop table if exists skills;'
conn.execute(query)

query = 'drop table if exists admin;'
conn.execute(query)

query = 'drop table if exists collaborator CASCADE;'
conn.execute(query)

query = 'drop table if exists dreamer;'
conn.execute(query)

# admin table
print("rebuild admin table...")
query = 'CREATE TABLE admin (ID INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(50) DEFAULT NULL, email VARCHAR(256) DEFAULT NULL, password VARCHAR(64), create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (`id`), UNIQUE KEY (`email`));'
conn.execute(query)

# collaborator table
print("rebuild collaborator table...")
# education: -1 = default, 1 = Other, 2 = bachelor, 3 = master, 4 = PhD
query = 'CREATE TABLE collaborator (ID INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(50) DEFAULT NULL, email VARCHAR(256) DEFAULT NULL, password VARCHAR(64), phone_no VARCHAR(20) DEFAULT NULL, education TINYINT DEFAULT -1, user_level INT(5), description TEXT, create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (`ID`), UNIQUE KEY (`email`));'
conn.execute(query)

# dreamer table
print("rebuild dreamer table...")
query = 'CREATE TABLE dreamer (ID INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(50) DEFAULT NULL, email VARCHAR(256) DEFAULT NULL, password VARCHAR(64), phone_no VARCHAR(20) DEFAULT NULL, user_level INT(5), description TEXT, create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (`ID`), UNIQUE KEY (`email`));'
conn.execute(query)

# skill/exp table
print("rebuild skill/exp table...")
query = 'CREATE TABLE skills (skill TINYINT DEFAULT -1, experience TINYINT DEFAULT 0, collaboratorID int(11) NOT NULL, FOREIGN KEY (`collaboratorID`) REFERENCES collaborator(`ID`));'
conn.execute(query)

print("pre initialisation complete")
