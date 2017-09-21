# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def string_checker(string):
    if string == "":
        return ""
    elif len(string) == 1:
        return string[0]
    else: 
        return string[0] + "*" + string_checker(string[1:])
        

print(string_checker("xxxxxkjkn"))