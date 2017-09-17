# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.
# The word parameter should be a string, that will be written to the file as lines
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.

path_string = "apple.txt"
word_string = "Apple"
loop_number = 5

def word_5_times(file_txt, word_st, loop_numb):
    try:
        my_file = open(file_txt, "w")
        for i in range(loop_numb):
            my_file.write(word_st + "\n")
        my_file.close()
        print("Done!")
    except IOError:
        print("Unable to write file, ",file_text)

word_5_times(path_string, word_string, loop_number)