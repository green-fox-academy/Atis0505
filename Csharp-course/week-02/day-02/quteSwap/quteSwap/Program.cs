using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace quteSwap
{
    class Program
    {
        static void Main(string[] args)
        {
            var list = new List<string> { "What", "I", "do", "create,", "I", "cannot", "not", "understand." };

            // Accidentally I messed up this quote from Richard Feynman.
            // Two words are out of place
            // Your task is to fix it by swapping the right words with code
            // Create a method called QuoteSwap().

            // Also, print the sentence to the output with spaces in between.
            Console.WriteLine(string.Join(" ",QuoteSwap(list)));
            Console.ReadKey();
            // Expected output: "What I cannot create I do not understand." 
        }

        public static List<string> QuoteSwap(List<string> stringList)
        {
            string temp = stringList[2];
            stringList[2] = stringList[5];
            stringList[5] = temp;
            return stringList;
        }
    }
}
