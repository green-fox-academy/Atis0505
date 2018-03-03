using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appendA
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create a string variable named `am` and assign the value `kuty` to it
            string am = "kuty";
            // - Write a function called `appendA` that gets a string as an input,
            //   appends an 'a' character to its end and returns with a string
            // - Print the result of `appendAFunc(am)`
            Console.WriteLine("Append function result: {0}",appendFunc(am));
            Console.ReadLine();
        }

        public static string appendFunc(string word)
        {
            return word + "a";
        }
    }
}
