using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace reverse
{
    class Program
    {
        static void Main(string[] args)
        {
            string reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI";
            // Create a method that can reverse a String, which is passed as the parameter
            // Use it on this reversed string to check it!

            Console.WriteLine(Reverse(reversed));
            Console.ReadKey();
        }

        public static string Reverse(string charChain)
        {
            string newString = String.Empty;
            for (int i = charChain.Length-1; i >= 0; i--)
            {
                newString += charChain[i];
            }
            return newString;
        }
    }
}
