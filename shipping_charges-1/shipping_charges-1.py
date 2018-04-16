
#ask user for the weight of the package
weight = int(input('What is the weight of the package? '))

#Find the correct shipping charge
if weight <= 2:                         #less than 2 pounds
    print('The shipping charge is $1.10')
elif weight >= 3 and weight <= 6:       #between 3 to 6 pounds
    print('The shipping charge is $2.20')
elif weight >= 7 and weight <= 10:      #between 7 to 10 pounds
    print('The shipping charge is $3.70')
else:                                   #over 10 pounds
    print('The shipping charge is $3.80')
    



