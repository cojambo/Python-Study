import sqlite3

#create connection
def dbconection():
    path = 'C:/Users/erikv/Documents/repositorios GitHub/Python-Study/Database/diary'
    con = None
    try:
        con = sqlite3.connect(path)
    except OSError as er:
        print(er)
    return con

#Create Table
vcon=dbconection()

vsql='''CREATE TABLE tb_contacts(
            N_CONTACTID INTEGER PRIMARY KEY AUTOINCREMENT,
            T_CONTACTNAME VARCHAR(30),
            T_CONTACTNUMBER VARCHAR(14),
            T_CONTACTEMAIL VARCHAR(30)

);'''

def createtb(conection, sql):
    try:
        c = conection.cursor()
        c.execute(sql)
        print('Tabela criada')

    except OSError as ex:
        print(ex)

createtb(vcon, vsql)