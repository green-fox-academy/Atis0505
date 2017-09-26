from Person import Person

class Sponsor(Person):
    def __init__(self, name = "Jane Doe", age = 30, gender = "female", company = "Google", hired_students = 0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students


    def get_goal(self):
        print("Hire brilliant junior software developers.")


    def introduce(self):
        print("Hi, I'm {}, a {} year old {}  who represents {} and hired {} students so far.".format(self.name, self.age, self.gender, self.company, self.hired_students))

    
    def hire(self):
        self.hired_students += 1
    