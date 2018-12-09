import requests
from io import StringIO
import json
import mysql.connector as mysql
from mysql.connector import errorcode
import sqlite3
import pytest
import datetime
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import pprint
import sys


# Database Connection Variables
db_master = 'upts_s1'
db_host = '134.173.236.104'
db_user='prog_user'
db_password='Pr0gpass'
db_table = ""

class upts_game():

    # Class Variables
    total_game_count = 0
    allGames = []

    def __init__(self, game_name='none', game_notes='none', game_currency='none', game_trophies='none', game_ach='none', game_items='none'):
        print('Initialized Game')
        self.game_name = game_name
        self.game_notes = game_notes
        self.game_currency = game_currency
        self.game_trophies = game_trophies
        self.game_ach = game_ach
        self.game_items = game_items

        self.total_game_count += 1
        self.allGames.append(self.game_name)

    def convert_class_to_dict(self):
        game_name = self.game_name
        game_notes = self.game_notes
        game_currency = self.game_currency
        game_trophies = self.game_trophies
        game_ach = self.game_ach
        game_items = self.game_items
        class_dict = { game_name : [
            {'game_name' : game_name},
            {'game_notes' : game_notes},
            {'game_currency' : game_currency},
            {'game_trophies' : game_trophies},
            {'game_ach' : game_ach},
            {'game_items' : game_items}
        ]
        }
        print (class_dict)
        return class_dict

    def make_Pandas(self, datadict):
        dataframe = pd.DataFrame(datadict)
        print('DataFrame:')
        print(dataframe)
        return dataframe

    def save_json_pd(self):
        print ('Saving game json file')
        datadict = self.convert_class_to_dict()
        pd_dataframe = self.make_Pandas(datadict)
        json_name = "json/" + self.game_name + ".json"
        with open(json_name, 'w') as f:
            f.write(pd_dataframe.to_json(orient='records', lines=True))

    def load_json_pd(self):
        json_name = "json/" + self.game_name + ".json"
        dataframe = pd.read_json(json_name, orient='records', lines=True)
        print(dataframe)
        return dataframe

    def save_game_to_db(self):
        pass

# ----------  START DATABASE FUNCTIONS

class upts_db():
    # Create Database - NOT WORKING YET - Included for Reference
    def create_database(cursor):
        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_master))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

        try:
            cursor.execute("USE {}".format(db_master))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(db_master))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print("Database {} created successfully.".format(db_master))
                cnx.database = db_master
            else:
                print(err)
                exit(1)


    # Open Database Connection and Print Confirmation
    # Report Error then Close Connection
    def open_test_close():
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
            print ('Connection Closed')


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

    # ----------  START DATABASE TABLE FUNCTIONS

    # Create a Table - Pass table_columns as a list
    def createTable(cnx,db_table,table_columns):
        c = cnx.cursor()
        colCount = 0
        try:
            # Create table
            print (table_columns)
            sqlStatement = 'CREATE TABLE '+ db_table + ' ('
            for col_Name in table_columns:
                sqlStatement += col_Name
                if colCount < len (table_columns) - 1:
                    sqlStatement += ', '
                    colCount += 1
            sqlStatement += ')'
            print ('sql statement: ' + str(sqlStatement))

            c.execute(sqlStatement)
            cnx.commit()
            print('created ' + db_table + ' table')

        except Exception as identifier:
            print(str(identifier))
            # dropTable(cnx, 'users')

