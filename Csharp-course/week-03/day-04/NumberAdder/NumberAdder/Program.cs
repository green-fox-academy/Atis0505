using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NumberAdder
{
    class Program
    {
        public static int result = 0;
        static void Main(string[] args)
        {
            // Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
            NumberAdder(5);
            Console.Read();
        }

        public static void NumberAdder(int number)
        {
            
            if (number == 1)
            {
                Console.WriteLine("Number {0}", number);
                result += 1;
                Console.WriteLine("Result: {0}", result);
            }
            else
            {
                result += number;
                Console.WriteLine("Number {0}", number);
                NumberAdder(number - 1);
            }
        }
    }
}
