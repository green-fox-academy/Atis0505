using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Power
{
    class Program
    {
        public static int resul = 1;
        static void Main(string[] args)
        {
            // Given base and n that are both 1 or more, compute recursively (no loops)
            // the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
            Console.WriteLine("Result: {0}", powerN(3,4));
            Console.ReadKey();
        }

        public static int powerN(int numBase, int numPower)
        {
            if (numPower == 1)
            {
                resul *= numBase;
            }
            else
            {
                resul *= numBase;
                powerN(numBase, numPower-1);
            }
            return resul;
        }
    }
}
