#find anagram second chapter

first_word = "ohhh"
second_word = "hhohh"


def check_len(word_string_01, word_string_02):
    if len(word_string_01) == len(word_string_02):
        sort_words(word_string_01,word_string_02)
    else:
        print("The lengths are not same!")
    

def sort_words(word_01, word_02):
    word_01_list = list(word_01)
    word_01_list.sort()
    print(word_01_list)
    word_02_list = list(word_02)
    word_02_list.sort()
    print(word_02_list)
    if word_01_list == word_02_list:
        print("Anagram!!")
    else:
        print("Not anagram!!")


check_len(first_word, second_word)
