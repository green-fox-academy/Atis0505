using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Animal
{
    class Anim
    {
        int hunger;
        int thirst;

        public Anim()
        {
            this.hunger = 50;
            this.thirst = 50;
        }

        public void Eat()
        {
            this.hunger--;
        }

        public void Drink()
        {
            this.thirst--;
        }

        public void Play()
        {
            this.thirst++;
            this.hunger++;
        }

        public void GetValues()
        {
            Console.WriteLine("Hunger point: {0}, Thirst point: {1}", this.hunger, this.thirst);
        }

        public int GetHungryPoint()
        {
            return this.hunger;
        }
    }
}
