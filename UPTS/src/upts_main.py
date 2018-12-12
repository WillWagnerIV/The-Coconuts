import requests
from io import StringIO
import json
import mysql.connector as mysql
from mysql.connector import errorcode
import pytest
import datetime
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import pprint
import os, sys
import time

from upts_games import upts_game 
from upts_dbs import upts_db 

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

        self.loginVal = "Not Valid"
        

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
                session_user = upts_user (name = "Default Invalid First Last Name", un = un , pw = pw , uid = 0)
                upts_db.CloseDB(cnx)
                session_user.loginVal = "Not Valid"
                return session_user

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


class upts_player():

    def __init__(self, player_id = 0, player_name = "None"):
        self.player_id = player_id
        self.player_name = player_name


    def GetPlayers(user_id):
        players = []
        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        sql = "SELECT * FROM players WHERE users_idusers = '" + str(user_id) + "'"
        cursor.execute(sql)
        for playerx in cursor:
            temp_player = upts_player (player_id = playerx[0], player_name = playerx[1])
            print("{0}   {1}".format(temp_player.player_id, temp_player.player_name))
            players.append(temp_player)

        upts_db.CloseDB(cnx)
        return players


    def AddPlayer(un, pn):

        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        sql = "INSERT INTO players (users_idusers, player_name) VALUES (%s, %s)"
        val = (un, pn)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        upts_db.CloseDB(cnx)

    def removePlayer(player_id):

        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        sql = "DELETE FROM `upts_s1`.`players` WHERE (`idplayers` = '"
        sql += str(player_id) + "')"
        print (sql)
        cursor.execute(sql)
        cnx.commit()
        print("1 record removed.")
        upts_db.CloseDB(cnx)


class upts_report():

    def __init__(self):
        print('\n')

    # Use a decorator to open/close database connection
    def db_con (func):
        def inner (*args, **kwargs):
            upts_db.cnx = upts_db.OpenDB()
            upts_db.cursor = upts_db.cnx.cursor()

            try:
                func ( *args, **kwargs)
                
            except Exception as err:
                print("Failed accessing record: {}".format(err))
                
            upts_db.CloseDB(upts_db.cnx)

        return inner

    @db_con
    def list_all_games (self):
        query = ("SELECT * FROM games")
        upts_db.cursor.execute(query)
        for (game_name) in upts_db.cursor:
            print("{}".format(game_name))


class Temporary_Game_Functions():

    # Class Variables
    # none

    def __init__(self):
        print('\n')

    def GetGames(game_name):

        games = []
        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        sql = "SELECT * FROM games WHERE game_name = '" + game_name + "'"
        val = un
        cursor.execute(sql)
        for (game_name) in cursor:
            print("{}".format(game_name))
            games.append(game_name)
        upts_db.CloseDB(cnx)
        return games

    def AddGame(game_name, game_currency, game_trophies, game_ach, game_items):

        cnx = upts_db.OpenDB()
        cursor = cnx.cursor()
        sql = "INSERT INTO games (game_name, game_currency,game_trophies, game_ach,game_items) VALUES (%s, %s, %s, %s, %s )"
        val = (game_name, game_currency, game_trophies, game_ach, game_items)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        upts_db.CloseDB(cnx)

    def AddGame_json(game_name, game_currency, game_trophies, game_ach, game_items):

        cnx = OpenDB()
        cursor = cnx.cursor()
        self.sql = "INSERT INTO games (game_name, game_currency,game_trophies, game_ach,game_items) VALUES (%s, %s, %s, %s, %s )"
        self.val = (game_name, game_currency, game_trophies, game_ach, game_items)
        cursor.execute(sql, val)
        cnx.commit()
        print("1 record inserted, ID:", cursor.lastrowid)
        CloseDB(cnx)

    def removeGame(game_name):

        cnx = OpenDB()
        cursor = cnx.cursor()
        self.sql = "DELETE FROM `upts_s1`.`games` WHERE (`idgame` = '"
        sql += str(game_name[0]) + "')"
        print (sql)
        cursor.execute(sql)
        cnx.commit()
        print("1 record removed.")
        CloseDB(cnx)


class Temporary_json_funcs:
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
        temp_data = upts_player.GetPlayers('asdf')
        print (temp_data)
        dataframe = json_funcs.make_Pandas(temp_data)
        print ('Dataframe:')
        print (dataframe)
        json_funcs.save_json_pd(dataframe)
        json_funcs.load_json_pd()

    def test_generic_sequence():
        temp_data = upts_player.GetPlayers('asdf')
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


