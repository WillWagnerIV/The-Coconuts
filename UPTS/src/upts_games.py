from os import walk

import pandas as pd
from pandas.io.json import json_normalize
import numpy

import upts_dbs as upts_db


class upts_game():

    # Class Variables
    total_game_count = 0
    allGames = []

    def __init__(self, game_name='none', game_notes='none', game_currency='none', game_trophies='none', game_ach='none', game_items='none'):
        # print('Initialized Game')
        self.game_name = game_name
        self.game_notes = game_notes
        self.game_currency = game_currency
        self.game_trophies = game_trophies
        self.game_ach = game_ach
        self.game_items = game_items

        self.sql = ""
        self.val = ""
        self.cnx = ""
        self.csr = ""
        self.games_idgames = ""

        self.pd_structure = ""

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

    def save_json_pd(self,jsonpath):
        print ('Saving game json file')
        datadict = self.convert_class_to_dict()
        pd_dataframe = self.make_Pandas(datadict)
        json_name = jsonpath + self.game_name + ".json"
        with open(json_name, 'w') as f:
            f.write(pd_dataframe.to_json(orient='records', lines=True))

    def load_json_pd(self, jsonpath):
        
        json_name = jsonpath + self.game_name + ".json"

        print ('JSON NAME:')
        print (json_name)

        dataframe = pd.read_json(json_name, orient='records', lines=True)
        
        print ()
        print ('returned dataframe')
        print(dataframe)
        print()

        # # create the game then save to db
        # print ('dataframe[gamename.game_name.tolist()]')

        df_to_list = dataframe[self.game_name].tolist()
        print ()
        # print (df_to_list)
        # print ()

        # convert dataframe to class
        self.game_name = df_to_list[0]['game_name']
        self.game_notes = df_to_list[1]['game_notes']
        self.game_currency = df_to_list[2]['game_currency']
        self.game_trophies = df_to_list[3]['game_trophies']
        self.game_ach = df_to_list[4]['game_ach']
        self.game_items = df_to_list[5]['game_items']
        
        print (self.game_name)
        print (self.game_notes)
        print (self.game_currency)
        print (self.game_trophies)
        print (self.game_ach)
        print (self.game_items)



    def json_to_db(self, jsonpath, session_user):   
        filelist = []
        gameslist = []
        index = 0                                   
        for (dirpath, dirnames, filenames) in walk(jsonpath):
            filelist.extend(filenames)
            
        for filename in filelist:
            gn = filename[:-5] 
            temp_game = upts_game (game_name=gn)
            print("{0}   {1}".format(index, temp_game.game_name))
            gameslist.append(temp_game)
            index += 1

        file_choice = int (input ('Enter Index to Import: '))
        filename = filelist[file_choice]
        gamename = gameslist[file_choice]
        print (filename)
        print (gamename.game_name)
        print (jsonpath)
        
        json_name = jsonpath + gamename.game_name + ".json"
        print ('JSON NAME:')
        print (json_name)
        dataframe = pd.read_json(json_name, orient='records', lines=True)
        
        print ('returned dataframe')
        print(dataframe)

        # create the game then save to db
        print ('dataframe[gamename.game_name]')
        print (dataframe[gamename.game_name].tolist())

        df_to_list = dataframe[gamename.game_name].tolist()

        # convert dataframe to class
        game_name = df_to_list[0]['game_name']
        game_notes = df_to_list[1]['game_notes']
        game_currency = df_to_list[2]['game_currency']
        game_trophies = df_to_list[3]['game_trophies']
        game_ach = df_to_list[4]['game_ach']
        game_items = df_to_list[5]['game_items']
        
        print (game_name)
        print (game_notes)
        print (game_currency)
        print (game_trophies)
        print (game_ach)
        print (game_items)

        imported_game = upts_game (game_name, game_notes, game_currency, game_trophies, game_ach, game_items)

    def json_files (self, json_path):
        filelist = []
        for (dirpath, dirnames, filenames) in walk(json_path):
            filelist.extend(filenames)
        return filelist

    # Save each property to their respective databases
    def save_to_db(self, session_userid):
        
        # Use a decorator to open/close database connection
        def db_con (func):

            # Runs the passed function or captures and returns the error
            def inner (*args, **kwargs):

                # print ('Setup')
                # Setup
                self.cnx = upts_db.OpenDB()
                self.csr = self.cnx.cursor()

                # try:
                func ( *args, **kwargs )
                    
                # except Exception as err:
                #     print("Failed accessing record: {}".format(err))

                # Teardown             
                # print ('Teardown')            

            return inner

        # Game Name
        def name_to_db(self):
            cnx = upts_db.OpenDB()
            csr = cnx.cursor()
            try:
                self.sql = "INSERT INTO `upts_s1`.`games` (`game_name`) VALUES ('"+self.game_name+"');"
                csr.execute(self.sql)
                cnx.commit()
                upts_db.CloseDB(cnx)
            except Exception as err:
                    print("Failed inserting record: {}".format(err))
                    upts_db.CloseDB(cnx)

            # Get games_idgames    
            cnx = upts_db.OpenDB()
            csr = cnx.cursor()
            self.sql = "SELECT * FROM `upts_s1`.`games` WHERE (`game_name`) = '" + self.game_name + "'"
            csr.execute(self.sql)
            for (game_name) in csr:
                self.games_idgames = game_name[0]
            print ('Adding ' + game_name[1] + ' with Game ID = ' + str (self.games_idgames))
            upts_db.CloseDB(cnx)

        # Game Notes
        @db_con
        def notes_to_db (self):
            
            for note in self.game_notes:
                for key in note :
                    csr = self.cnx.cursor()
                    # print ("KEY: %s : VALUE: %s" % (key, note[key]))
                    sql = "INSERT INTO notes (gnote_name, gnote_details, games_idgames) VALUES (%s , %s, %s)"
                    val = (key, note[key], self.games_idgames)
                    csr.execute(sql, val)
                    self.cnx.commit()
                    
                    
        # Currency
        @db_con
        def cur_to_db(self):
            for cur in self.game_currency:
                for key in cur :
                    csr = self.cnx.cursor()
                    # print ("key: %s , value: %s" % (key, cur[key]))
                    sql = "INSERT INTO currencies (game_currency, currency_note, games_idgames) VALUES (%s , %s, %s)"
                    val = (key, cur[key], self.games_idgames)
                    csr.execute(sql,val)
                    self.cnx.commit()

        # Trophies
        @db_con
        def trophies_to_db(self):
            for trophy in self.game_trophies:
                for key in trophy:
                    csr = self.cnx.cursor()
                    # print ("key: %s , value: %s" % (key, trophy[key]))
                    sql = "INSERT INTO trophies (trophy_name, trophy_description, games_idgames) VALUES (%s , %s, %s)"
                    val = (key, trophy[key], self.games_idgames)
                    csr.execute(sql, val)
                    self.cnx.commit()

        # Acheivements
        @db_con
        def ach_to_db(self):
            for achievement in self.game_ach:
                for key in achievement:
                    csr = self.cnx.cursor()
                    # print ("key: %s , value: %s" % (key, achievement[key]))
                    sql = "INSERT INTO achievements (ach_name, ach_desc, games_idgames) VALUES (%s , %s, %s)"
                    val = (key, achievement[key], self.games_idgames)
                    csr.execute(sql, val)
                    self.cnx.commit()

        # Game Items
        @db_con
        def items_to_db (self):
            for item in self.game_items:
                for key in item:
                    csr = self.cnx.cursor()
                    # print ("key: %s , value: %s, %s, %s" % (key, item[key][0], item[key][1], item[key][2]))
                    sql = "INSERT INTO items (item_name, item_desc, item_cost, cost_unit, games_idgames) VALUES (%s , %s, %s, %s, %s)"
                    val = (key, item[key][0], item[key][1], item[key][2], self.games_idgames)
                    csr.execute(sql, val)
                    self.cnx.commit()

        # Register user with games_has_users database
        @db_con
        def game_has_user (self, session_userid):
            print (session_userid , self.games_idgames)
            if session_userid != "None":
                csr = self.cnx.cursor()
                try:
                    sql = "INSERT INTO games_has_users (users_idusers,games_idgames) VALUES (%s , %s)"
                    val = (session_userid , self.games_idgames)
                    csr.execute(sql, val)
                    self.cnx.commit()
                except Exception as err:
                        print("Failed inserting record: {}".format(err))

        


        name_to_db(self)
        notes_to_db (self)
        cur_to_db (self)
        trophies_to_db (self)
        ach_to_db (self)
        items_to_db (self)
        game_has_user (self, session_userid)
        
        print("Game Records Inserted")
