# This program will use the file named names.txt
# and calculate the total amount of names in the file.

def intro():
    print('This program will use the file named names.txt')
    print('and calculate the total amount of names in it.')
    print()

def main():
    # Open the names.txt file to read.
    names_file = open('names.txt','r')

    # Initialize an accumulator
    # to keep total of names.
    total = 0
    # Inialize an accumulator
    # to keep number track of each name.
    count = 0

    print('The names in the file are: ')
    print('-----------------')

    # Get the values from the file and figure out the total.
    for line in names_file:
        # Convert a line to a float.
        amount_of_names = (line)

        # Add 1 to the count variable.
        count += 1
        

        # Display the name.
        print('Name',count,':',amount_of_names)

        # Add 1 to the total variable.
        total += 1
    print('-----------------')   
    print('There are a total of',total,'name(s) in the names.txt file.')
    
      

    # Close the file.
    names_file.close()
intro()
# Close main function.  
main()
