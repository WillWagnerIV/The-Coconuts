import os, sys
import time

# #getting current file path
path=os.path.abspath(__file__)

# getting directory name
fd=os.path.dirname(path)
# print ('fd = ' + fd)

# Split the current path
head, tail = os.path.split(fd)
# print ('head = ' + head)

#going forward one level - add the folder name 'src'
modulePath=os.path.join(head,'src')

#adding the path
sys.path.append(modulePath)

from upts_main import *
import pytest

#input output values for account with balance $500
# input_output = (
#     (20, 520),
#     (30, 530),
#     (-35, 465),
#     (12, 512)
# )


        
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
    {"Com L1 Normal" : "Completed Level One on Normal Difficulty" },
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

# TestGame = upts_game ( game_name, game_notes, game_currency, game_trophies, game_ach, game_items)
dt = time.strftime('%d/%m/%Y %H:%M:%S')
print (dt)
user_realname = "Test User Name" + dt
un = "testuser" + dt
pw = "testpass"
uid = 0
player_id = 0
player_name = "Test Player Name"

# Test Database Connection
def test_upts_db():
    x = upts_db.OpenDB()
    upts_db.CloseDB(x)
    assert "Access denied" not in str(x)

#fixture for creating Objects
@pytest.fixture()
def create_objects():
    a = upts_user ( user_realname, un, pw, uid )
    b = upts_player ( player_id, player_name)
    c = upts_game ( game_name, game_notes, game_currency, game_trophies, game_ach, game_items)
    return [a, b, c]

#test creating objects
def test_creating_objects(create_objects):
    assert create_objects[0].name == user_realname
    assert create_objects[1].player_name == player_name
    assert create_objects[2].game_name == game_name



# Test for adding User (actually saves the user to database)
def test_AddUser():
    lastrowid = upts_user.AddUser(un, pw)
    print (lastrowid)

# Test for adding player

# Test for deleting player

# Test for adding game

# Test for deleting game

# Test for player report

# Test for games report




# #parametrized fixture
# @pytest.fixture(params=input_output)
# def input_output_tuples(request):
#     a = BankAccount()
#     a.balance = 500
#     return (a, request.param)

# #test function utilizing parametrized fixture
# def test_deposit_advanced(input_output_tuples):
#     input_output_tuples[0].deposit(input_output_tuples[1][0])
#     assert input_output_tuples[0].balance == input_output_tuples[1][1]


# #fixture for creating Account objects
# @pytest.fixture()
# def create_objects():
#     a = BankAccount("X Abc", 1234, date.today(), 500)
#     b = CheckingAccount("X Abc", 1234, date.today(), 500)
#     c = SavingsAccount("X Abc", 1234, date.today(), 500)
#     return [a, b, c]

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
#                             pytest.param(-35,465, marks=pytest.mark.xfail(reason="Deposit of negative amount should be disallowed")),
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
