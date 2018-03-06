using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TeachersStudents
{
    class Program
    {
        static void Main(string[] args)
        {
            /*Create Student and Teacher classes
                Student
                    learn()
                    question(teacher)->calls the teachers answer method
                Teacher
                    teach(student)->calls the students learn method
                    answer()*/

            Student student = new Student();
            Teacher teacher = new Teacher();
            student.Question(teacher);
            teacher.Teach(student);


            Console.ReadKey();
        }
    }
}
