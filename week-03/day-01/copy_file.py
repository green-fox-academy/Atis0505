# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful
first_file = "apple.txt"
second_file = "copy_file.txt"

def copy_file(from_file, to_file):
    try:
        file_01_string = open(from_file, "r")
        file_02_string = open(to_file, "w")
        from_string = file_01_string.readlines()
        for line in from_string:
            print(line)
        file_01_string.close()
        file_02_string.close()

        print("Done!")
    except IOError:
        print("Unable to write file, ",first_file)

copy_file(first_file,second_file)