using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GreenFox
{
    class Student : Person
    {
        public string previousOrganization;
        public int skippedDays;

        public Student(string _name, int _age, string _gender, string prevOrg)
        {
            this.name = _name;
            this.age = _age;
            this.gender = _gender;
            this.previousOrganization = prevOrg;
            this.skippedDays = 0;
        }

        public Student()
        {
            name = "Jane Doe";
            age = 30;
            gender = "female";
            previousOrganization = "The School of Life";
            skippedDays = 0;
        }

        public override void GetGoal()
        {
            Console.WriteLine("Hi, I'm name, a {0} year old {1} {2} from {3} who skipped {4} days from the course already.",this.name,this.age,this.gender,this.previousOrganization, this.skippedDays);
        }

        public int SkipDays(int number)
        {
            return this.skippedDays += number;
        }
    }
}
