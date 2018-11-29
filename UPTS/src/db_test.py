import requests
import json
import mysql.connector as mysql
from mysql.connector import errorcode



DB_NAME = 'employees'






class dbConn():

    cnx = ""
    cursor = ""

    def __init__(self):

        req_code = requests.get('http://cgu.edu')
        print('\n\n')
        print('Hello World!')
        print('req_code: ' + str(req_code))
        print('\n\n')

    def create_database(cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

        try:
            cursor.execute("USE {}".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print("Database {} created successfully.".format(DB_NAME))
                cnx.database = DB_NAME
            else:
                print(err)
                exit(1)

    def conDB(self):
        print('\n\n')
        print('Connecting to DB')
        self.cnx = mysql.connect(user='root', password='R00tpass',
                                 host='134.173.236.104',
                                 database='upts_s1')
        self.cursor = self.cnx.cursor()

    def closeDB(self):
        self.cursor.close()
        self.cnx.close()

    def getUsers(self):

        self.conDB()
        query = ("SELECT * FROM users")
        self.cursor.execute(query)
        for (username) in self.cursor:
            print("{}".format(username))
        self.closeDB()

    def addUser(self, un, pw):

        self.conDB()
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (un, pw)
        self.cursor.execute(sql, val)

        self.cnx.commit()

        print("1 record inserted, ID:", self.cursor.lastrowid)
        self.closeDB()


thisConn = dbConn()
thisConn.getUsers()
aUser, aPass = input("Enter username and pw: ").split(',')
thisConn.addUser(aUser, aPass)


# print('\n\n')
# print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))













"""
# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
"""


import requests
import json
import sqlite3
import pytest
import datetime


sqlite_master = 'upts_main.db'

def uptsConn():
    conn = sqlite3.connect(sqlite_master)
    conStatus = conn.Error 
    print ("Connected = " + str(conStatus))
    return conn, conStatus


def createTable(conn):

    c = conn.cursor()

    try:
        # Create table
        c.execute('''CREATE TABLE users
                    (username, password)''')
        conn.commit()
        print('created users table')

    except Exception as identifier:
        print(str(identifier))
        # dropTable(conn)


def dropTable(conn):

    c = conn.cursor()

    c.execute('''DROP TABLE users''')
    conn.commit()
    print('Table users dropped')



conn, conStatus = uptsConn()
c = conn.cursor()

# Check if the table exists
if c.execute("""select count(*) from sqlite_master where type='table' and name='users'""") != 1:
    createTable(conn)

# Insert a row of data
c.execute("INSERT INTO users VALUES ('will','willtest')")

c.execute("SELECT * FROM users")
print(c.fetchall())


# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()