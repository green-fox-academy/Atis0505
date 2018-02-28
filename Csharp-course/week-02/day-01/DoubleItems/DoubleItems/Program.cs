using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DoubleItems
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create an array variable named `ag`
            //   with the following content: `[3, 4, 5, 6, 7]`
            int[] ag = { 3, 4, 5, 6, 7 };
            // - Double all the values in the array
            for (int i = 0; i < ag.Length; i++)
            {
                ag[i] = ag[i] * 2;
                Console.WriteLine(ag[i]);
            }
            Console.ReadLine();
        }
    }
}
