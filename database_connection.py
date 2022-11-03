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


"""
All data stored in the same DB, but each user could have their own tables - if I have the time it could be 
a name input and the tables could be Beth_completed_list for example
"""
