# users table connections
class UserCon():
    
    def __init__(self):
        print('\n')

    def GetUsers(self):

        cnx = self.OpenDB()
        cursor = cnx.cursor()
        query = ("SELECT * FROM users")
        cursor.execute(query)
        for (username) in cursor:
            print("{}".format(username))
        self.CloseDB(cnx)

    def AddUser( un, pw):

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
        