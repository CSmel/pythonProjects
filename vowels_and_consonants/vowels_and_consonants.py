# Main function.
def main():
    # Get a string from the user.
    string = input('Enter a string of characters: ')

    # Report the vowels and consonants.
    print('That string has', num_vowels(string),'vowels and',\
          num_cons(string), 'consonants.')

# The num_vowels function returns the number of
# vowels in the string passed as an argument.
def num_vowels(s):
    # Make a list containing the vowels.
    vowels = ['a','e','i','o','u']

    # Initialize an accumulator.
    vol_count = 0

    # Count rhe consonants in s.
    for ch in s:
        if ch.lower() in vowels:
            vol_count += 1

    # Return the consonant count.
    return vol_count

# The num_cons function returns the number of
# consonants in the string passed as an argument.
def num_cons(s):
    # Make a list containing the vowels.
    vowels = ['a','e','i','o','u']

    # Initialize an accumulator.
    cons_count = 0

    # Count the consonants in s.
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            cons_count += 1
    # Return the consonant count.
    return cons_count
# Call the main function.
main()
