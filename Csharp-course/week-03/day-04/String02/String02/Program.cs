using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace String02
{
    class Program
    {
        static void Main(string[] args)
        {
            // Given a string, compute recursively a new string where all the 'x' chars have been removed.
            Console.WriteLine("New string from 'Foxies at Green Fox Academy': {0}",StringChanger("Foxies at Green Fox Academy"));
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
                if (givenString[0] != 'x')
                {
                    actualChar += StringChanger(givenString.Substring(1), givenString[0].ToString());
                }
                else
                {
                    actualChar += StringChanger(givenString.Substring(1), "");
                }
            }
            return actualChar;
        }
    }
}
