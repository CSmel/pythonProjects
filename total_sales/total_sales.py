
# Ask user to enter the amount of sales for each day of the week.
# The constant for days is the number seven becuase there are seven days in a week.
days = 7

def main():
    # Create a list to hold the sales
    # for each day
    sales = [0] * days

    # Creat a variable to hold an index.
    index = 0
    
    print('Enter the sales for each day.')
    print()
    # Display the number of days within the range of seven.
    for weeks in range(days):
        print('Day',index + 1)# Display the day number for each loop iteration.
        sales[index] = float(input('Enter daily sales: '))# Ask user to input daily sales and store values into a list named sales.
        index += 1                                       
    
    sales_list_sum = sum(sales) # Formula used to calculate the sum of daily sales.
    print()
    print('Total weekly sales: $',\
    format(sales_list_sum,'.2f')) # Display the total weekly sales.
    
# Call the main function.
main()
    
