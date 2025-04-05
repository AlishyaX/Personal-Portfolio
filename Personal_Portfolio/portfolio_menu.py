#Alishya Xavier, Personal Portfolio
import time
from Battle_Simulator.main import main as battle_main
from Coin_Change_Problem.main import main as coin_main
from financial_calculator.main import main as financial_main
from High_Score_Tracker.main import main as score_main
from Random_password_generator.main import main as password_main
from Simple_Morse_Code_Translator.main import main as translator_main
from project_details import show_project_details 
from projects_data import projects


def programming_portfolio():
    print('Welcome to my Programming Portfolio!')
    print('Here you can see some of the projects I am most proud of.')
    print('To use this portfolio, please enter a number for which project you want to see in the menu.')

    while True:
        options = input(
            'Menu:\n1. Project 1: Battle Simulator\n2. Project 2: Coin Change Problem\n3. Project 3: Financial Calculator\n4. Project 4: High Score Tracker\n5. Project 5: Random Password Generator\n6. Project 6: Simple Morse Code Translator\n7. Exit\nChoice: '
        )

        if options == '1':
            show_project_details(projects[0])
            battle_main()  # Call Battle Simulator program
            time.sleep(3)

        elif options == '2':
            show_project_details(projects[1])
            coin_main()  # Call Coin Change Problem program
            time.sleep(3)

        elif options == '3':
            show_project_details(projects[2])
            financial_main()  # Call Financial Calculator program
            time.sleep(3)

        elif options == '4':
            show_project_details(projects[3])
            score_main()  # Call High Score Tracker program
            time.sleep(3)

        elif options == '5':
            show_project_details(projects[4])
            password_main()  # Call Random Password Generator program
            time.sleep(3)

        elif options == '6':
            show_project_details(projects[5])
            translator_main()  # Call Simple Morse Code Translator program
            time.sleep(3)

        elif options == '7':
            print('Thank you for using my personal portfolio!')
            exit()

        else:
            print('That is not an option. Try Again...')
            continue
if __name__ == "__main__":
    programming_portfolio()