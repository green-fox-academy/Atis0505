#Anagram.py


def check_is_anagram(first_word, second_word):
        if first_word == "" or second_word == "":
            return -1
        else:
            if len(first_word) == len(second_word):
                if sorted(first_word.lower()) == sorted(second_word.lower()):
                    return True