using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CountLines
{
    class Program
    {
        static void Main(string[] args)
        {
            // Write a function that takes a filename as string,
            // then returns the number of lines the file contains.
            // It should return zero if it can't open the file, and
            // should not raise any error.
            string txtPath = @"../../textFile.txt";
            Console.WriteLine("Counted lines number: {0}", CountLines(txtPath));
            Console.ReadKey();
        }

        public static int CountLines(string filePath)
        {
            int counter = 0;
            try
            {
                using (System.IO.StreamReader file = new System.IO.StreamReader(filePath))
                {
                    while (file.ReadLine() != null)
                    {
                        counter++;
                    }
                    return counter;
                }
            }
            catch (Exception)
            {
                return counter;
            }
        }
    }
}
