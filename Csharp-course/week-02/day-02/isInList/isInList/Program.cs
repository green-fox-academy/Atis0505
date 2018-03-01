using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace isInList
{
    class Program
    {
        static void Main(string[] args)
        {
            var list = new List<int> { 2, 4, 6, 8, 10, 12, 14, 16 };

            // Check if list contains all of the following elements: 4,8,12,16
            // Create a method that accepts list as an input
            // it should return "true" if it contains all, otherwise "false"
            Console.WriteLine(CheckNums(list));
            Console.ReadKey();
        }

        public static bool CheckNums(List<int> numberList)
        {
            var checkNumbers = new List<int> { 4, 8, 12, 16 };
            int containedNumber = 0;
            foreach (int checkNum in checkNumbers)
            {
                foreach (int  gotNum in numberList)
                {
                    if(checkNum == gotNum)
                    {
                        containedNumber++;
                    }
                }
                if(containedNumber == checkNumbers.Count)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
