#Alishya

# This lets us be able to use seperate files in one file
from High_Score_Tracker.game import play_game
from High_Score_Tracker.file import check_file
from High_Score_Tracker.high_score import display_top_ten, update
from High_Score_Tracker.user import store_user, check_user

#This is the main function that runs the user interface
def main():
    #This is the beginning of our whole program
    check_file()
    title = "\n\nWelcome to a rock paper scissors game!\n\n"
    title_case_string = title.title()
    print(title_case_string)

    #This lets it keep running over and over again until they want to exit
    while True:

        #Lets them input their option whithout worrying about leading/trailing space
        log_in_or_exit = input('What do you want to do?\n1. Log into an account\n2. Sign up\n3. Exit\nChoice: ').strip()

        #These check to see what option the user chose and gets information based off their choice
        match log_in_or_exit:
            case '1':
                #Logs into an account
                username = input('What is your username: ').strip()
                password = input('What is your password: ').strip()
                if check_user(username, password):
                    print(f"\nWelcome {username}!\n")
                    break
                else:
                    print("\nInvalid Username or Password\n")
                    continue
            case '2':
                #This signs up for an account that you later log into again
                username = input('What is your username: ').strip()
                password = input('What is your password: ').strip()
                if not store_user(username, password):
                    continue
                print(f"\nWelcome {username}\n")
                break

            case '3':
                #This exits the program
                print('Thank you for playing!')
                return

            case _:
                #This is for if they input something other than those options
                print('That is not an option. Try again')
                continue
    
    #This keeps running until they want to Log out
    while True:
        if log_in_or_exit == '3':
            break
        #These is the users choice's that they have to input that also doesn't have to worry about leading/trailing spaces
        choice = input('What would you like to do?\n1. Play Game\n2. Display top 10 scores\n3. Log out\nChoice: ').strip()

        #These are the outputs for the users input
        match choice:
            case '1':
                #Runs the play_game function
                score = play_game()
                update(name=username, score=score)
            case '2':
                #Displays the top ten high scores
                display_top_ten()
            case '3':
                #Logs out of their account
                print("You have logged out!")
                main()
            case _:
                #Makes sure they don't choose an option other than the ones provided
                print("That is not an option")
                continue

#This runs our main function before any of the rest
#if __name__ == "__main__":
#    main()