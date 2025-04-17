import sqlite3
from sqlite3 import Error
import re

#create connection
def dbconection():
    path = 'C:/Users/erikv/Documents/repositorios GitHub/Python-Study/Database/diary'
    con = None
    try:
        con = sqlite3.connect(path)
    except Error as er:
        print(er)
    return con
'''
name = input('Name: ')
number = input('Number: ')
email = input('Email: ')

vsql = f"""INSERT INTO tb_contacts
            (T_CONTACTNAME, T_CONTACTNUMBER, T_CONTACTEMAIL)
        VALUES('{name}','{number}','{email}')
"""
'''
def insert(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        print('inserted')
    except Error as er:
        print(er)

con = dbconection()
#insert(con, vsql)

def delete(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Deleted')
    except Error as er:
        print(er)

vsql = 'DELETE FROM tb_contacts WHERE N_CONTACTID=3'
#delete(con, vsql)


def update(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Updated')
    except Error as er:
        print(er)

vsql = 'UPDATE tb_contacts SET T_CONTACTNAME="Bruno" WHERE N_CONTACTID=2'
#update(con, vsql)


def consult(connection, sql):
    c = connection.cursor()
    c.execute(sql)
    result = c.fetchall()
    return result

vsql = 'SELECT * FROM tb_contacts'

res = consult(con, vsql)

for r in res:
    one = re.sub(',',' |',str(r))
    two = re.sub(' ','',str(one))
    three = re.sub("'"," ",str(two))
    print(three)