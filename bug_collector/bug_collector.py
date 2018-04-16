# this program will calculate the amount
#of bugs being collected over a  day span.

max = 5

# Initiate  an accumulator variable
total = 0.0

#  Ask user to enter the amount of bugs that were collected
# over a five day span.
for counter in range(max):
    bugs = int(input('How many bugs were collected? '))
    total = total + bugs

# Display the amount of bugs collected over the five day span
print('The amount of bugs collected over a five day span is: ',total,'bug(s)')
