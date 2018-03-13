using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bunny1
{
    class Program
        {

        public static int numberOfBunny = 0;
        static void Main(string[] args)
        {
            // We have a number of bunnies and each bunny has two big floppy ears.
            // We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
            Console.WriteLine("Number of bunnies: {0}", CountBunny(21));
            Console.WriteLine("Number of bunnies: {0}", CountBunny(22));
            Console.ReadKey();
        }

        public static int CountBunny(int earnNumber)
        {
            if (earnNumber % 2 != 0)
            {
                Console.WriteLine("The number of bunny's earn should be even number!!!");
                numberOfBunny = -1;
            }
            else if(earnNumber - 2 == 0 )
            {
                numberOfBunny += 1;
            }
            else
            {
                numberOfBunny += 1;
                CountBunny(earnNumber - 2);
            }
            return numberOfBunny;
        }
    }
}
