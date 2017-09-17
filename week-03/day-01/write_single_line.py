# Open a file called "my-file.txt"
# Write your name in it as a single line
# If the program is unable to write the file,
# then it should print an error message like: "Unable to write file: my-file.txt"
file_address = "my_file.txt"

def write_in_file(file_text):
    try:
        my_file = open(file_text, "w")
        my_file.writelines("Kőröm Attila")
        my_file.close()
        print("Done!")
    except IOError:
        print("Unable to write file, ",file_text)

write_in_file(file_address)