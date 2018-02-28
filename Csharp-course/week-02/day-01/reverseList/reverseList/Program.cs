using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reverseList
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create an array variable named `aj`
            //   with the following content: `[3, 4, 5, 6, 7]`
            // - Reverse the order of the elements in `aj`
            // - Print the elements of the reversed `aj`
            int[] aj = { 3, 4, 5, 6, 7 };
            for (int i = 0; i <= aj.Length/2; i++)
            {
                int temp = aj[i];
                aj[i] = aj[aj.Length -1 - i];
                aj[aj.Length-1 - i] = temp;
            }

            for (int i = 0; i < aj.Length; i++)
            {
                Console.Write(aj[i]+ " ");
            }
            Console.ReadLine();
        }
    }
}
