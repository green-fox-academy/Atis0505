class Person:
    def __init__(self, name = "Jane Doe", age = 30, gender = "female"):
        self.name = name
        self.age = age
        self. gender = gender

    
    def introduce(self):
        print('Hi, I\'m {}, a {} years old {}'.format(self.name, self.age, self.gender))

    
    def get_goal(self):
        print("My goal is: Live for the moment!")