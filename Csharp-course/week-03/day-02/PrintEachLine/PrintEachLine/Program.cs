using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PrintEachLine
{
    class Program
    {
        static void Main(string[] args)
        {
            // Write a program that opens a file called "my-file.txt", then prints
            // each of lines form the file.
            // If the program is unable to read the file (for example it does not exists),
            // then it should print an error message like: "Unable to read file: my-file.txt"
            string txtPath = @"../../example_file.txt";
            string line;
            try
            {
                using(System.IO.StreamReader file = new System.IO.StreamReader(txtPath))
                {
                    while ((line = file.ReadLine()) != null)
                    {
                        Console.WriteLine(line);
                    }
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
            Console.ReadKey();
        }
    }
}
