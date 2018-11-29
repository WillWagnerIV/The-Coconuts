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
table_name = ""

def uptsConn():
    conn = sqlite3.connect(sqlite_master)
    conStatus = conn.Error 
    print ("Connected = " + str(conStatus))
    return conn, conStatus


def createTable(conn,table_name,table_columns):
    c = conn.cursor()
    colCount = 0
    try:
        # Create table
        print (table_columns)
        sqlStatement = 'CREATE TABLE '+ table_name + ' ('
        for col_Name in table_columns:
            sqlStatement += col_Name
            if colCount < len (table_columns) - 1:
                sqlStatement += ', '
                colCount += 1
        sqlStatement += ')'
        print ('sql statement: ' + str(sqlStatement))

        c.execute(sqlStatement)
        conn.commit()
        print('created ' + table_name + ' table')

    except Exception as identifier:
        print(str(identifier))
        # dropTable(conn, 'users')


def dropTable(conn, table_name):

    c = conn.cursor()

    c.execute('''DROP TABLE users''')
    conn.commit()
    print('Table users dropped')


def commit_close(conn):

    # Save (commit) the changes
    conn.commit()
    # Close the connection
    conn.close()


conn, conStatus = uptsConn()
c = conn.cursor()

# Check if the table exists
if c.execute("""select count(*) from sqlite_master where type='table' and name='users'""") == 1:
    dropTable(conn, 'users')


createTable(conn, 'users', ['username','password'])

# Insert a row of data
c.execute("INSERT INTO users VALUES ('will','willtest')")







c.execute("SELECT * FROM users")
print(c.fetchall())



commit_close(conn)















class UserCon():

    cnx = ""
    cursor = ""

    def __init__(self):
        print('\n')

    def OpenDB(self):
        print('\n')
        print('Connecting to DB \n')
        self.cnx = mysql.connect(user='program_user', password='Pr0gpass',
                                 host='134.173.236.104',
                                 database='coco_upts')
        self.cursor = self.cnx.cursor()

    def CloseDB(self):
        self.cursor.close()
        self.cnx.close()
        print()
        print('Connection Closed')

    def GetUsers(self):

        self.OpenDB()
        query = ("SELECT * FROM users")
        self.cursor.execute(query)
        for (username) in self.cursor:
            print("{}".format(username))
        self.CloseDB()

    def AddUser(self, un, pw):

        self.OpenDB()
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (un, pw)
        self.cursor.execute(sql, val)

        self.cnx.commit()

        print("1 record inserted, ID:", self.cursor.lastrowid)
        self.CloseDB()

    def SignIn(self, un, pw):
        print('Need to add code to validate')


class PlayerCon():

    cnx = ""
    cursor = ""

    def __init__(self):
        print('\n')

    def OpenDB(self):
        print('\n')
        print('Connecting to DB \n')
        self.cnx = mysql.connect(user='program_user', password='Pr0gpass',
                                 host='134.173.236.104',
                                 database='coco_upts')
        self.cursor = self.cnx.cursor()

    def CloseDB(self):
        self.cursor.close()
        self.cnx.close()
        print()
        print('Connection Closed')

    def GetPlayers(self, un):

        self.OpenDB()
        sql = "SELECT * FROM players WHERE username = '" + un + "'"
        val = un
        self.cursor.execute(sql)
        for (player_name) in self.cursor:
            print("{}".format(player_name))
        self.CloseDB()

    def AddPlayer(self, un, pn):

        self.OpenDB()
        sql = "INSERT INTO players (username, player_name) VALUES (%s, %s)"
        val = (un, pn)
        self.cursor.execute(sql, val)
        self.cnx.commit()

        print("1 record inserted, ID:", self.cursor.lastrowid)
        self.CloseDB()


