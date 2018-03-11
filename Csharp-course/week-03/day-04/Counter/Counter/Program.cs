using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Counter
{
    class Program
    {
        static void Main(string[] args)
        {
            // Write a recursive function that takes one parameter: n and counts down from n.
            Counter(10);
            Console.ReadKey();
        }

        public static void Counter(int number)
        {
            if(number == 0)
            {
                Console.WriteLine("Number: {0}", number);
            }
            else
            {
                Console.WriteLine("Number: {0}", number);
                Counter(number - 1);
            }
        }
        
    }
}
