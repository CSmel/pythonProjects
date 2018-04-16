
# State is the variable for the dictionary
# Florida is the key.
# Tallahasee is a value.

# The state dictionary.
state = {
        'Alabama':'Montgomery',
        'Alaska':'Juneau',
        'Arizona':'Phoenix',
        'Arkansas':'Little Rock',
        'California':'Sacramento',
        'Colorado':'Denver',
        'Connecticut':'Hartford',
        'Delaware':'Dover',
        'Florida':'Tallahassee',
        'Georgia':'Atlanta',
        'Hawaii':'Honolulu',
        'Idaho':'Boise',
        'Illinois':' Springfield',
        'Indiana':'Indianapolis',
        'Iowa':'Des Moines',
        'Kansas':'Topeka',
        'Kentucky':'Frankfort',
        'Louisiana':'Baton Rouge',
        'Maine':'Augusta',
        'Maryland':'Annapolis',
        'Massachusetts':'Boston',
        'Michigan':'Lansing',
        'Minnesota':'Saint Paul',
        'Mississippi':'Jackson',
        'Missouri':'Jefferson City',
        'Montana':'Helena',
        'Nebraska':'Lincoln',
        'Nevada':'Carson City',
        'New Hampshire':'Concord',
        'New Jersey':'Trenton',
        'New Mexico':'Santa Fe',
        'New York':'Albany',
        'North Carolina':'Raleigh',
        'North Dakota':'Bismarck',
        'Ohio':'Columbus',
        'Oklahoma':'Oklahoma City',
        'Oregon':'Salem',
        'Pennsylvania':'Harrisburg',
        'Rhode Island':'Providence',
        'South Carolina':'Columbia',
        'South Dakota':'Pierre',
        'Tennessee':'Nashville',
        'Texas':'Austin',
        'Utah':'Salt Lake City',
        'Vermont':'Montpelier',
        'Virginia':'Richmond',
        'Washington':'Olympia',
        'West Virginia':'Charleston',
        'Wisconsin':'Madison',
        'Wyoming':'Cheyenne',
        }
# Initialize a value that counts the amount of  correct answers.
true = 0
# Initialize a value that counts the amount of  incorrect answers.
false = 0
print('What are the capitals for the following states?')
# The for loop will only literate 50 times.
for question in range(2):
    key, value = state.popitem()
    # The key will be randomly chosen and then displayed.
    # Once the program asks the user to enter a value.  That value should match
    # the key in the state dictionary.
    print('The captial of',key,'is _______.')
    question = input('Your answer: ')
    # If the value matches the key in the dictionary count one.
    if question == value:
        true += 1
        print('Correct')# Display the word correct so that the user knows the
        print()         # answer was correct.

    # If the value does not match the key in the dictionary count one.
    else:
        false += 1
        print('Incorrect')# Display the word incorrect so that the user knows they got the
        print()           # answer incorrect.
       
# Display the total amount of correct and incorrect answers.
print('You have',true,'correct and',false,'incorrect.')
    

