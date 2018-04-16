
# Ask user for how many years of rainfall to be used in calculations.
num_years = int(input('How many years? '))

# Determine how many years.
print()
for years in range(num_years):
    total = 0               # Initialize an accumulator for number of inches of rainfall.
    
    print('---------------')
    print('Year',years + 1)
    print('---------------')
                            # Display the amount of months within a range of 12.
    for num_months in range(12): 
        print('Month',num_months + 1, end='')
        print()
        num_inches = float(input('How many inches? ',))# Ask for user's inches.
                            # Perform calculation for total amount of inches.
        total += num_inches
                            # Print total rainfall for that year.
    print('Total rainfall for year',years + 1, 'is:',total,'Inches') 
    average = total / 12    # Perform calculation for average.
    print('Average rainfall for year',years + 1, 'is:',\
          format(average,'.2f'),'Inches')
    
 
   
