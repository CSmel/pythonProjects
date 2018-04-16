# The insurance rate.
INSURANCE_RATE = .80

def main():
    rep_cost = float(input('Cost of replacement for building: $ '))
    print('--------------------------------------------')
    show_insurance_rate(rep_cost)
def intro():
    print('This program will calculate the minimum')
    print('amount of insurance he or she should buy')
    print('for their property.')
  
    print('The formula is:')
    print('INSURANCE RATE COST = REPLACEMENT COST X 80%')
    print('--------------------------------------------')
# The show_insurance_rate function accepts the rep_cost
# as an argument and displays the insurance rate to
# the amount of repair cost.
def show_insurance_rate(cost):
    insurance_cost = cost * INSURANCE_RATE
    print('The mininum amount of ')
    print('insurance you should purchase is: $',\
          format(insurance_cost,'.2f'))
# Call the main function.

intro()   
main()    
    
