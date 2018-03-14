using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace String01
{
    class Program
    {
        static void Main(string[] args)
        {
            // Given a string, compute recursively (no loops) a new string where all the
            // lowercase 'x' chars have been changed to 'y' chars.
            Console.WriteLine("Green Fox Foxies string : {0}", StringChanger("Green Fox Foxies"));
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
                    actualChar += StringChanger(givenString.Substring(1), "y");
                }
            }
            return actualChar;
        }
    }
}
