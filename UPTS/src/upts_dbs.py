# import pandas as pd
import mysql.connector as mysql
from mysql.connector import errorcode
import requests

# Database Connection Variables
db_master = 'upts_s1'
db_host = '134.173.236.104'
db_user='prog_user'
db_password='Pr0gpass'
db_table = ""

# from upts_main import upts_users


# Open Database Connection and Print Confirmation
# If there's an Error, Report Error then Close Connection
def open_test_close():
    try:
        cnx = mysql.connect(user=db_user, password=db_password,
                                    host=db_host,
                                    database=db_master)
        print ('Connection Opened')
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
        print ('Connection Closed')


# Open Database Connection or Report Error - Does not Close Connection
def OpenDB():
    try:
        cnx = mysql.connect(user=db_user, password=db_password,
                                    host=db_host,
                                    database=db_master)
        # print('Connection Opened: ' + str(cnx))
        return cnx
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with Database user name or password")
            return err
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return err
        else:
            print(err)
            return err


# Close Database Connection
def CloseDB(cnx):
    # print ('should be closing')
    # c = cnx.cursor()
    # c.close()
    # cnx.close()
    # if cnx.close() == None:
    #      print('Connection Closed')
    return cnx

# ----------  START DATABASE TABLE FUNCTIONS

# Create a Table - Pass table_columns as a list
def createTable(cnx,db_table,table_columns):
    c = cnx.cursor()
    colCount = 0
    try:
        # Create table
        print (table_columns)
        sqlStatement = 'CREATE TABLE '+ db_table + ' ('
        for col_Name in table_columns:
            sqlStatement += col_Name
            if colCount < len (table_columns) - 1:
                sqlStatement += ', '
                colCount += 1
        sqlStatement += ')'
        print ('sql statement: ' + str(sqlStatement))

        c.execute(sqlStatement)
        cnx.commit()
        print('created ' + db_table + ' table')

    except Exception as identifier:
        print(str(identifier))
        # dropTable(cnx, 'users')




# class upts_db():

#     def __init__(self,user=db_user, password=db_password,
#                                         host=db_host,
#                                         database=db_master):

#         self.user=db_user
#         self.password=db_password
#         self.host=db_host
#         self.database=db_master
#         self.cnx = ""
#         self.csr = ""

#     # Create Database - NOT WORKING YET - Included for Reference
#     def create_database(self, cursor):
#         try:
#             cursor.execute(
#                 "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_master))
#         except mysql.Error as err:
#             print("Failed creating database: {}".format(err))
#             exit(1)

#         # try:
#         #     cursor.execute("USE {}".format(db_master))
#         # except mysql.Error as err:
#         #     print("Database {} does not exists.".format(db_master))
#         #     if err.errno == errorcode.ER_BAD_DB_ERROR:
#         #         create_database(cursor)
#         #         print("Database {} created successfully.".format(db_master))
#         #         cnx.database = db_master
#         #     else:
#         #         print(err)
#         #         exit(1)

