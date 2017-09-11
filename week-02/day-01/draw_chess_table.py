# Crate a program that draws a chess table like this
#
# % % % % 
#  % % % %
# % % % %
#  % % % %
# % % % %
#  % % % %
# % % % % 
#  % % % %
#
p = ""
for i in range(1,9):
    if i % 2 == 0:
        for j in range(1,9):
            if j % 2 == 0:
                p += "%"
            else:
                p += " "
    else:
        for j in range(1,9):
            if j % 2 == 0:
                p += " "
            else:
                p += "%"
    print(p)
    p = ""
