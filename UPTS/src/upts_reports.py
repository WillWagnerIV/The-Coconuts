from os import walk

from upts_dbs import upts_db

# class upts_report():

    # def __init__(self, report_name="Default Report", filelist = []):
    #     print ('Initialized Report')
    #     self.report_name = report_name
    #     self.filelist = filelist
    #     print('\n')



def list_json (jsonpath):
    filelist = []
    for (dirpath, dirnames, filenames) in walk(jsonpath):
        filelist.extend(filenames)
        

    return self.filelist

# Use a decorator to open/close database connection
def db_con (func):
    '''
    This decorator will open and close the UPTS Database connection.
    It will execute the passed function or fail gracefully.
    This decorator Tries to run a passed function
    If the passed function returns an error then the decorator 
        will return the Error.  Otherwise it returns 
        the result of the function.
    '''
    
    # Build
    cnx = upts_db.OpenDB()
    cursor = cnx.cursor()

    # Runs the passed function or captures and returns the error
    def inner (*args, **kwargs):

        try:
            func ( *args, **kwargs)
            
        except Exception as err:
            print("Failed accessing record: {}".format(err))

    # Teardown    
    upts_db.CloseDB(cnx)

    return inner

@db_con
def list_all_games (self):
    query = ("SELECT * FROM games")
    upts_db.cursor.execute(query)
    for (game_name) in upts_db.cursor:
        print("{}".format(game_name))
    

