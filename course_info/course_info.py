# Global constants.
LOOK_UP_ONE = 1
LOOK_UP_TWO = 2
LOOK_UP_THREE = 3
QUIT = 4

def main():
    # Room number's dictionary.
    room_number = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
# Teacher's name dictionary.
    name = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
# Meeting time's dictionary.
    meeting_time = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}

    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's choice.
        choice = menu_choice()
        if choice == LOOK_UP_ONE:
            look_up_room_number(room_number)
        elif choice == LOOK_UP_TWO:
            look_up_name(name)
        elif choice == LOOK_UP_THREE:
            look_up_meeting_time(meeting_time)

# The menu_choice function displays the menu
# and gets a validated number from the user.
def menu_choice():
    print('------------------------')
    print('1. Look up room number.')
    print('2. Look up teacher\'s name.')
    print('3. Look up meeting time.')
    print('4. Quit.')
    print('-------------------------')
    # Ask user to choice a number from the menu.
    choice = int(input('Enter your choice: '))
    
    # Validate the choice.
    while choice < LOOK_UP_ONE or choice > QUIT:
        choice = int(input('Enter a choice: '))# When choice is not a valid number, ask again.

    # Return the choice.
    return choice
    
    
# The look_up_room_number function will ask the user for a course number.
# The function will then search through the room_number dictionary to get
# the correct room number for that course number.
def look_up_room_number(room_number):
    search_room_number = input('Enter course number to locate the room number: ')
    print('Room number:',room_number.get(search_room_number))

# The look_up_name function will ask the user for a course number.
# The function will then search through the name dictionary to get
# the correct teacher's name for that course number.
def look_up_name(name):
    search_name = input('Enter course number to locate the teacher\'s name: ')
    print('Teacher\'s name: ',name.get(search_name))

# The look_up_meeting_time function will ask the user for a course number.
# The function will then search through meeting_time dictionary to get
# the correct meeting time for that course number.
def look_up_meeting_time(meeting_time):
    search_meeting_time = input('Enter course number to locate the meeting time: ')
    print('Meeting time: ',meeting_time.get(search_meeting_time))




main()


