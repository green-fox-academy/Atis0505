# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output
oneline = ""

for i in range(0,4):
    oneline=""
    for j in range(0,4):
        if i==j:
            oneline += "1"
        else:
            oneline +="0"
        oneline+=" "
    print(oneline)

matrix = []
size = 3
for n in range(size):
    row = []
    for m in range(size):
        if n==m:
            row.append("1")
        else: 
            row.append("0")
    matrix.append(row)

for matrix_row in matrix:
    print(matrix_row)