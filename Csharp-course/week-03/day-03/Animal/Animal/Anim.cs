using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Animal
{
    class Anim
    {
        static int hunger;
        static int thirst;

        public Anim()
        {
            hunger = 50;
            thirst = 50;
        }

        public void Eat()
        {
            hunger--;
        }

        public void Drink()
        {
            thirst--;
        }

        public void Play()
        {
            thirst++;
            hunger++;
        }

        public void GetValues()
        {
            Console.WriteLine("Hunger point: {0}, Thirst point: {1}", hunger, thirst);
        }
    }
}
