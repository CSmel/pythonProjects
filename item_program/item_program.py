import retailitem

def main():

    # Get a list for the retail objects.
    info = make_list()

    # Display the data in the list.
    display_list(info)


    # The _list function will ask the user how many retail items need
    # to be entered. The function will then return a list of item objects
    # containing the data.

def make_list():
    # Create an empty list.
    retail_list = []
    
   
   
    amount = int(input('How many items do you need to add to the list? '))     
    for count in range(amount):
        # Get information from user.
        print('----------')
        print('Item #' + str(count + 1) + ':')
        print('----------')
        descr = input('Enter item description: ')
        units = int(input('Enter the amount of unit(s): '))
        _price = float(input('Enter the price of the unit: '))
        print()

        # Creat a new RetailItem object  and assign it to the
        # retail variable.
        retail = retailitem.RetailItem(descr, units, _price)

        # Add the object to the list.
        retail_list.append(retail)

        # Return the list.

    return retail_list

    # The display_list function accepts a list containing
    # RetailItem objects as an object and displays the data stored
    # in each object.

def display_list(retail_list):
    print('These are the items that you added:')
    print('---------------------------------')

    for item in retail_list:
    

        print('Item description: ',item.get_item_descr(), sep='')
        print('Unit(s): ',item.get_units_inven(), sep='')
        print('Price: $', format(item.get_price(),',.2f'), sep='')
        print()
# Call the main functio.
main()
                      
