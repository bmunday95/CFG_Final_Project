import string
import stringprep

import requests
from pprint import pprint as pp
from creditials_API import tmdb_api_key_v3, show_db_format
from database_connection import connect_to_db, execute_query

"""
Show class - each method within it must do one thing:
1) Search
2) Show lists
3) Insert to lists
4) Remove from lists

"""

class KoreanShows:

    def __init__(self):
        self.show_choice = ""
        self.show_name = ""
        self.show_release = ""
        self.show_overview = ""

    @classmethod #had to add this to avoid missing positional arguments in menu page
    def is_korean_show(self, tv_dict):  # filter function for KR shows
        origin_country_list = tv_dict['origin_country']
        if 'KR' in origin_country_list:
            return True
        else:
            return False

    @classmethod
    def korean_show_search(self, show_choice):
        response_show = requests.get(
            f"https://api.themoviedb.org/3/search/tv?api_key={tmdb_api_key_v3}&query={show_choice}")
        show_info = response_show.json()
        # print(show_info)
        tv_shows = show_info['results']
        if tv_shows:
            korean_tv_shows = list(filter(self.is_korean_show, tv_shows))
            initial_result = self.get_first_show(korean_tv_shows)
            return initial_result
        else:
            return False

    @classmethod
    def get_first_show(self, k_tv):
        first_result = k_tv.pop(0)  # this variable is now a dict
        self.show_name = first_result.pop('name')
        self.show_release = first_result.pop('first_air_date')
        self.show_overview = first_result.pop('overview')
        show_data_list = [f"Show title: {self.show_name}", f"Show release date: {self.show_release}",
                          f"Show overview: {self.show_overview}"]
        print("\n".join(show_data_list))  # this is just personal preference,the output is easier to read than pp
        return show_data_list




"""
Decided to put the DB work in a child class, not sure if this is best practice? I wanted to keep the DB work separate 
from the search, but it still needs access to the info that was pulled from the API
"""
class KDramaDB(KoreanShows):

    def db_data(self):
        return show_db_format(self.show_name, self.show_release, self.show_overview)

    @classmethod
    def is_search_correct(self, menu_option, result):
        if menu_option == 3:
            if result == 'Y':#call insert func
                self.insert_show_complete()
                print('\nShow added to Completed List\n')
            elif result == 'N':
                print('\nSorry\n')  # pull up second result if available? This needs some functionality
            else:
                print("\nInput not accepted\n")

        elif menu_option == 4:
            if result == 'Y':  # call insert func
                self.insert_show_to_watch()
                print('\nShow added to Watch List\n')  # append the entry to DB or file
            elif result == 'N':
                print('\nSorry\n')
            # pull up second result if available? This needs some functionality
            else:
                print("\nInput not accepted\n")
            return result


    @classmethod
    def get_completed(self):
        query = "SELECT * FROM completed_shows"  # update to cleaner search
        result = execute_query(query)
        for entry in result:  # this will show the whole list, but i could probs make it show individ entries? further search functionality
            print(entry)
        print('\nConnection closed\n\n')
        return result #what to return?

    @classmethod
    def get_to_watch(self):
        query = "SELECT * FROM watch_list"  # update to cleaner search
        result = execute_query(query)
        for entry in result:  # this will show the whole list, but i could probs make it show individ entries? further search functionality
            print(entry)
        print('\nConnection closed\n\n')
        return result #what to return?

    @classmethod
    def insert_show_to_watch(self):
        values_to_add = self.db_data(self)
        query = 'INSERT INTO watch_list (show_title, show_release, show_overview) ' \
                f'VALUES ("{values_to_add.show_name}", "{values_to_add.show_release}", ' \
                f'"{values_to_add.show_overview}");'
        result = execute_query(query)
        return result

    @classmethod
    def insert_show_complete(self):
        values_to_add = self.db_data(self)
        query = 'INSERT INTO completed_shows (show_title, show_release, show_overview) ' \
                f'VALUES ("{values_to_add.show_name}", "{values_to_add.show_release}", ' \
                f'"{values_to_add.show_overview}");'
        result = execute_query(query)
        return result


