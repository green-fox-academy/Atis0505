using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CopyFile
{
    class Program
    {
        static void Main(string[] args)
        {
            string fromPath = @"../../FromFile.txt";
            string toPath = @"../../ToFile.txt";
            string word = "Hello World!!!";
            int number = 20;

            WriteToFile(fromPath, word, number);

            CopyFile(fromPath, toPath);

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
                        writer.WriteLine(text+(i+1));
                    }
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Unable to write file: multipleLines.txt");
            }

        }

        public static void CopyFile(string fromPath, string toPath)
        {
            try
            {
                using (System.IO.StreamReader reader = new System.IO.StreamReader(fromPath))
                {
                    using (System.IO.StreamWriter writer = new System.IO.StreamWriter(toPath))
                    {
                        string line;
                        while ((line = reader.ReadLine()) != null)
                        {
                            Console.WriteLine(line);
                            writer.WriteLine(line);
                        }
                    }        
                }
            }
            catch (Exception)
            {
                Console.WriteLine("Unable to copy files!");
            }

        }
    }
}
