using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sumdigit
{
    class Program
    {
        public static int sumdigit = 0;
        static void Main(string[] args)
        {
            // Given a non-negative int n, return the sum of its digits recursively (no loops). 
            // Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
            // divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

            int number = 12345;
            Sumdigit(number);

            Console.ReadKey();
        }

        public static void Sumdigit(int number)
        {
            if (number / 10 == 0 && number <= 9)
            {
                sumdigit += number;
                Console.WriteLine("Sum of digits: {0}", sumdigit);
            }
            else
            {
                string numStr = number.ToString();
                int div = 10;
                Console.WriteLine(number / Convert.ToInt32(Math.Pow(div, (numStr.Length-1))));
                sumdigit += number / Convert.ToInt32(Math.Pow(div, (numStr.Length-1)));
                Console.WriteLine(number % Convert.ToInt32(Math.Pow(div, (numStr.Length-1))));
                Sumdigit(number % Convert.ToInt32(Math.Pow(div, (numStr.Length-1))));
            }
        }
    }
}
