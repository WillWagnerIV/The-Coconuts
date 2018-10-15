import requests
import json
import mysql.connector as mysql


class UserCon():

    cnx = ""
    cursor = ""

    def __init__(self):
        print('\n')

    def OpenDB(self):
        print('\n')
        print('Connecting to DB \n')
        self.cnx = mysql.connect(user='program_user', password='Pr0gpass',
                                 host='localhost',
                                 database='upts_s1')
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
                                 host='127.0.0.1',
                                 database='upts_s1')
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


MainLoop()
# print('\n\n')
# print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))
