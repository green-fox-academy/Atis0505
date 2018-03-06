using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TeachersStudents
{
    class Student
    {
        public Student()
        {

        }

        public void Learn()
        {
            Console.WriteLine("Student learning!");
        }

        public void Question(Teacher teacher)
        {
            teacher.Answer();
        }

    }
}
