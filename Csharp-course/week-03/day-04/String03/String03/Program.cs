using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace String03
{
    class Program
    {
        static void Main(string[] args)
        {
            // Given a string, compute recursively a new string where all the
            // adjacent chars are now separated by a "*".
            Console.WriteLine("Adjancent chars separated by *: {0}", StringChanger("Green fox academy"));
            Console.ReadKey();
        }

        public static string StringChanger(string givenString, string actualChar = "")
        {
            if (givenString == "" || givenString == null)
            {
                return actualChar;
            }
            else
            {
                actualChar += StringChanger(givenString.Substring(1), givenString[0].ToString()+"*");
            }
            return actualChar;
        }
    }
}
