using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GreenFox
{
    class Cohort
    {
        protected string name;
        protected List<Student> students = new List<Student>();
        protected List<Mentor> mentors = new List<Mentor>();

        public Cohort(string _name)
        {
            this.name = _name;
            this.students.Clear();
            this.mentors.Clear();
        }

        public void AddStudent(Student _student)
        {
            this.students.Add(_student);
        }

        public void AddMentor(Mentor _mentor)
        {
            this.mentors.Add(_mentor);
        }

        public void Info()
        {
            Console.WriteLine("The {0} cohort has {1} students and {2} mentors.", this.name, this.students.Count, this.mentors.Count);
        }
    }
}