#  Menus
#  Login Menu
def LoginMenu():
    thisConn = UserCon()
    loggingIn = True

    while (loggingIn):
        print()
        print('       ###   Login Menu   ###')
        print()
        print(' 1 - Sign In')
        print(' 2 - New User')
        print(' 3 - Recover Credentials')
        print(' 0 - Quit')
        print()

        menuChoice = input(' Selection: ')

        if menuChoice in ("1", "2", "3"):
            print()

        if menuChoice == '0':
            loggingIn = False
            return "Quit"
            break

        elif menuChoice == '1':
            aUser, aPass = input(
                "Enter Username and Password (Username, Password): ").split(',')
            thisConn.SignIn(aUser, aPass)
            return aUser

        elif menuChoice == '2':
            aUser, aPass = input(
                "Enter new Username and Password (Username, Password): ").split(',')
            thisConn.AddUser(aUser, aPass)

        elif menuChoice == '3':
            UserRecover()

        elif menuChoice == '4':
            thisConn.GetUsers()

        else:
            print()
            print('Please choose one of the options above.')
            print()


#  Player Menu
def PlayerMenu(aUser):
    thisConn = PlayerCon()
    PlayerMenuing = True

    while (PlayerMenuing):
        print()
        print('       ###   Player Menu   ###')
        print()
        print(' 1 - List My Players')
        print(' 2 - Add a Player')
        print(' 3 - Remove a Player')
        print(' 4 - Edit a Player')
        print(' 0 - Return to Main Menu')
        print()

        menuChoice = input(' Selection: ')

        if menuChoice in ("1", "2", "3", "4"):
            print()

        if menuChoice == '0':
            PlayerMenuing = False
            break

        elif menuChoice == '1':
            thisConn.GetPlayers(aUser)

        elif menuChoice == '2':
            aName = input(
                "Enter new Player Name: ")
            thisConn.AddPlayer(aUser, aName)

        elif menuChoice == '3':
            print('remove player')

        elif menuChoice == '4':
            print('Edit a Player')

        else:
            print()
            print('Please choose one of the options above.')
            print()


#  Main Loop
def MainLoop():
    mainLooping = True
    thisUser = ""
    thisConn = UserCon()

    while (mainLooping):

        # Call the LoginMenu
        if thisUser == "":
            thisUser = LoginMenu()
            print(thisUser)
            if thisUser == 'Quit':
                mainLooping = False
                break

        # Main 3 Choices

        print()
        print('       ###   Main Menu   ###')
        print()
        print(' 1 - Players Menu')
        print(' 2 - Games Menu')
        print(' 3 - Reports Menu')
        print(' 0 - Quit')
        print()
        menuChoice = input(' Selection: ')

        if menuChoice in ("1", "2", "3", "4"):
            print()
        if menuChoice == '0':
            mainLooping = False
            break
        elif menuChoice == '1':
            PlayerMenu(thisUser)
        elif menuChoice == '2':
            print('Need to add Game Menu')
        elif menuChoice == '3':
            print('Need to add Reports Menu \n')
            thisConn.GetUsers()
        elif menuChoice == '4':
            ListPlayers()
        else:
            print()
            print('Please choose one of the options above.')
            print()


# MainLoop()


@pytest.mark.xfail
def test_login():
    UserCon.OpenDB(UserCon)
    aUser = "asdf"
    aPass = "kjhkljh"
    assert UserCon.SignIn(UserCon, aUser, aPass) == "asdf"
    UserCon.CloseDB(UserCon)


@pytest.mark.xfail
def test_new_user():
    un = "TestUser"+str(datetime.datetime)
    pw = "kjhkljh"
    UserCon.OpenDB(UserCon)
    assert UserCon.AddUser(UserCon, un, pw) == UserCon.cursor.lastrowid
    self.CloseDB()


@pytest.mark.xfail
def test_list_users():
    assert 1 == 5


@pytest.mark.xfail
def test_list_players():
    assert 1 == 5


@pytest.mark.xfail
def test_add_player():
    assert 1 == 5

# print('\n\n')
# print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))


# conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
