import requests
import json
import mysql.connector as mysql


class dbConn():

    cnx = ""
    cursor = ""

    def __init__(self):

        req_code = requests.get('http://cgu.edu')
        print('\n\n')
        print('Hello World!')
        print('req_code: ' + str(req_code))
        print('\n\n')

    def conDB(self):
        print('\n\n')
        print('Connecting to DB')
        self.cnx = mysql.connect(user='root', password='R00tpass',
                                 host='127.0.0.1',
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
