from High_Score_Tracker.high_score import write, load

USER_PATH = "user.csv" 

# Store username as key and password as values to csv file
def store_user(username: str, password: str) -> None:
    username = username.lower()
    users = load(USER_PATH)

    # check if username is already used
    if username in users:
        print("\nUsername is already used\n")
        return False
    
    users[username] = password

    write(USER_PATH, users)

    return True

# Check if username and password is valid
def check_user(username: str, password: str) -> bool:
    username = username.lower()
    users = load(USER_PATH)

    if username in users:
        if password == users[username]:
            return True
    return False

if __name__ == "__main__":

    while True:
        log_in_or_exit = input('What do you want to do?\n1. Log into an account\n2. Sign up\n3. Exit\nChoice: ').strip()

        match log_in_or_exit:
            case '1':
                username = input('What is your username: ').strip()
                password = input('What is your password: ').strip()
                if check_user(username, password):
                    print(f"\nWelcome {username}\n")
                    break
                else:
                    print("\nInvalid Username or Password\n")
                    continue
            case '2':
                username = input('What is your username: ').strip()
                password = input('What is your password: ').strip()
                store_user(username, password)
                continue

            case '3':
                print('Thankyou for playing!')
                break

            case _:
                print('That is not an option. Try again')
                continue