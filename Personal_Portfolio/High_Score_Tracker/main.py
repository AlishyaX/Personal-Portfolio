#Alishya

# This lets us be able to use seperate files in one file
from High_Score_Tracker.game import play_game
from High_Score_Tracker.file import check_file
from High_Score_Tracker.high_score import display_top_ten, update
from High_Score_Tracker.user import store_user, check_user

#This is the main function that runs the user interface
def main():
    # This is the beginning of our whole program
    check_file()
    title = "\n\nWelcome to a Rock Paper Scissors Game!\n\n"
    title_case_string = title.title()
    print(title_case_string)

    while True:
        log_in_or_exit = input('What do you want to do?\n1. Log into an account\n2. Sign up\n3. Exit\nChoice: ').strip()

        match log_in_or_exit:
            case '1':
                # Logs into an account
                username = input('What is your username: ').strip()
                password = input('What is your password: ').strip()
                if check_user(username, password):
                    print(f"\nWelcome {username}!\n")
                    while True:
                        # Second menu after logging in
                        choice = input('What would you like to do?\n1. Play Game\n2. Display top 10 scores\n3. Log out\nChoice: ').strip()

                        match choice:
                            case '1':
                                # Runs the play_game function
                                score = play_game()
                                update(name=username, score=score)
                            case '2':
                                # Displays the top ten high scores
                                display_top_ten()
                            case '3':
                                # Logs out of their account and returns to the first menu
                                print("You have logged out!")
                                break  # Breaks out of second loop to return to first menu
                            case _:
                                # Handles invalid input
                                print("That is not an option")
                else:
                    print("\nInvalid Username or Password\n")
            case '2':
                # Signs up for a new account
                username = input('What is your username: ').strip()
                password = input('What is your password: ').strip()
                if not store_user(username, password):
                    continue
                print(f"\nWelcome {username}!\n")
                # Automatically goes to the second menu after signing up
                while True:
                    choice = input('What would you like to do?\n1. Play Game\n2. Display top 10 scores\n3. Log out\nChoice: ').strip()

                    match choice:
                        case '1':
                            # Runs the play_game function
                            score = play_game()
                            update(name=username, score=score)
                        case '2':
                            # Displays the top ten high scores
                            display_top_ten()
                        case '3':
                            # Logs out of their account and returns to first menu
                            print("You have logged out!")
                            break  # Breaks out of second loop to return to first menu
                        case _:
                            # Handles invalid input
                            print("That is not an option")
            case '3':
                # Exits the High Score Tracker entirely and returns to the portfolio
                print('Thank you for playing!')
                return  # Exits to portfolio menu
            case _:
                # Handles invalid input
                print('That is not an option. Try again')