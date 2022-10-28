import requests
from pprint import pprint as pp
from creditials_API import tmdb_api_key_v3

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

    @classmethod
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
        tv_shows = show_info['results']
        korean_tv_shows = list(filter(self.is_korean_show, tv_shows))
        initial_result = self.get_first_show(korean_tv_shows)
        return initial_result

    @classmethod
    def get_first_show(self, k_tv):
        first_result = k_tv.pop(0)  # this variable is now a dict
        self.show_name = first_result.pop('name')
        self.show_release = first_result.pop('first_air_date')
        self.show_overview = first_result.pop('overview')
        show_data_list = [f"Show title: {self.show_name}", f"Show release date: {self.show_release}",
                          f"Show overview: {self.show_overview}"]
        pp(show_data_list)
        return show_data_list

    @classmethod
    def is_search_correct(self, result):
        if result == 'Y':
            print('added\n')  # append the entry to DB or file
        elif result == 'N':
            print('Sorry\n')  # pull up second result if available
        else:
            print("Input not accepted\n")



class KDramaDB(KoreanShows):

    def get_to_watch(self):
        pass

    def get_completed(self):
        pass

    def insert_show_to_watch(self):
        pass

    def insert_show_complete(self):
        pass