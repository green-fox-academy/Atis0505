using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FleetOfThings
{
    class Thing
    {
        private string Name;
        private bool Completed;

        public Thing(string name)
        {
            this.Name = name;
        }

        public void Complete()
        {
            this.Completed = true;
        }

        public void Print()
        {
            if (this.Completed)
            {
                Console.WriteLine("[X] {0}", this.Name);
            }
            else
            {
                Console.WriteLine("[ ] {0}", this.Name);
            }
        }
    }
}
