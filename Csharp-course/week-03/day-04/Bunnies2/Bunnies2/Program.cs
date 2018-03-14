using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Bunnies2
{
    class Program
    {
        static void Main(string[] args)
        {
            // We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
            // (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
            // have 3 ears, because they each have a raised foot. Recursively return the
            // number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

            Console.WriteLine("Earn's number with 6 bunnies: {0}", CountBunniesEarn(6));
            Console.WriteLine("Earn's number with 5 bunnies: {0}", CountBunniesEarn(5));
            Console.WriteLine("Earn's number with 4 bunnies: {0}", CountBunniesEarn(4));
            Console.WriteLine("Earn's number with 3 bunnies: {0}", CountBunniesEarn(3));
            Console.WriteLine("Earn's number with 2 bunnies: {0}", CountBunniesEarn(2));
            Console.WriteLine("Earn's number with 0 bunnies: {0}", CountBunniesEarn(0));
            Console.ReadKey();
        }

        public static int CountBunniesEarn(int bunniesNumber, int numberOfEarn = 0)
        {
            if (bunniesNumber == 0)
            {
                numberOfEarn += 0;
            }
            else
            {
                if (bunniesNumber % 2 == 0)
                {
                    numberOfEarn += CountBunniesEarn(bunniesNumber - 1, 3);
                }
                else
                {
                    numberOfEarn += CountBunniesEarn(bunniesNumber - 1, 2);
                }
            }
            return numberOfEarn;
        }
    }
}
