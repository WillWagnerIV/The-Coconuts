
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

