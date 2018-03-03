using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace sortList
{
    class Program
    {
        static void Main(string[] args)
        {
            //  Create a function that takes a list of numbers as parameter
            //  Returns a list where the elements are sorted in ascending numerical order
            //  Make a second boolean parameter, if it's `True` sort that list descending

            //  Example:
            Console.WriteLine("{0}",string.Join(" ",Bubble(new int[] { 34, 12, 24, 9, 5 })));
            Console.WriteLine("{0}",string.Join(" ",Bubble(new int[] { 34, 12, 24, 9, 5 }, true)));
            //  should print [5, 9, 12, 24, 34]
            //Console.WriteLine(AdvancedBubble(new int[] { 34, 12, 24, 9, 5 }, true));
            //  should print [34, 24, 12, 9, 5]
            Console.ReadKey();
        }

        public static int[] Bubble(int[] numbers, bool desc = false)
        {
            if (desc)
            {
                for (int i = 0; i < numbers.Length; i++)
                {
                    for (int j = 0; j < numbers.Length; j++)
                    {
                        if(numbers[i] > numbers[j])
                        {
                            int temp = numbers[i];
                            numbers[i] = numbers[j];
                            numbers[j] = temp;
                        }
                    }
                }
            }else
            {
                for (int i = 0; i < numbers.Length; i++)
                {
                    for (int j = 0; j < numbers.Length; j++)
                    {
                        if (numbers[i] < numbers[j])
                        {
                            int temp = numbers[i];
                            numbers[i] = numbers[j];
                            numbers[j] = temp;
                        }
                    }
                }

            }
            return numbers;
        }
    }
}
