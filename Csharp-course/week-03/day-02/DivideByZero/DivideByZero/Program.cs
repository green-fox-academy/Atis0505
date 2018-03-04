using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DivideByZero
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a function that takes a number
            // divides ten with it,
            // and prints the result.
            // It should print "fail" if the parameter is 0
            int number = 2;
            int number02 = 0;
            Console.WriteLine("Divide by ten, and handling execption: {0}", DivideByTen(number));
            Console.WriteLine("Divide by ten, and handling execption: {0}", DivideByTen(number02));
            Console.ReadKey();
        }

        public static string DivideByTen(int num)
        {
            int result;
            try
            {
                result = 10 / num;
            }
            catch (Exception e)
            {

                return e.Message;
            }
            
            return result.ToString();
        }
    }
}
