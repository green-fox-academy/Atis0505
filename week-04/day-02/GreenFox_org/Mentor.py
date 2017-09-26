from Person import Person

class Mentor(Person):
    def __init__(self, level = "intermediate"):
        self.level = level

    
    def get_goal(self):
        print("Educate brilliant junior software developers.")


    def introduce(self):
        print("Hi, I'm {}, a {} year old {} {} mentor.".format(self.name, self.age, self.gender, self.level))