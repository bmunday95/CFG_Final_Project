#create db?
import mysql.connector
from creditials_API import USER, PASSWORD, HOST, DB_NAME

def connect_to_db(func):
    def inner_function(query):
        connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=DB_NAME
        )
        cur = connection.cursor() #assigns cursor to a variable
        result = func(query, cur) #the function being wrapped MUST take 2 variables
        connection.commit() #will commit changes, but doesnt do anything to view
        cur.close() #close cursor
        connection.close() #close connection
        return result
    return inner_function

@connect_to_db #the func being wrapped up needs to take 2 arguments
def execute_query(query, cur=None): #set cursor as None so it doesn't mess with the wrapping?
    cur.execute(query)
    return cur.fetchall() #this didnt work when I assigned it to a variable


def display_completed_list():
    query = "SELECT * FROM completed_shows" #update to cleaner search
    result = execute_query(query)
    for entry in result: #this will show the whole list, but i could probs make it show individ entries? further search functionality
        print(entry)
    print('Connection closed')
    return


def display_to_watch_list():
    query = "SELECT * FROM watch_list"  # update to cleaner search
    result = execute_query(query)
    for entry in result:  # this will show the whole list, but i could probs make it show individ entries? further search functionality
        print(entry)
    print('Connection closed')

def add_completed_show():
    query = ""
    result = execute_query(query)
    pass #use the SQL statements to add entries
    #when adding, include if statement - if show in watchlist then remove from watch list

def add_to_watchlist():
    query = ""
    result = execute_query(query)
    pass


"""
All data stored in the same DB, but each user could have their own tables - if I have the time it could be 
a name input and the tables could be Beth_completed_list for example
"""

# def insert_record_in_table(record):
#     try:
#         db_name = 'tests'
#         # db engine provides connection to db
#         db_connection = connect_to_db(db_name)
#         # cursor allows us to execute queries
#         cur = db_connection.cursor()
#         print('Database connection successful')
#
#         query = f"INSERT INTO  completed_shows (show_title, show_release, show_overview) " \
#                 "VALUES ({},{},{})"
#         cur.execute(query)
#         db_connection.commit() #you have to explicitly commit it to make the change work
#         cur.close()
#
#     except Exception:
#         raise DbConnectionError
#
#     finally:
#         if db_connection:
#             db_connection.close()
#             print('Connection closed')