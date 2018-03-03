using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace compareLength
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create an array variable named `p1`
            //   with the following content: `[1, 2, 3]`
            int[] p1 = { 1, 2, 3 };
            // - Create an array variable named `p2`
            //   with the following content: `[4, 5]`
            int[] p2 = { 4, 5 };
            // - Print if `p2` has more elements than `p1`
            if (p2.Length > p1.Length)
            {
                Console.WriteLine("P2 has more element!");
                printArrayElements(p2);
            }else
            {
                Console.WriteLine("P1 has more elements!");
                printArrayElements(p1);
            }
            Console.ReadLine();
        }

        public static void printArrayElements(int[] arrayItem)
        {
            for (int i = 0; i < arrayItem.Length; i++)
            {
                Console.WriteLine("{0}. element is {1}",i+1,arrayItem[i]);
            }
        }
    }
}
