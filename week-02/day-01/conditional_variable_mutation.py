w = 25
out = 0
# if w is even increment out by one
if w % 2 == 0:
    out = 1
    print(out)
else:
    print(out)




b = 3
out2 = ""
if 10 < b < 20:
    out2 = "Sweet"
    print(out2)
elif 10 > b:
    out2 = "More"
    print(out2)
else:
    out2 = "Less!"
    print(out2)
# if b is between 10 and 20 set out2 to "Sweet!"
# if less than 10 set out2 to "More!",
# if more than 20 set out2 to "Less!"

c = 123
credits = 100
is_bonus = True
# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same
if is_bonus == False:
    if credits > 50:
        c = c-2
    else:
        c = c-1
else:
    print(c)

d = 8
time = 120
out3 = ""
# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"
if d % 4 == 0:
    if time <= 200:
        out3="Check"
        print(out3)
    else:
        out3="Time out"
        print(out3)
else:
    out3 = "Run Forest Run!"
    print(out3)
