import sys
from os import walk

import upts_users, upts_players, upts_games, upts_json

#  Login Menu
def LoginMenu (session_user):

    # def __init__ (self, session_user):
    #     self.session_user = session_user
    #     print (session_user.loginvalue)

            
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
            session_user.loginVal = "Quit"
            return session_user

        elif menuChoice == '1':

            try:
                aUser = input( "Enter Username: ")
                aPass = input( "Enter Password: ")
            except:
                # print("Invalid input.  Please try again. ",sys.exc_info()[0],"occured.")
                print("Invalid input.  Please try again. ")

            try:
                session_user = upts_users.SignIn(aUser, aPass)
                # print ('Tried to sign in')
                if session_user.loginVal == "Not Valid":
                    print ('Invalid username or password')
                    # print ('none : ' + session_user.user_name)
                    # upts_db.CloseDB(cnx)
                    loggingIn = True
                    
                    return session_user
                    
                elif session_user.loginVal == "Valid":
                    # print (session_user.user_name)
                    loggingIn = False
                    
                    return session_user

            except:
                pass
                # print("Login System Oops!",sys.exc_info()[0],"occured.")

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
            upts_users.UserRecover()

        elif menuChoice == '4':
            upts_users.GetUsers()

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
            players = upts_players.GetPlayers(session_user)
            for player in players:
                print("{0}   {1}".format(player.player_id, player.player_name))

        elif menuChoice == '2':                             # Add a Player
            aName = input(
                "Enter new Player Name: ")
            upts_players.AddPlayer(session_user.uid, aName)

        elif menuChoice == '3':                             # Remove a Player
            print ('Player Key | Player Information')
            players = upts_players.GetPlayers(session_user)
            for player in players:
                print("{0}   {1}".format(player.player_id, player.player_name))
            pk = int(input ('Enter Player Key: '))
            for player in players:
                if int(pk) == player.player_id:
                    print ('Are you sure you want to remove: ' + str(player.player_name))
                    double_check = input (' Enter y to Confirm Delete - There is no reversing this action!')
                    if double_check == 'y':
                        upts_players.removePlayer (player.player_id)

        # elif menuChoice == '4':                             # Edit a Player
        #     print('Edit a Player')

        else:
            print()
            print('Please choose one of the options above.')
            print()

#  Games Menu
def GamesMenu(session_user, jsonpath):

    def __init__ (self):
        pass

    GamesMenuing = True

    while (GamesMenuing):
        print()
        print('       ###   Games Menu   ###')
        print()
        print(" 1 - List All User's Games from DB")
        print(" 2 - List Contents of json directory")
        print(' 3 - Import a Game from .json')
        print(' 4 - Save Imported Game to DB')
        print(' 0 - Return to Main Menu')
        print()       

        menuChoice = input(' Selection: ')

        if menuChoice in ("0","1", "2", "3"):
            print()

        if menuChoice == '0':                               # Main Menu
            GamesMenuing = False
            break

        elif menuChoice == '1':                             # List Games
            upts_users.Load_games_from_db(session_user)

        elif menuChoice == '2':                             # list json files

            print("{0}   {1}".format("Index", "Game Name"))
            jsonlist = upts_json.list_json(jsonpath)
            index = 0
            for jsongame in jsonlist:
                print("{0}   {1}".format(index, jsongame.game_name ))
                index += 1

        elif menuChoice == '3':                             # Import json file
            
            print("{0}   {1}".format("Index", "Game Name"))
            jsonlist = upts_json.list_json(jsonpath)
            index = 0
            for jsongame in jsonlist:
                print("{0}   {1}".format(index, jsongame.game_name ))
                index += 1

            sel = int (input ('Enter index to Import: '))
            imported_game = jsonlist[sel]
            print ()
            print ('Game Name:')
            print (imported_game.game_name)
            print ()
            print ('Imported dataframe:')
            imported_game.load_json_pd(jsonpath)
            print ()
            print ('Imported: ' + str (imported_game.game_name))
            session_user.imported_game = imported_game
            print ()

        elif menuChoice == '4':                             # Save Imported json file
            session_user.imported_game.save_to_db(session_user.uid)
            
        elif menuChoice == '8':                             # List Players
            upts_players.GetPlayers(session_user)

        else:
            print()
            print('Please choose one of the options above.')
            print()

#  Reports and Admin Menu
def ReportsMenu(session_user):
    reportsmenuing = True

    while (reportsmenuing):
        print()
        print('       ###   Reports Menu   ###')
        print()
        print (' This is where the reports and admin menus would go')
        # print(" 1 - List All User's Games")
        # print(' 2 - Import a Game from .json')
        # print(' 3 - Remove a Game')
        print(' 9 - Return to Main Menu')
        print(' 0 - Quit')
        print()       

        menuChoice = input(' Selection: ')

        if menuChoice in ("0","1", "2", "3", "4"):
            print()

        if menuChoice == '9':                               # Main Menu
            GamesMenuing = False
            break

        if menuChoice == '0':                               # Quit
            GamesMenuing = False
            session_user.loginVal = "Quit"
            break                

        # elif menuChoice == '1':                             # List Games
        #     upts_user.Load_games_from_db(session_user)

        # elif menuChoice == '2':                             # Import a Game
        #     upts_report.list_all_games()
        #     gameID = input("Enter Game ID: ")
        #     # upts_game.....

        # elif menuChoice == '3':                             # Remove Game
        #     upts_player.GetPlayers(session_user.uid)


        else:
            print()
            print('Please choose one of the options above.')
            print()
