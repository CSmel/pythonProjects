import ProductionWorker

# Get costomer information.
name = input('Name: ')
number = input('Employee Number: ')
shift_number = int(input('Choose Shift 1,2, or 3: '))

pay_rate = float(input('Hourly Pay Rate: '))






# Create an instance of the sutomer class.
my_productionworker = ProductionWorker.ProductionWorker(name, number, shift_number, pay_rate)

# Display the object's data.
print('Employee Information')
print('--------------------')
print('Name:', my_productionworker.get_name())
print('Employee Number:', my_productionworker.get_number())
print('Shift Number:', my_productionworker.get_shift_number())
print('Hourly Pay Rate: $', format(my_productionworker.get_pay_rate(),'.2f'), sep='')

