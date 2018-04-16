# Ask user to enter to enter first, middle and last name.
# Intro function.
def intro():
    print('This program will ask the user to enter his or her')
    print('first, middle and last name. The program will then')
    print('display the user\'s full name and their initials.')
    print()

# Main function.
def main():
    # Enter first name.
    first_name = input('Enter first name: ')

    # Enter middle name.
    middle_name = input('Enter middle name: ')

    # Enter last name.
    last_name = input('Enter last name: ')

    full_name = first_name + ' ' + middle_name + ' ' + last_name

    # Display the full name.
    print('Full name: ',full_name)

    # Innitials variable
    initial_string = first_name[:1] + '. ' + middle_name[:1] + '. ' + last_name [:1] + '. '

    # Display the initials.
    print('Initial\'s: ',initial_string)

# Call intro function.
intro()
# Call main function.
main()
