using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WriteMutipleLines
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a function that takes 3 parameters: a path, a word and a number,
            // than it should write to a file.
            // The path parameter should be a string, that describes the location of the file.
            // The word parameter should be a string, that will be written to the file as lines
            // The number paramter should describe how many lines the file should have.
            string filePath = @"../../multipleLines.txt";
            string word = "Hello World!!!";
            int number = 10;
            // So if the word is "apple" and the number is 5, than it should write 5 lines
            // to the file and each line should be "apple"
            // The function should not raise any error if it could not write the file.
            WriteToFile(filePath, word, number);
            ReadFromFile(filePath);
            Console.ReadKey();
        }

        public static void WriteToFile(string filePath, string text, int freq)
        {
            try
            {
                using (System.IO.StreamWriter writer = new System.IO.StreamWriter(filePath))
                {
                    for (int i = 0; i < freq; i++)
                    {
                        writer.WriteLine(text);
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Unable to write file: multipleLines.txt");
            }

        }

        public static void ReadFromFile(string path)
        {
            try
            {
                using (System.IO.StreamReader reader = new System.IO.StreamReader(path))
                {
                    string line;
                    while ((line = reader.ReadLine()) != null)
                    {
                        Console.WriteLine(line);
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Unable to read file: multipleLines.txt");
            }

        }
    }
}
