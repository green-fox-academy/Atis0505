class Student(object):
    def learn(self):
        print("I'm learning!")


    def question(self):
        Teacher.answer(self)


class Teacher(object):
    def teach(self):
        Student.learn(self)


    def answer(self):
        print("Answer!")

teacher_01 =Teacher()
teacher_01.teach()
student_01 = Student()
student_01.question()