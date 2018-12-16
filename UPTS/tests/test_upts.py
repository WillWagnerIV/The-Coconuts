import os, sys
import time
import pytest

# #getting current file path
path=os.path.abspath(__file__)

# getting directory name
fd=os.path.dirname(path)
# print ('fd = ' + fd)

# Split the current path
head, tail = os.path.split(fd)
print ('head = ' + head)

#going forward one level - add the folder name 'src'
modulePath=os.path.join(head,'src')
jsonpath=os.path.join(head,'json')

print ('Module Path = ' + modulePath)
print ('json Path = ' + jsonpath)


#adding the path
sys.path.append(modulePath)

import upts_games
import upts_dbs as upts_db
import upts_json
import upts_users, upts_players, upts_reports 

# from upts_main import *



#input output values for account with balance $500
# input_output = (
#     (20, 520),
#     (30, 530),
#     (-35, 465),
#     (12, 512)
# )

# TestGame = upts_game ( game_name, game_notes, game_currency, game_trophies, game_ach, game_items)

dt = time.strftime('%d/%m/%Y %H:%M:%S')
print (dt)
user_realname = "Test User Name" + dt
un = "testuser" + dt
pw = "testpass"
uid = 0
player_id = 0
player_name = "Test Player Name"
lastrowid = 0
        
game_name = "Test Game"
game_notes = [
    {'Note 1' : 'Learning with numbers is brilliant.'},
    {'Note 2' : 'ISK is both in-game currency and real-world currency of Iceland where the game was developed.'}
]
game_currency = [
    {"Gold Dollar" : "Most valuable"},
    {"Silver Quarter" : "Second biggest Unit.  1/4 of a dollar."},
    {"Bronze Dime" : "Third unit.  1/10 of a dollar."}
]
game_trophies = [
    {"Test Trophy One" : "An awesome test trophy" },
    {"Test Trophy Two" : "An second awesome test trophy" }
]
game_ach = [
    {"Score " : "Completed Level One on Normal Difficulty" },
    {"Com L1 Quick" : "Completed Level One Normal Difficulty in less than 2 minutes" },
    {"Com L2 Hard" : "Completed Level Two on Hard Difficulty" }
]
game_items = [
    {"Jelly Gun" : ["Portable Jelly Gun" , 500, "Silver" ]},
    {"Marshmellow Gun" : ["Portable Marshmellow Gun", 250, "Dollars"]},
    {"Marshmellow Cannon" : ["Stationary Marshmellow Cannon" , 1000, "Dollars" ]}
]

testGame_labels = {
    'game_name' : game_name,
    'game_notes' : game_notes,
    'game_currency' : game_currency,
    'game_trophies' : game_trophies,
    'game_ach' : game_ach,
    'game_items' : game_items
}

testGame_alt_labels = {
    game_name : {
    'game_notes' : game_notes,
    'game_currency' : game_currency,
    'game_trophies' : game_trophies,
    'game_ach' : game_ach,
    'game_items' : game_items
    }
}

# Test Database Connection
def test_upts_db():
    x = upts_db.OpenDB()
    print (x.cursor())
    assert str (x.cursor()) == "MySQLCursor: (Nothing executed yet)"
    upts_db.CloseDB(x)
    print (x.cursor())
    assert str (x.cursor()) == "MySQLCursor: (Nothing executed yet)"

# Test old-Fashioned Test
def test_old_test():
    upts_db.open_test_close()
    assert 1 == 1

# Fixture for creating Objects
@pytest.fixture()
def create_objects():
    a = upts_users.upts_user ( user_realname, un, pw )
    print ('a.uid = ' + str (a.user_name))
    b = upts_players.upts_player ( player_id, player_name)
    c = upts_games.upts_game ( game_name, game_notes, game_currency, game_trophies, game_ach, game_items)
    return [a, b, c]

# Test creating objects
def test_creating_objects(create_objects):
    assert create_objects[0].name == user_realname
    assert create_objects[1].player_name == player_name
    assert create_objects[2].game_name == game_name

# Test Players Module
def test_Players_module(create_objects):

    uid = upts_users.AddUser(un, pw)
    tsession_user = upts_users.upts_user ( 'Players Test Name', 'plyrtest '+un, pw )
    tsession_user.uid = uid

    print ('Session User.user_name : ' + str (tsession_user.user_name))
    print (tsession_user.uid)

    upts_players.AddPlayer ( tsession_user.uid, "Players Test Player Name" + dt)

    x = upts_players.GetPlayers( tsession_user )
    print (x)
    assert x != []

    upts_players.removePlayer(player_id)
    x = upts_players.GetPlayers(tsession_user)
    print (x)
    assert x != []

#parametrized tests for Adding new User to DB
@pytest.mark.parametrize("uname",[ pytest.param(un+"at", marks=pytest.mark.xpass(reason="Username is unique")), 
                                   pytest.param("testuser", marks=pytest.mark.xfail(reason="Username must be unique"))  ])
def test_advanced_AddUser(uname):
    lastrowid = upts_users.AddUser(uname, pw)
    assert lastrowid != 0



# Test for adding player
# @pytest.mark.parametrize("uname",
#                             [
#                             pytest.param(un, marks=pytest.mark.xpass(reason="Username is unique")),
#                             pytest.param("testuser", marks=pytest.mark.xfail(reason="Username must be unique"))
#                             ]
# )
# def test_advanced_AddPlayer(uname):
#     lastrowid = upts_user.AddUser(uname, pw)
#     assert lastrowid != 0

# Test for deleting player

# Test for adding game

# Test for deleting game

# Test for player report

# Test for games report

# Test reading list of json files from directory
# Must have at least one file in directory or test should be made xfail
def test_list_json_dir():
    assert upts_json.list_json(jsonpath) != None


# #test checking account withdraw
# def test_checking_withdraw(create_objects):
#     create_objects[1].balance = 561
#     create_objects[1].withdraw(561)
#     assert create_objects[1].balance == 0

# #parametrized tests for deposit
# @pytest.mark.parametrize("deposited_amount, updated_balance",
#                             [
#                             (20, 520),
#                             (30, 530),
#                             pytest.param(-35,465, marks=pytest.mark.xpassl(reason="Deposit of negative amount should be disallowed")),
#                             pytest.param(10, 512, marks=pytest.mark.xfail(reason="Deposit of $10 on $500 balance must not give a balance of $512"))
#                             ]
# )
# def test_deposit(deposited_amount, updated_balance):
#     c = CheckingAccount("X Abc", 1234, date.today(), 500)
#     c.deposit(deposited_amount)
#     assert c.balance == updated_balance

# def test_future_date(create_objects):
#     with pytest.raises(Exception):
#         a = BankAccount("X Abc", 1234, date.today() + timedelta(days=2), 500)
