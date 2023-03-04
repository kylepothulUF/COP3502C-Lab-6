# Kyle Pothul

# initializes a variable to store the encoded password
ENCODED_PASSWORD = ''


# starts the user menu
def main():
    user_input_menu()


# displays the input menu
def user_input_menu():
    user_menu_input = int(input('''
    Menu  
    ------------- 
    1. Encode  
    2. Decode  
    3. Quit
     
    Please enter an option: '''))

    # encodes an inputted password
    if user_menu_input == 1:
        encode()

    # decodes the current encoded password
    if user_menu_input == 2:
        decode()

    # exits the application
    elif user_menu_input == 3:
        exit()

    # if the user's input is invalid, displays an error and redisplays the menu
    else:
        print('''
        Invalid input!
        Please enter an integer value between 1 and 3.''')
        user_input_menu()


# encodes a given password
def encode():
    global ENCODED_PASSWORD

    user_password = input('Please enter your password to encode: ')

    # increases the value of each digit place in the inputted password by 3
    for index in range(0, len(user_password)):
        encoded_value = int(user_password[index]) + 3

        # if the value ends up higher than 9, reduce the value by 10 so it stays a single digit
        if encoded_value > 9:
            encoded_value -= 10

        # adds the encoded digit to the new encoded password
        ENCODED_PASSWORD += str(encoded_value)

    # tells the user their password was encoded and redisplays the input menu
    print('Your password has been encoded and stored!')
    user_input_menu()


# starts the application
if __name__ == '__main__':
    main()
