# Find part of an integer

# Create a function that takes two strings as a parameter
# Returns the starting index where the second one is starting in the first one
# Returns -1 if the second string is not in the first one
# Example

# input: "this is what I'm searching in", "searching"
# output: 17

string01 = "this is what I'm searching in"
string02 = "searching"

def search_string(st01, st02):
    index = 0

    if st02 in st01:
        a = st02[0]
        for b in  st01:
            if b == a:
                if st01[index:index+len(st02)] == st02:
                    return index
            index += 1
    return -1

print(search_string(string01,string02))
