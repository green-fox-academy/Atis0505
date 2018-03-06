using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TeachersStudents
{
    class Teacher
    {
        public Teacher() { }

        public void Teach(Student student)
        {
            student.Learn();
        }

        public void Answer()
        {
            Console.WriteLine("This is the answer!");
        }
    }
}
