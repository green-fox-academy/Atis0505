def check_words(word01,word02):
    if len(word01) == len(word02):
        if sorted(word01) == sorted(word02):
            return True
    return False

