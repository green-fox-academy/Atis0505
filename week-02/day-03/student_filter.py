students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def moreCandies():
    for n in range(len(students)):
        if students[n]['candies'] > 4:
            print(students[n]['name'])
   

def averageCandies():
    sum = 0
    for n in range(len(students)):
        sum += students[n]['candies']
    print(sum/n)
moreCandies()
averageCandies()