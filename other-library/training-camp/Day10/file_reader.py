with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    # print(contents)
    # print(contents.rstrip())

    # for line in file_object:
    #     print(line)
    for line in file_object:
        print(line.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())