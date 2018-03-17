using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GreenFox
{
    class Program
    {
        static void Main(string[] args)
        {
            /*Test output:
             
                Hi, I'm Mark, a 46 year old male.
                My goal is: Live for the moment.
                Hi, I'm Jane Doe, a 30 year old female.
                My goal is: Live for the moment.
                Hi, I'm John Doe, a 20 year old male from BME who skipped 0 days from the course already.
                My goal is: Be a junior software developer.
                Hi, I'm Jane Doe, a 30 year old female from The School of Life who skipped 3 days from the course already.
                My goal is: Be a junior software developer.
                Hi, I'm Gandhi, a 148 year old male senior mentor.
                My goal is: Educate brilliant junior software developers.
                Hi, I'm Jane Doe, a 30 year old female intermediate mentor.
                My goal is: Educate brilliant junior software developers.
                Hi, I'm Jane Doe, a 30 year old female who represents Google and hired 5 students so far.
                My goal is: Hire brilliant junior software developers.
                Hi, I'm Elon Musk, a 46 year old male who represents SpaceX and hired 3 students so far.
                My goal is: Hire brilliant junior software developers.
                The AWESOME cohort has 2 students and 2 mentors.*/

            var people = new List<Person>();

            var mark = new Person("Mark", 46, "male");
            people.Add(mark);
            var jane = new Person();
            people.Add(jane);
            var john = new Student("John Doe", 20, "male", "BME");
            people.Add(john);
            var student = new Student();
            people.Add(student);
            var gandhi = new Mentor("Gandhi", 148, "male", "senior");
            people.Add(gandhi);
            var mentor = new Mentor();
            people.Add(mentor);
            var sponsor = new Sponsor();
            people.Add(sponsor);
            var elon = new Sponsor("Elon Musk", 46, "male", "SpaceX");
            people.Add(elon);

            student.SkipDays(3);

            for (int i = 0; i < 3; i++)
            {
                elon.Hire();
            }
            for (int i = 0; i < 5; i++)
            {
                sponsor.Hire();
            }

            foreach (var person in people)
            {
                person.Introduce();
                person.GetGoal();
            }

            Cohort awesome = new Cohort("AWESOME");
            awesome.AddStudent(student);
            awesome.AddStudent(john);
            awesome.AddMentor(mentor);
            awesome.AddMentor(gandhi);
            awesome.Info();

            Console.ReadKey();
        }
    }
}
