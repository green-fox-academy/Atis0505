using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WriteSingleLine
{
    class Program
    {
        static void Main(string[] args)
        {
            // Open a file called "my-file.txt"
            // Write your name in it as a single line
            // If the program is unable to write the file,
            // then it should print an error message like: "Unable to write file: my-file.txt"
            string filePath = @"../../toWrite.txt";
            string greeting = "Hello everyone! :)";
            WriteToFile(filePath, greeting);
            ReadFromFile(filePath);
            Console.ReadKey();
        }

        public static void WriteToFile(string filePath, string text)
        {
            try
            {
                using (System.IO.StreamWriter writer = new System.IO.StreamWriter(filePath))
                {
                    writer.WriteLine(text);
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Unable to write file: toWrite.txt");
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
                Console.WriteLine("Unable to read file: toWrite.txt");
            }
           
        }
    }
}
