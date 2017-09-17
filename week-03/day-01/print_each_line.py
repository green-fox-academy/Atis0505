# Write a program that opens a file called "my-file.txt", then prints
# each of lines form the file.
# If the program is unable to read the file (for example it does not exists),
# then it should print an error message like: "Unable to read file: my-file.txt"

file_address = "example_file_01.txt"

def read_file(file_txt):
    try:
        file = open(file_txt,"r")
        my_file = file.readlines()
        for line in my_file:
            print(line.rstrip())
        file.close()
    except IOError:
        print("Unable to read file: ",file_txt)

read_file(file_address)