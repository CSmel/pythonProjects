# Constant for thenumber of inches per foot
INCHES_PER_FOOT = 12

# Main functions.
def main():
    # Get the number of feet from the user
    feet = int(input('How many feet? '))

    # Display and convert feet to inches
    print(feet,'feet converted to inches is:',feet_to_inches(feet),'inches.')
    
# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * 12

# Call the main function.
main()
