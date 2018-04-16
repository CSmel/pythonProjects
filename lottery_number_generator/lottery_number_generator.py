# Import random module.
import random


# The program constants.
MAXIMUM = 7
START = 0
END = 9

 # The main function.
def main():
    
    # Create a list.
    winning_numbers = [0] * MAXIMUM

    # Create a list with the random numbers.
    for index in range(MAXIMUM):
        winning_numbers[index] = random.randint(START, END)
        

    # Display the winning numbers.
    print('The winning numbers are:')
    for index in range(MAXIMUM):
        # Display the winning numbers.
        print(winning_numbers[index],end='')
        


# The introduction function.
def intro():
    # Display the purpose of the program.
    print('This program will produce 7 random numbers.')
    print('The numbers will be in the range of 0 to 9.')
    print('-------------------------------------------')

# Call the intro function.
intro()

# Call the main function.
main()


