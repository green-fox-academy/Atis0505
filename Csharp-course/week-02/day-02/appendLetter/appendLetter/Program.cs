using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appendLetter
{
    class Program
    {
        static void Main(string[] args)
        {
            var far = new List<string> { "kuty", "macsk", "kacs", "rók", "halacsk" };
            // Create a method called AppendA() that adds "a" to every string in the far list.
            // The parameter should be a list.

            Console.WriteLine(string.Join(" ",AppendA(far)));
            Console.ReadKey();
            // Expected output: "kutya", "macska", "kacsa", "róka", "halacska"
        }

        public static List<string> AppendA(List<string> inputList)
        {
            for (int i = 0; i < inputList.Count; i++)
            {
                inputList[i] = inputList[i] + "a";
            }
            return inputList;
        }
    }
}
