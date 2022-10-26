import requests
from pprint import pprint as pp
from creditials_API import tmdb_api_key_v3
from bool_functions import is_korean_show

#search by show name - this is the primary function
def show_search():
    response_show = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={tmdb_api_key_v3}&query={show_input()}")
    show_info = response_show.json()
    tv_shows = show_info['results']
    korean_tv_shows = list(filter(is_korean_show, tv_shows))
    show_list(korean_tv_shows)
    return korean_tv_shows

def show_input():
    show_choice = input('What show are you looking for? ')
    show_choice.title()
    return show_choice

# can i use index and then pop to remove the specific searched show and then return it as a variable? then add that vriable to our db/list
def show_list(k_tv): #can i make this cleaner?
    first_result = k_tv.pop(0)  # this variable is now a dict
    show_name = first_result.pop('name')
    release_date = first_result.pop('first_air_date')
    show_overview = first_result.pop('overview')
    show_data_list = [f"Show title: {show_name}", f"Show release date: {release_date}",
                      f"Show overview: {show_overview}"]
    pp(show_data_list)
    return show_data_list

#how do i access these variables to add them to the DB??

def user_menu():
    initial_greeting = "Hello, what would you like to do? \n1) View 'Completed' List \n" \
                       "2) View 'To Watch' List \n3) Add to 'Completed' List \n4) Add to 'To Watch' List \n"
    menu_option = int(input(f"{initial_greeting}Please choose option 1, 2, 3, or 4: "))

    if menu_option == 1:
        pass #this will be a DB print
    elif menu_option == 2:
        pass #this will be a DB print
    elif menu_option == 3: #completed
        show_search()
        is_search_correct()
        #is this show correct func
        #if yes, append, if no pull next result (if i can lol)
    elif menu_option == 4:
        show_search()
        is_search_correct()
        #is this show correct func
        # if yes, append, if no pull next result (if i can lol)
    else:
        print(f"Input not recognised, try again.")

    return menu_option

def is_search_correct():
    is_correct = input("Is this the correct show? Y/N ").upper()
    if is_correct == 'Y':
        print('added') # append the entry to DB or file
    elif is_correct == 'N':
        print('Sorry') # pull up second result if available
    else:
        print("Input not accepted")


def completed_show():
    completed_date = input("When did you finish the show? YYYY-MM-DD ")
    pass


user_menu()