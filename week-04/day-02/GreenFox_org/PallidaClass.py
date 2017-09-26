from Student import Student
from Mentor import Mentor

class PallidaClass:
    def __init__(self, class_name):
        self.class_name = class_name
        self.list_of_students = []
        self.list_of_mentors = []


    def add_student(self, student):
        self.list_of_students.append(student)


    def add_mentor(self, mentor):
        self.list_of_mentors.append(mentor)


    def info(self):
        print("Pallida {} class has {} students and {} mentors.".format(self.class_name, str(len(self.list_of_students)), str(len(self.list_of_mentors))))