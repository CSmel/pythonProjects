# Open a file.
myfile = open('numbers.txt','r')

# Read and line in the file and display it.
for line in myfile:
    print(line)

# Close the file.
myfile.close()
