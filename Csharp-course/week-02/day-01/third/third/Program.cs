using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace third
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create an array variable named `q`
             int[]q = new int[] { 4, 5, 6, 7 };
            //   with the following content: `[4, 5, 6, 7]`
            // - Print the third element of `q`
            Console.WriteLine("Original array is:");
            for (int i = 0; i < q.Length; i++)
            {
                Console.WriteLine("{0}. item is {1}",i+1,q[i]);
            }
            Console.WriteLine("Third element of array is {0}",q[2]);
            Console.ReadLine();
        }
    }
}
