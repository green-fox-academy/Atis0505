using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GreenFox
{
    class Sponsor : Person
    {
        protected string companyName;
        protected int hiredStudent;

        public Sponsor(string _name, int _age, string _gender, string company)
        {
            this.name = _name;
            this.age = _age;
            this.gender = _gender;
            this.companyName = company;
        }

        public Sponsor()
        {
            name = "JaneDoe";
            age = 30;
            gender = "female";
            this.companyName = "Google";
            this.hiredStudent = 0;
        }

        public override void Introduce()
        {
            Console.WriteLine("Hi, I'm {0}, a {1} year old {2} who represents {3} and hired {4} students so far.", this.name, this.age, this.gender, this.companyName, this.hiredStudent);
        }

        public void Hire()
        {
            this.hiredStudent++;
        }

        public override void GetGoal()
        {
            Console.WriteLine("Hire brilliant junior software developers!");
        }
    }
}
