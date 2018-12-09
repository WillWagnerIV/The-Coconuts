import os, sys











# ---------  TESTING

def test_Game():
        
    game_name = "Test Game"
    game_notes = [
        {'Note 1' : 'A space-based MMO.'},
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

    TestGame = upts_game ( game_name, game_notes, game_currency, game_trophies, game_ach, game_items)
    
    TestGame.save_json_pd()

    TestGame.save_to_db(session_userid = 8)

    TestGame.load_json_pd()


    print ('Test Complete')

# test_Game()

class TestFuncts():

    @pytest.mark.xfail
    def test_login():
        OpenDB(upts_user)
        aUser = "asdf"
        aPass = "kjhkljh"
        assert upts_user.SignIn(upts_user, aUser, aPass) == "asdf"
        CloseDB(upts_user)


    @pytest.mark.xfail
    def test_new_user():
        un = "TestUser"+str(datetime.datetime)
        pw = "kjhkljh"
        OpenDB(upts_user)
        assert upts_user.AddUser(upts_user, un, pw) == upts_user.cursor.lastrowid
        self.CloseDB()


    @pytest.mark.xfail
    def test_list_users():
        assert 1 == 5


    @pytest.mark.xfail
    def test_list_players():
        assert 1 == 5


    @pytest.mark.xfail
    def test_add_player():
        assert 1 == 5

    # print('\n\n')
    # print("{}, {} was hired on {:%d %b %Y}".format(
    #     last_name, first_name, hire_date))


    # cnx.execute('''CREATE TABLE COMPANY
    #          (ID INT PRIMARY KEY     NOT NULL,
    #          NAME           TEXT    NOT NULL,
    #          AGE            INT     NOT NULL,
    #          ADDRESS        CHAR(50),
    #          SALARY         REAL);''')

def sample_data_and_normalize():
    '''
    In [246]: data = [{'state': 'Florida',
                'shortname': 'FL',
                'info': {
                    'governor': 'Rick Scott'
                },
                'counties': [{'name': 'Dade', 'population': 12345},
                            {'name': 'Broward', 'population': 40000},
                            {'name': 'Palm Beach', 'population': 60000}]},
                {'state': 'Ohio',
                'shortname': 'OH',
                'info': {
                    'governor': 'John Kasich'
                },
                'counties': [{'name': 'Summit', 'population': 1234},
                            {'name': 'Cuyahoga', 'population': 1337}]}]
    

    In [247]: json_normalize(data, 'counties', ['state', 'shortname', ['info', 'governor']])
    '''

    '''
    data = [
        {
        'game': 'Eve',
        'info': 
        {
            'currency': 'ISK',
            'note': 'A space-based MMO. ISK is both in-game currency and real-world currency of Iceland where the game was developed.'
        },
        'items': [{'name': 'Frigate', 'cost': 1000},
                    {'name': 'Cruiser', 'cost': 40000},
                    {'name': 'Destroyer', 'cost': 60000}]},
        {
        'game': 'Crushy',
        'info': 
        {
            'currency': 'Crushy Bucks',
            'note': 'A fun destruction-based game by world-renowned designer Will Wagner'
        },
        'items': [{'name': 'Bomb', 'cost': 1000},
                    {'name': 'Gun', 'cost': 750}]}]
    

    json_normalize(data, 'items', ['game', ['info', 'currency']])

    json_normalize(data, ['game', ['info', 'currency']])
    '''


def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result