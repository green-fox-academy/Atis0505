# This should be a simple word counter which give us the most common word in a file
# If ran from the command line without arguments it should print out the usage:
# python most_common_word.py [source]
# When the argument provided and the source is a file
# count all words in the given file and print the most common 
# ("cat", "CAT", "cat," "cat." are different words ) 

test_file_source = "test_file.txt"

def read_file(test_file):
    with open(test_file, "r") as f:
        for line in f:
            words_list = line.strip().split(" ")
    check_words_in_list(words_list)


def check_words_in_list(list_of_words):   
    words_dict = {} 
    for item in list_of_words:
        if item in words_dict:
            words_dict[item] += 1
        else:
            words_dict[item] = 1
    max_value = max(words_dict.values())
    most_word = [key for key, value in words_dict.items() if value == max_value]
    print(most_word)


read_file(test_file_source)