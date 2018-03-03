using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace incrementElement
{
    class Program
    {
        static void Main(string[] args)
        {
            //- Create an array variable named `t`
            //  with the following content: `[1, 2, 3, 4, 5]`
            int[] t = { 1, 2, 3, 4, 5 };
            //- Increment the third element
            t[2]++;
            //- Print the third element
            Console.WriteLine("Third element is {0}", t[2]);
            Console.ReadLine();
        }
    }
}
