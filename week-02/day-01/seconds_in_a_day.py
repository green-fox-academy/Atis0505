current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables

seconds = int((60-current_seconds) + (60-current_minutes-1)*60 + (24-current_hours-1) * 3600)
print(seconds)