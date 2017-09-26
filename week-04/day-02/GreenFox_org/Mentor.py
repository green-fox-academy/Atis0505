from Person import Person

class Mentor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "famela", level = "intermediate"):
        super().__init__(name, age, gender)
        self.level = level

    
    def get_goal(self):
        print("Educate brilliant junior software developers.")


    def introduce(self):
        print("Hi, I'm {}, a {} year old {} {} mentor.".format(self.name, self.age, self.gender, self.level))