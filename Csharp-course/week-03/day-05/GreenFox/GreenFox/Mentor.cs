using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GreenFox
{
    class Mentor : Person
    {
        protected string level;

        public Mentor(string _name, int _age, string _gender, string _level)
        {
            this.name = _name;
            this.age = _age;
            this.gender = _gender;
            this.level = _level;
        }

        public Mentor()
        {
            name = "Jane Doe";
            age = 30;
            gender = "female";
            level = "intermediet";
        }

        public override void Introduce()
        {
            Console.WriteLine("Hi, I'm {0}, a {1} year old {2} {3} mentor", this.name, this.age, this.gender, this.level);

        }

        public override void GetGoal()
        {
            Console.WriteLine("Educate brilliant junior software developers!");
        }
    }
}
