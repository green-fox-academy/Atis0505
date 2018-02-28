using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sumElements
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create an array variable named `r`
            //   with the following content: `[54, 23, 66, 12]`
            int[] r = { 54, 23, 66, 12 };
            Console.WriteLine("Sum of the second and third element: {0}",r[1]+r[2]);
            // - Print the sum of the second and the third element
            Console.ReadLine();
        }
    }
}
