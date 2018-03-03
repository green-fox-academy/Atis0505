using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace unique
{
    class Program
    {
        static void Main(string[] args)
        {
            //  Create a function that takes a list of numbers as a parameter
            //  Returns a list of numbers where every number in the list occurs only once
            var numbersLisr = new List<int> { 1, 11, 34, 11, 52, 61, 1, 34 };
            //  Example
            Unique(numbersLisr);
            //  should print: `[1, 11, 34, 52, 61]`
            Console.ReadKey();
        }

        public static void Unique(List<int> gettingList)
        {
            var uniqueList = new List<int>{ };
            for (int i = 0; i < gettingList.Count; i++)
            {
                if(!uniqueList.Contains(gettingList[i]))
                {
                    uniqueList.Add(gettingList[i]);
                }
            }
            Console.WriteLine("Unique numbers: ");
            for (int j = 0; j < uniqueList.Count; j++)
            {
                Console.Write(uniqueList[j]+ " ");
            }
        }
    }
}
