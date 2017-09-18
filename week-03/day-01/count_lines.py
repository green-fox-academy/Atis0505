# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

file_address = "example_file_02.txt"

def read_file(file_txt):
    try:
        counter = 0
        file = open(file_txt,"r")
        for line in file:
            counter +=1
        file.close()
        print("Lines number in the file: ",counter)
    except IOError:
        return 0

print(read_file(file_address))