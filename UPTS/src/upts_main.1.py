import requests
import json
import mysql.connector as mysql
from mysql.connector import errorcode
import sqlite3
import pytest
import datetime



db_master = 'upts_s1'
db_host = '127.0.0.1'
db_user='prog_user'
db_password='pr0gpass'
table_name = ""


# NOT WORKING - Included for Reference
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


# Open Database Connection and Print Confirmation
# Report Error then Close Connection
def openDB_test():
    
    try:
        cnx = mysql.connect(user=db_user, password=db_password,
                                    host=db_host,
                                    database=db_master)
        print ('Connection Opened')
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


# Open Database Connection or Report Error - Does not Close Connection
def OpenDB():

    try:
        cnx = mysql.connect(user=db_user, password=db_password,
                                    host=db_host,
                                    database=db_master)
        print('Connection Opened')
        return cnx
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            return err


# Close Database Connection
def CloseDB(cnx):
    c = cnx.cursor()
    c.close()
    cnx.close()
    print('Connection Closed')



# Create a Table - Pass table_columns as a list
def createTable(cnx,table_name,table_columns):
    c = cnx.cursor()
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
        cnx.commit()
        print('created ' + table_name + ' table')

    except Exception as identifier:
        print(str(identifier))
        # dropTable(cnx, 'users')



# users table connections
class UserCon():
    
    def __init__(self):
        print('\n')

    def GetUsers():

        cnx = OpenDB()
        cursor = cnx.cursor()
        query = ("SELECT * FROM users")
        cursor.execute(query)
        for (username) in cursor:
            print("{}".format(username))
        CloseDB(cnx)

    def AddUser(un, pw):

        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (un, pw)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        CloseDB(cnx)

    def SignIn(un, pw):

        print('Trying to Validate')
        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = 'SELECT * FROM users WHERE username = "' + un + '"'
        # print (sql)
        cursor.execute(sql)
        for response in cursor:
            if response[2] == pw:
                CloseDB(cnx)
                return "Valid"
            else:
                CloseDB(cnx)
                return "Invalid Username or Password"


class PlayerCon():

    def __init__(self):
        print('\n')


    def GetPlayers(un):
        players = []
        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "SELECT * FROM players WHERE username = '" + un + "'"
        val = un
        cursor.execute(sql)
        for (player_name) in cursor:
            print("{}".format(player_name))
            players.append(player_name)
        CloseDB(cnx)
        return players


    def AddPlayer(un, pn):

        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "INSERT INTO players (username, player_name) VALUES (%s, %s)"
        val = (un, pn)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        CloseDB(cnx)

    def removePlayer(player):

        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "DELETE FROM `upts_s1`.`players` WHERE (`idplayers` = '"
        sql += str(player[0]) + "')"
        print (sql)
        cursor.execute(sql)
        cnx.commit()
        print("1 record removed.")
        CloseDB(cnx)


class GameCon():

    def __init__(self):
        print('\n')

    def GetGames(un):

        players = []
        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "SELECT * FROM games WHERE username = '" + un + "'"
        val = un
        cursor.execute(sql)
        for (player_name) in cursor:
            print("{}".format(player_name))
            players.append(player_name)
        CloseDB(cnx)
        return players

    def AddGame(un, pn):

        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "INSERT INTO players (username, player_name) VALUES (%s, %s)"
        val = (un, pn)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        CloseDB(cnx)

    def removeGame(player):

        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "DELETE FROM `upts_s1`.`players` WHERE (`idplayers` = '"
        sql += str(player[0]) + "')"
        print (sql)
        cursor.execute(sql)
        cnx.commit()
        print("1 record removed.")
        CloseDB(cnx)




#  Menus
#  Login Menu
def LoginMenu():
    loggingIn = True
    # cnx = OpenDB()
    # cursor = cnx.cursor()

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

        elif menuChoice == '1':
            aUser, aPass = input(
                "Enter Username and Password (Username, Password): ").split(',')
            userVal = UserCon.SignIn(aUser, aPass)
            if userVal == None:
                CloseDB(cnx)
            elif userVal == "Valid":
                loggingIn = False
                return aUser
            else:
                print (userVal)
            

        elif menuChoice == '2':
            aUser, aPass = input(
                "Enter new Username and Password (Username, Password): ").split(',')
            UserCon.AddUser(aUser, aPass)

        elif menuChoice == '3':
            UserCon.UserRecover()

        elif menuChoice == '4':
            UserCon.GetUsers()

        else:
            print()
            print('Please choose one of the options above.')
            print()


#  Player Menu
def PlayerMenu(aUser):
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

        if menuChoice == '0':                               # Main Menu
            PlayerMenuing = False
            break

        elif menuChoice == '1':                             # List Players
            PlayerCon.GetPlayers(aUser)

        elif menuChoice == '2':                             # Add a Player
            aName = input(
                "Enter new Player Name: ")
            PlayerCon.AddPlayer(aUser, aName)

        elif menuChoice == '3':                             # Remove a Player
            print ('Player Key | Player Information')
            players_list = PlayerCon.GetPlayers(aUser)
            pk = int(input ('Enter Player Key: '))
            for player in players_list:
                if pk == player[0]:
                    print ('Are you sure you want to remove ' + str(player))
                    double_check = input ('Enter 0 to Confirm Delete - There is no reversing this action!')
                    if double_check == '0':
                        PlayerCon.removePlayer (player)

        elif menuChoice == '4':                             # Edit a Player
            print('Edit a Player')

        else:
            print()
            print('Please choose one of the options above.')
            print()


#  Main Loop
def MainLoop():
    mainLooping = True
    thisUser = ""

    while (mainLooping):

        # Call the LoginMenu
        if thisUser == "":
            thisUser = LoginMenu()
            print ()
            print("User: ",thisUser)
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
            UserCon.GetUsers()
        elif menuChoice == '4':
            PlayerCon.ListPlayers()
        else:
            print()
            print('Please choose one of the options above.')
            print()


MainLoop()


@pytest.mark.xfail
def test_login():
    OpenDB(UserCon)
    aUser = "asdf"
    aPass = "kjhkljh"
    assert UserCon.SignIn(UserCon, aUser, aPass) == "asdf"
    CloseDB(UserCon)


@pytest.mark.xfail
def test_new_user():
    un = "TestUser"+str(datetime.datetime)
    pw = "kjhkljh"
    OpenDB(UserCon)
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


# cnx.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
