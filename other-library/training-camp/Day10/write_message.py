filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("Hello World.")
    # file_object.write(1)
    file_object.write("I love\n")
    file_object.write("Python.")