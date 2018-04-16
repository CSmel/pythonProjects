    # This program converts kilometers to miles.
CONVERSTION_VALUE = 0.6214
    # The main function get the distance in kilometers and calls
    # the show_miles function to covert it.
def main():
    # Ask for distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles.
    show_miles(kilometers)
    #
    # The show_miles function converts the parameter km from
    # kilometers to miles and displays the result.
def show_miles(km):
    # Calculate miles.
    miles = km * CONVERSTION_VALUE

    # Display the miles.
    print(km, 'kilometers equals to',\
          format(miles,'.3f'),'miles')
    # Calls the main function.
main()
