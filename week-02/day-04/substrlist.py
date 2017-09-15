# Find the substring in the list

# Create a function that takes a string and a list of string as a parameter
# Returns the index of the string in the list where the first string is part of
# Returns -1 if the string is not part any of the strings in the list
# Example

# input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
# output: 4
string_list = ["this", "is", "what", "I'm", "searching", "in"]
key_string = "this"

def check_string(word, str_list):
    index = -1
    for word_from_list in str_list:
        index += 1
        if not -1 == word_from_list.find(word):
            print(word_from_list.find(word))


check_string(key_string,string_list)