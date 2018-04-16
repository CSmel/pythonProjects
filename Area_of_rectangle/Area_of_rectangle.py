#ask user for dimensions of first rectangle
length_one = int(input('What is the length of the first rectangle? '))
width_one = int(input('What is the width of the first rectangle? '))

#calculate the area of the first rectangle
area_one = length_one * width_one

#ask user for dimensions of the second rectangle
length_two = int(input('What is the length of the second rectangle? '))
width_two = int(input('What is the width of the second rectangle? '))

#calculate the area of the second rectangle
area_two = length_two * width_two

#if statement
if area_one == area_two:
    print('WE HAVE A MATCH!')
if area_one > area_two:
    print('The first rectangle has a bigger area!')
if area_one < area_two:
    print('The second rectangle has a bigger area!')
