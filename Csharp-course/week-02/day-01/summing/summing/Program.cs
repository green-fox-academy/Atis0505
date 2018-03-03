using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace summing
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Write a function called `sum` that sum all the numbers
            //   until the given parameter and returns with an integer
            Console.WriteLine("Sumall method result: {0}", sumAll(5)); 
            Console.ReadKey();
        }

        public static int sumAll(int number)
        {
            int sum = 0;
            for (int i = 0; i <= number; i++)
            {
                sum += i;
            }
            return sum;
        }
    }
}
