using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppendAtoWords
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create an array variable named `nimals`
            //   with the following content: `["kuty", "macsk", "cic"]`
            // - Add all elements an `"a"` at the end
            string[] nimals = { "kuty", "macsk", "cic" };
            for (int i = 0; i < nimals.Length; i++)
            {
                nimals[i] = nimals[i] + "a";
                Console.WriteLine(nimals[i]);
            }
            Console.ReadLine();
        }
    }
}
