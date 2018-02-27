using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace greeter
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create a string variable named `al` and assign the value `Greenfox` to it
            string al = "Greenfox";
            // - Create a function called `greet` that greets it's input parameter
            //     - Greeting is printing e.g. `Greetings dear, Greenfox`
            // - Greet `al`
            greeting(al);
            Console.ReadKey();
        }

        public static void greeting (string name)
        {
            Console.WriteLine("Greetings dear, {0}", name);
        }
    }
}