# ----------  START TABLECONS

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

    def UserRecover():

        print('This is where the screens to assist with credentials would go.')


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

    # Class Variables
    # none

    def __init__(self):
        print('\n')

    def GetGames(game_name):

        games = []
        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "SELECT * FROM games WHERE game_name = '" + game_name + "'"
        val = un
        cursor.execute(sql)
        for (game_name) in cursor:
            print("{}".format(game_name))
            games.append(game_name)
        CloseDB(cnx)
        return games

    def AddGame(game_name, game_currency, game_trophies, game_ach, game_items):

        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "INSERT INTO games (game_name, game_currency,game_trophies, game_ach,game_items) VALUES (%s, %s, %s, %s, %s )"
        val = (game_name, game_currency, game_trophies, game_ach, game_items)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        CloseDB(cnx)

    def AddGame_json(game_name, game_currency, game_trophies, game_ach, game_items):

        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "INSERT INTO games (game_name, game_currency,game_trophies, game_ach,game_items) VALUES (%s, %s, %s, %s, %s )"
        val = (game_name, game_currency, game_trophies, game_ach, game_items)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        CloseDB(cnx)

    def removeGame(game_name):

        cnx = OpenDB()
        cursor = cnx.cursor()
        sql = "DELETE FROM `upts_s1`.`games` WHERE (`idgame` = '"
        sql += str(game_name[0]) + "')"
        print (sql)
        cursor.execute(sql)
        cnx.commit()
        print("1 record removed.")
        CloseDB(cnx)

# ----------  END DATABASE FUNCTIONS

# ----------  START JSON FUNCTIONS

class json_funcs:
    def __init__(self):
        print('\n')

    def make_json_dict(url):
        req = requests.get(url)
        json_dict = req.json()
        return json_dict

    def make_Pandas(datadict):
        dataframe = pd.DataFrame(datadict)
        return dataframe

    def generic_save(data):
        with open('temp.json', 'w') as outfile:
            json.dumps(data)

    def generic_load():
            json_data = json.loads('temp.json')
            print(json_data)

    def save_json_pd(pd_dataframe):
        with open('temp.json', 'w') as f:
            f.write(pd_dataframe.to_json(orient='columns'))

    def load_json_pd():
        dataframe = pd.read_json('temp.json', orient='columns')
        print(dataframe)
        return dataframe

    def test_json_sequence():
        temp_data = PlayerCon.GetPlayers('asdf')
        print (temp_data)
        dataframe = json_funcs.make_Pandas(temp_data)
        print ('Dataframe:')
        print (dataframe)
        json_funcs.save_json_pd(dataframe)
        json_funcs.load_json_pd()

    def test_generic_sequence():
        temp_data = PlayerCon.GetPlayers('asdf')
        print (temp_data)
        json_funcs.generic_save(temp_data)
        loaded_data = json_funcs.generic_load()
        print ('Loaded: \n')
        print (loaded_data)
        loaded_data = json_funcs.make_Pandas(loaded_data)
        print (loaded_data)


    def save_json_NG(json_filename):
        pd.to_json(orient='table'), {"schema": {"fields": [{"name": "index", "type": "string"},
                            {"name": "Player Key", "type": "int"},
                            {"name": "Player Name", "type": "string"},
                            {"name": "col 1", "type": "string"},
                            {"name": "col 2", "type": "string"},
                            {"name": "User", "type": "string"}],
                    "primaryKey": "index",
                    "pandas_version": "0.20.0"},
            "data": [{"index": "row 1", "Player Key": "36","Player Name": "A Player Name","col 1": "a", "col 2": "b", "User": "A User Name"}]}

# ----------  END JSON FUNCTIONS

# ----------  START MENUS
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
            try:
                aUser, aPass = input(
                    "Enter Username and Password (Username, Password): ").split(',')
            except:
                print("Oops!",sys.exc_info()[0],"occured.")

            try:
                userVal = UserCon.SignIn(aUser, aPass)
                if userVal == None:
                    CloseDB(cnx)
                elif userVal == "Valid":
                    loggingIn = False
                    return aUser
                else:
                    print (userVal)
            except:
                print("Oops!",sys.exc_info()[0],"occured.")
            

        elif menuChoice == '2':
            try:
                print ('PASSWORD IS NOT ENCRYPTED OR SECURE!')
                print ('PASSWORD WILL BE VISIBLE!')
                print ("ONLY USE A TEMPORARY TEST PASSWORD YOU DON'T CARE IF ANYONE SEES!")
                aUser, aPass = input("Enter new Username and Password (Username, Password): ").split(',')
                UserCon.AddUser(aUser, aPass)

            except:
                print("Oops!",sys.exc_info()[0],"occured.")

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
                    double_check = input ('Enter y to Confirm Delete - There is no reversing this action!')
                    if double_check == 'y':
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

