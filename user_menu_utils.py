from KDrama_Classes import KoreanShows, KDramaDB

"""
Functions for the menu options
"""

def menu_option_1(): #completed
    print("Completed list: \n")
    KDramaDB.get_completed()

def menu_option_2(): #to watch
    print("To Watch list: \n")
    KDramaDB.get_to_watch()

def menu_option_3(show_choice, menu_option):
    while not KoreanShows.korean_show_search(show_choice):
        print("No results")
        show_choice = input('\nWhat show are you looking for? ').title()
    is_correct = input("\nIs this the correct show? Y/N ").upper()
    KDramaDB.is_search_correct(menu_option, is_correct)

def menu_option_4(show_choice, menu_option):
    while not KoreanShows.korean_show_search(show_choice):
        print("No results")
        show_choice = input('\nWhat show are you looking for? ').title()
    is_correct = input("\nIs this the correct show? Y/N ").upper()
    KDramaDB.is_search_correct(menu_option, is_correct)