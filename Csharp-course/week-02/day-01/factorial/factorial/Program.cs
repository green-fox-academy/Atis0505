using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace factorial
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create a function called `factorio`
            //   that returns it's input's factorial
            Console.WriteLine("Result of factorio method: {0}", factorio(5));
            Console.ReadLine();
        }

        public static int factorio(int number)
        {
            int result = 1;
            for (int i= 1; i <= number; i++)
            {
                result *= i;
            }
            return result;
        }
    }
}
