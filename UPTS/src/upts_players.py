import upts_dbs as upts_db


def GetPlayers( session_user):
    user_id = session_user.uid
    players = []
    cnx = upts_db.OpenDB()
    cursor = cnx.cursor()
    sql = "SELECT * FROM players WHERE users_idusers = '" + str(user_id) + "'"
    cursor.execute(sql)
    for playerx in cursor:
        temp_player = upts_player (player_id = playerx[0], player_name = playerx[1])
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
    # print (sql)
    cursor.execute(sql)
    cnx.commit()
    print("1 record removed.")
    upts_db.CloseDB(cnx)

class upts_player():

    def __init__(self, player_id = 0, player_name = "None"):
        self.player_id = player_id
        self.player_name = player_name

