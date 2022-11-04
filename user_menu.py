from KDrama_Classes import KoreanShows, KDramaDB
from user_menu_utils import menu_option_3, menu_option_1, menu_option_2, menu_option_4

#this will be the main page that gets run

initial_greeting = "**********************************\n" \
                   "Hello, what would you like to do?\n" \
                   "**********************************\n\n" \
                   "1) View 'Completed' List \n2) View 'To Watch' List \n" \
                   "3) Add to 'Completed' List \n4) Add to 'To Watch' List \n5) Quit \n\n"

while True:
    menu_option = int(input(f"{initial_greeting}Please choose option 1, 2, 3, 4, or 5: "))

    if menu_option == 1:         # this will be a DB print
        menu_option_1()

    elif menu_option == 2:       # this will be a DB print
        menu_option_2()

    elif menu_option == 3:  # completed
        show_choice = input('\nWhat show are you looking for? ').title()
        menu_option_3(show_choice, menu_option) #update to remove input from function

    elif menu_option == 4: #to watch]]
        show_choice = input('\nWhat show are you looking for? ').title()
        menu_option_4(show_choice, menu_option) #update to remove input from function

    elif menu_option == 5:
        print("Goodbye\n")
        break

    else:
        print(f"Input not recognised, try again.") #re-runs while True