# ---------  END MAIN

# ---------  TESTING

def test_Game():
        
    game_name = "Test Game"
    game_notes = [
        {'Note 1' : 'A space-based MMO.'},
        {'Note 2' : 'ISK is both in-game currency and real-world currency of Iceland where the game was developed.'}
    ]
    game_currency = "Test Currency"
    game_trophies = [
        {"Test Trophy One" : {"Description" : "An awesome test trophy" }},
        {"Test Trophy Two" : {"Description" : "An second awesome test trophy" }}
    ]
    game_ach = [
        {"Com L1 Normal" : {"Description" : "Completed Level One on Normal Difficulty" }},
        {"Com L1 Quick" : {"Description" : "Completed Level One Normal Difficulty in less than 2 minutes" }},
        {"Com L2 Hard" : {"Description" : "Completed Level Two on Hard Difficulty" }}
    ]
    game_items = [
        {"jelly_gun" : [{"Description" : "Jelly Gun" }, {"Cost" : 500 }]},
        {"mar_gun" : [{"Description" : "Marshmellow Gun" }, {"Cost" : 750 }]},
        {"mar_cannon" : [{"Description" : "Marshmellow Cannon" }, {"Cost" : 1000 }]}
    ]

    testGame_labels = {
        'game_name' : game_name,
        'game_notes' : game_notes,
        'game_currency' : game_currency,
        'game_trophies' : game_trophies,
        'game_ach' : game_ach,
        'game_items' : game_items
    }

    testGame = {
        game_name : {
        'game_notes' : game_notes,
        'game_currency' : game_currency,
        'game_trophies' : game_trophies,
        'game_ach' : game_ach,
        'game_items' : game_items
        }
    }

    TestGame = upts_game ( game_name, game_notes, game_currency, game_trophies, game_ach, game_items)
    
    TestGame.save_json_pd()

    print(TestGame.game_notes)

    TestGame.load_json_pd()

    print (TestGame.allGames)

test_Game()

class TestFuncts():

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

def sample_data_and_normalize():
    '''
    In [246]: data = [{'state': 'Florida',
                'shortname': 'FL',
                'info': {
                    'governor': 'Rick Scott'
                },
                'counties': [{'name': 'Dade', 'population': 12345},
                            {'name': 'Broward', 'population': 40000},
                            {'name': 'Palm Beach', 'population': 60000}]},
                {'state': 'Ohio',
                'shortname': 'OH',
                'info': {
                    'governor': 'John Kasich'
                },
                'counties': [{'name': 'Summit', 'population': 1234},
                            {'name': 'Cuyahoga', 'population': 1337}]}]
    

    In [247]: json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])
    '''

    '''
    data = [
        {
        'game': 'Eve',
        'info': 
        {
            'currency': 'ISK',
            'note': 'A space-based MMO. ISK is both in-game currency and real-world currency of Iceland where the game was developed.'
        },
        'items': [{'name': 'Frigate', 'cost': 1000},
                    {'name': 'Cruiser', 'cost': 40000},
                    {'name': 'Destroyer', 'cost': 60000}]},
        {
        'game': 'Crushy',
        'info': 
        {
            'currency': 'Crushy Bucks',
            'note': 'A fun destruction-based game by world-renowned designer Will Wagner'
        },
        'items': [{'name': 'Bomb', 'cost': 1000},
                    {'name': 'Gun', 'cost': 750}]}]
    

    json_normalize(data, 'items', ['game', ['info', 'currency']])

    json_normalize(data, ['game', ['info', 'currency']])
    '''