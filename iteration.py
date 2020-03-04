index = 0

while index < 10:
    print('Application is running')
    print(f"index: {index}")
    index += 1


while index < 10:
    print('App is running')
    print(f"index: {index}")
    index += 1

    if index == 3:
        break


with open('sample.txt', 'r') as fl:
    output_data = fl.read()
    output_data += '\nI added another line from Python code'
    print(output_data)


with open('output.txt', 'w') as fl:
    fl.write(output_data)


# loop over a string
# while loop
# for loop
# read from a file
# write to a file
# String methods

