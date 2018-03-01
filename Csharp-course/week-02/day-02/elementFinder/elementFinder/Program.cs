using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace elementFinder
{
    class Program
    {
        static void Main(string[] args)
        {
            var List = new List<int> { 1, 2, 3, 4, 5, 7 };
            var List2 = new List<int> { 1, 2, 3, 4, 5 };
            Console.WriteLine(ContainsSeven(List));
            Console.WriteLine(ContainsSeven(List2));
            // Write a method that checks if the arrayList contains "7" if it contains return "Hoorray" otherwise return "Noooooo"
            // The output should be: "Noooooo"
            // Do this again with a different solution using different list methods!
            Console.ReadKey();
        }

        public static string ContainsSeven(List<int> numberList)
        {
            for (int i = 0; i < numberList.Count; i++)
            {
                if(numberList[i] == 7)
                {
                    return "Hoorray";
                }
            }
            return "Noooooo";
        }
    }
}
