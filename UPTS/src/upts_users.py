import requests
import upts_dbs as upts_db
import mysql.connector as mysql
from mysql.connector import errorcode

# Database Connection Variables
db_master = 'upts_s1'
db_host = '134.173.236.104'
db_user='prog_user'
db_password='Pr0gpass'
db_table = ""


class upts_user():

    # Class Variables
    total_user_count = 0
    allUsers = []
    
    def __init__(self, name = "Default User Name", un = "username", pw = "password", uid = 0):

        self.name = name
        self.user_name = un
        self.pw = pw
        self.uid = uid

        self.loginVal = None
        

    def GetUsers():

        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        query = ("SELECT * FROM users")
        cursor.execute(query)
        for (username) in cursor:
            print("{}".format(username))
        upts_db.CloseDB(cnx)

    def AddUser( un, pw):
        # print ('Should open con from inside Adduser')
        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (un, pw)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        upts_db.CloseDB(cnx)
        return cursor.lastrowid

    def SignIn(un, pw):

        # print('Trying to Validate')
        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        sql = 'SELECT * FROM users WHERE username = "' + un + '"'
        print (sql)
        cursor.execute(sql)
        for response in cursor:
            if response[2] == pw:
                upts_db.CloseDB(cnx)

                session_user = upts_user (name = "Default First Last Name", un = un , pw = pw , uid = response[0])
                session_user.loginVal = "Valid"

                return session_user

            else:
                upts_db.CloseDB(cnx)
                return "Invalid Username or Password"

    def UserRecover():

        print('This is where the screens to assist with credentials would go.')

    def Load_games_from_db (upts_user):

        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        sql = 'SELECT * FROM games_has_users WHERE users_idusers = "' + str(upts_user.uid) + '"'
        cursor.execute(sql)
        for game in cursor:
            games_idgames = game[0]
            users_idusers = game[1]
            sql = 'SELECT * FROM games WHERE idgames = "' + str(games_idgames) + '"'
            cursor.execute(sql)
            for game in cursor:
                print (game[0],game[1])

        upts_db.CloseDB(cnx)
