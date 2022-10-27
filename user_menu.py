from show_data import is_search_correct, show_search, show_choice

#this will be the main page that gets run

initial_greeting = "Hello, what would you like to do? \n1) View 'Completed' List \n" \
                   "2) View 'To Watch' List \n3) Add to 'Completed' List \n4) Add to 'To Watch' List \n"
menu_option = int(input(f"{initial_greeting}Please choose option 1, 2, 3, or 4: "))

if menu_option == 1:
    print('test')
    exit(0)  # this will be a DB print
elif menu_option == 2:
    print('test')
    exit(0)  # this will be a DB print
elif menu_option == 3:  # completed
    show_search(show_choice)
    is_correct = input("Is this the correct show? Y/N ").upper()
    is_search_correct(is_correct)
    # is this show correct func
    # if yes, append, if no pull next result (if i can lol)
elif menu_option == 4:
    show_search(show_choice)
    is_correct = input("Is this the correct show? Y/N ").upper()
    is_search_correct(is_correct)    # is this show correct func
    # if yes, append, if no pull next result (if i can lol)
else:
    print(f"Input not recognised, try again.")