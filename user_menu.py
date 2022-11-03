from KDrama_Classes import KoreanShows, KDramaDB

#this will be the main page that gets run

initial_greeting = "**********************************\n" \
                   "Hello, what would you like to do?\n" \
                   "**********************************\n\n" \
                   "1) View 'Completed' List \n2) View 'To Watch' List \n" \
                   "3) Add to 'Completed' List \n4) Add to 'To Watch' List \n5) Quit \n\n"

while True:
    menu_option = int(input(f"{initial_greeting}Please choose option 1, 2, 3, 4, or 5: "))

    if menu_option == 1:         # this will be a DB print
        print("Completed list: \n")
        KDramaDB.get_completed()
    elif menu_option == 2:       # this will be a DB print
        print("To Watch list: \n")
        KDramaDB.get_to_watch()
    elif menu_option == 3:  # completed
        show_choice = input('\nWhat show are you looking for? ').title()
        menu_option3(show_choice)

    elif menu_option == 4: #to watch
        show_choice = input('\nWhat show are you looking for? ').title()
        KoreanShows.korean_show_search(show_choice)
        is_correct = input("\nIs this the correct show? Y/N ").upper()
        KDramaDB.is_search_correct(menu_option, is_correct)
        # is this show correct func
        # if yes, append, if no pull next result (if i can - additional functionality)
    elif menu_option == 5:
        print("Goodbye\n")
        break

    else:
        print(f"Input not recognised, try again.") #re-runs while True


def menu_option3(show_choice):
    while not KoreanShows.korean_show_search(show_choice):
            print("No results")
            show_choice = input('\nWhat show are you looking for? ').title()
    is_correct = input("\nIs this the correct show? Y/N ").upper()
    KDramaDB.is_search_correct(menu_option, is_correct)