class Main ():

    def __init__(self):
        pass

            
    #  Login Menu
    def LoginMenu():
        loggingIn = True
        session_user = upts_user()


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
                session_user.loginVal = "Quit"
                return session_user

            elif menuChoice == '1':
                try:
                    aUser, aPass = input( "Enter Username and Password (Username, Password): ").split(',')
                except:
                    print("Invalid input.  Please try again. ",sys.exc_info()[0],"occured.")

                try:
                    session_user = upts_user.SignIn(aUser, aPass)
                    if session_user.loginVal == "Not Valid":
                        print ('Invalid username or password')
                        # print ('none : ' + session_user.user_name)
                        # upts_db.CloseDB(cnx)
                        loggingIn = True
                        
                        return session_user
                        
                    elif session_user.loginVal == "Valid":
                        print (session_user.user_name)
                        loggingIn = False
                        
                        return session_user

                except:
                    print("Login System Oops!",sys.exc_info()[0],"occured.")
                

            elif menuChoice == '2':
                try:
                    print ('PASSWORD IS NOT ENCRYPTED OR SECURE!')
                    print ('PASSWORD WILL BE VISIBLE!')
                    print ("ONLY USE A TEMPORARY TEST PASSWORD YOU DON'T CARE IF ANYONE SEES!")
                    aUser, aPass = input("Enter new Username and Password (Username, Password): ").split(',')
                    print ('Should add user')
                    upts_user.AddUser(aUser, aPass)

                except:
                    print("Oops!",sys.exc_info()[0],"occured.")

            elif menuChoice == '3':
                upts_user.UserRecover()

            elif menuChoice == '4':
                upts_user.GetUsers()

            else:
                print()
                print('Please choose one of the options above.')
                print()

    #  Player Menu
    def PlayerMenu(session_user):
        PlayerMenuing = True

        while (PlayerMenuing):
            print()
            print('       ###   Player Menu   ###')
            print()
            print(' 1 - List My Players')
            print(' 2 - Add a Player')
            print(' 3 - Remove a Player')
            print(' 0 - Return to Main Menu')
            print()

            menuChoice = input(' Selection: ')

            if menuChoice in ("1", "2", "3", "4"):
                print()

            if menuChoice == '0':                               # Main Menu
                PlayerMenuing = False
                break

            elif menuChoice == '1':                             # List Players
                upts_player.GetPlayers(session_user.uid)

            elif menuChoice == '2':                             # Add a Player
                aName = input(
                    "Enter new Player Name: ")
                upts_player.AddPlayer(session_user.uid, aName)

            elif menuChoice == '3':                             # Remove a Player
                print ('Player Key | Player Information')
                players_list = upts_player.GetPlayers(session_user.uid)
                pk = int(input ('Enter Player Key: '))
                for player in players_list:
                    if int(pk) == player.player_id:
                        print ('Are you sure you want to remove: ' + str(player.player_name))
                        double_check = input (' Enter y to Confirm Delete - There is no reversing this action!')
                        if double_check == 'y':
                            upts_player.removePlayer (player.player_id)

            # elif menuChoice == '4':                             # Edit a Player
            #     print('Edit a Player')

            else:
                print()
                print('Please choose one of the options above.')
                print()

    #  Games Menu
    def GamesMenu(session_user):
        GamesMenuing = True

        while (GamesMenuing):
            print()
            print('       ###   Games Menu   ###')
            print()
            print(' 1 - List My Games')
            print(' 2 - Add a Game')
            print(' 3 - Remove a Game')
            print(' 0 - Return to Main Menu')
            print()       

            menuChoice = input(' Selection: ')

            if menuChoice in ("0","1", "2", "3"):
                print()

            if menuChoice == '0':                               # Main Menu
                GamesMenuing = False
                break

            elif menuChoice == '1':                             # List Games
                upts_user.Load_games_from_db(session_user)

            elif menuChoice == '2':                             # Add a Game
                upts_report.list_all_games()
                gameID = input("Enter Game ID: ")
                # upts_game.....

            elif menuChoice == '3':                             # Remove Game
                upts_player.GetPlayers(session_user.uid)


            else:
                print()
                print('Please choose one of the options above.')
                print()

    #  Reports and Admin Menu
    def ReportsMenu(session_user):
        pass

    #  Main Loop
    mainLooping = True
    session_user = upts_user()
    session_user.loginVal == "Not Valid"

    while (mainLooping):

        # Call the LoginMenu
        while (session_user.loginVal == "Not Valid"):
            session_user = LoginMenu()
            print ()
            

            if session_user.loginVal == 'Quit':
                mainLooping = False
                break

        if session_user.loginVal == "Valid":
            print("User Logged In: ",session_user.name)

        

        # Main 3 Choices

        print()
        print('       ###   Main Menu   ###')
        print()
        print(' 1 - Players Menu')
        print(' 2 - Games Menu')
        print(' 3 - Reports and Admin Menu')
        print(' 0 - Quit')
        print()
        menuChoice = input(' Selection: ')

        if menuChoice in ("1", "2", "3", "4"):
            print()
        if menuChoice == '0':
            mainLooping = False
            session_user.loginVal == 'Quit'
            break
        elif menuChoice == '1':
            PlayerMenu(session_user)
        elif menuChoice == '2':
            GamesMenu( session_user)
        elif menuChoice == '3':
            ReportsMenu( session_user)
        elif menuChoice == '4':
            upts_player.ListPlayers(users_idusers)
            
        else:
            print()
            print('Please choose one of the options above.')
            print()




# For testing only

# #getting current file path
path=os.path.abspath(__file__)

# getting directory name
fd=os.path.dirname(path)
# print ('fd = ' + fd)

# Split the current path
head, tail = os.path.split(fd)
# print ('head = ' + head)

#going forward one level - add the folder name 'tests'
testPath=os.path.join(head,'tests')

#adding the path
sys.path.append(testPath)

