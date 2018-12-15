import upts_dbs as upts_db


def GetUsers():

    cnx = upts_db.OpenDB()
    cursor = cnx.cursor()
    query = ("SELECT * FROM users")
    cursor.execute(query)
    for (username) in cursor:
        print("{}".format(username))
    upts_db.CloseDB(cnx)

def AddUser(un, pw):
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



    print ('10 Starting sign in function')



    # print('Trying to Validate')
    cnx = upts_db.OpenDB()
    cursor = cnx.cursor()
    sql = 'SELECT * FROM users WHERE username = "' + un + '"'
    # print (sql)
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

    print()
    print('This is where the screens to assist with credentials would go.')
    print ()

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






class upts_user():

    # Class Variables
    total_user_count = 0
    allUsers = []

    def __init__(self, name = "Default User Name", un = "username", pw = "password", uid = 0, loginVal = "Not Valid"):

        self.name = name
        self.user_name = un
        self.pw = pw
        self.uid = uid
        self.loginVal = "Not Valid"
