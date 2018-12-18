import datetime
import json
import os
import pprint
import sys
import time
from io import StringIO
from os import walk

import mysql.connector as mysql
import numpy as np
import pandas as pd
# import pytest
import requests
from mysql.connector import errorcode
from pandas.io.json import json_normalize

import upts_dbs
import upts_menus
import upts_reports as urep
import upts_users
from upts_games import upts_game

# #getting current file path
path=os.path.abspath(__file__)

# getting directory name
fd=os.path.dirname(path)
# print ('fd = ' + fd)
# Split the current path
head, tail = os.path.split(fd)
# print ('head = ' + head)

#going forward one level - add the folders
testPath=os.path.join(head,'tests/')
srcpath=os.path.join(head,'src/')
jsonpath=os.path.join(head,'json/')

#adding the path
sys.path.append(testPath)
sys.path.append(srcpath)
sys.path.append(jsonpath)

# import upts_players, upts_reports

# Database Connection Variables
db_master = 'upts_s1'
db_host = '134.173.236.104'
db_user='prog_user'
db_password='Pr0gpass'
db_table = ""



#  Main Loop

class Main ():

    os.system('cls' if os.name == 'nt' else 'clear')
    
    #  Setup Main Class Variables
    mainLooping = True
    session_user = upts_users.upts_user()
    

    def __init__(self , session_user = ""):
        self.session_user = session_user
            
    while (mainLooping):

        # Call the LoginMenu
        while (session_user.loginVal == "Not Valid"):
            session_user = upts_menus.LoginMenu(session_user)
            print ()
            

            if session_user.loginVal == 'Quit':
                mainLooping = False
                break

            if session_user.loginVal == "Valid":
                print("User Logged In: ",session_user.name)
                break

        
        if session_user.loginVal == 'Quit':
                mainLooping = False
                break


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
            upts_menus.PlayerMenu(session_user)
        elif menuChoice == '2':
            upts_menus.GamesMenu( session_user, jsonpath)
        elif menuChoice == '3':
            upts_menus.ReportsMenu( session_user)
            
        else:
            print()
            print('Please choose one of the options above.')
            print()



if __name__ == "__main__":
    Main()
