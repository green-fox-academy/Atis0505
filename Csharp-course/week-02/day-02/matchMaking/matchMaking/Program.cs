using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace matchMaking
{
    class Program
    {
        static void Main(string[] args)
        {
            var girls = new List<string> { "Eve", "Ashley", "Bözsi", "Kat", "Jane" };
            var boys = new List<string> { "Joe", "Fred", "Béla", "Todd", "Neef", "Jeff" };

            // Write a method that joins the two lists by matching one girl with one boy into a new list
            // Exepected output: "Eve", "Joe", "Ashley", "Fred"...

            Console.WriteLine(string.Join(" ",MakingMatches(girls, boys)));
            Console.ReadKey();
        }

        public static List<string> MakingMatches(List<string> girlList, List<string>boyList)
        {
            var matchesList = new List<string>();
            foreach (string boy in boyList)
            {
                matchesList.Add(boy);
            }
            for (int i = 0; i < girlList.Count; i++)
            {
                matchesList.Insert(i * 2, girlList[i]);
            }
            return matchesList;
        }
    }
}
