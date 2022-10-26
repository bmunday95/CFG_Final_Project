import requests
import json
import flask
import sqlite3
from pprint import pprint as pp
from creditials_API import tmdb_api_key_v3

def show_input():
    show_choice = input('What show are you looking for? ')
    show_choice.title()
    return show_choice

#user menu in separate file

#search by show name - create function
def show_search():
    response_show = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={tmdb_api_key_v3}&query={show_input()}")
    show_info = response_show.json()
    tv_shows = show_info['results']
    korean_tv_shows = list(filter(is_korean_show, tv_shows))
    first_result = korean_tv_shows.pop(0)
    # second_result = korean_tv_shows.pop(1)
    pp(first_result)
    return korean_tv_shows

def is_korean_show(tv_dict): #filter function for KR shows
    origin_country_list = tv_dict['origin_country']
    if 'KR' in origin_country_list:
        return True
    else:
        return False



show_search()