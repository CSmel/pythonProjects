# This program will ask the user to enter two integers
# and then display the maximum integer to the user.

def main():
    # Get first value.
    a = int(input('Enter the first value: '))
    # Gte second value.
    b = int(input('Enter the second value: '))
    print('---------------------')
    total = max(a, b)
    print('The maximum value is: ',total)
# The intro function will display the purpose of the program.
def intro():
    print('This program will ask the user to enter two values')
    print('and then display the maximum value to the user.')
    print()

# The max function accept two integersas arguments and
# returns the max of those arguments.
def max(x, y):
    if x > y:
        return x
    else:
        return y
intro()
main()


    
    



