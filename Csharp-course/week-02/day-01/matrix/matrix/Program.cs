using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace matrix
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create (dynamically) a two dimensional array
            //   with the following matrix. Use a loop!
            //
            //   1 0 0 0
            //   0 1 0 0
            //   0 0 1 0
            //   0 0 0 1
            //
            // - Print this two dimensional array to the output
            int a = 4;

            for (int x = 0; x < a; x++)
            {
                for (int y = 0; y < a; y++)
                {
                    if (x == y)
                    {
                        Console.Write("1 ");
                    }else
                    {
                        Console.Write("0 ");
                    }
                }
                Console.WriteLine();
            }
            Console.ReadLine();
        }
    }
}
