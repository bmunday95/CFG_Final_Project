#create db?
import mysql.connector
from creditials_API import USER, PASSWORD, HOST

test_username = 'th0rtilla'

def connect_to_db(username):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=username
    )
    return connection

#maybe make the DB name specific like a user? i.e. insert your username: = input = db name

def display_completed_list(username):
    try:
        username = test_username
        # db engine provides connection to db
        db_connection = connect_to_db(username)
        # cursor allows us to execute queries
        cur = db_connection.cursor()
        print('Database connection successful')

        query = f"SELECT * FROM completed_shows" #update to cleaner search
        cur.execute(query)
        result = cur.fetchall()

        for entry in result: #this will show the whole list, but i could probs make it show individ entries? further search functionality
            print(entry)
        cur.close()

    except Exception:
        raise DbConnectionError #create this

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')

def display_to_watch_list(username):
    try:
        username = test_username
        # db engine provides connection to db
        db_connection = connect_to_db(username)
        # cursor allows us to execute queries
        cur = db_connection.cursor()
        print('Database connection successful')

        query = f"SELECT * FROM watch_list" #update to cleaner search
        cur.execute(query)
        result = cur.fetchall()

        for entry in result: #this will show the whole list, but i could probs make it show individ entries? further search functionality
            print(entry)
        cur.close()

    except Exception:
        raise DbConnectionError #need to create this?

    finally:
        if db_connection:
            db_connection.close()
            print('Connection closed')

def add_completed_show():
    pass #use the SQL statements to add entries

def add_to_watchlist():
    pass

connect_to_db(test_username)
display_completed_list(test_username)

# def insert_record_in_table(record):
#     try:
#         db_name = 'tests'
#         # db engine provides connection to db
#         db_connection = connect_to_db(db_name)
#         # cursor allows us to execute queries
#         cur = db_connection.cursor()
#         print('Database connection successful')
#
#         query = "INSERT INTO abcreport (OrderDate, Region, Rep, Item, Units, UnitCost) " \
#                 "VALUES ('2022-04-18','West','Beth','Pencil',26,1.99)"
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