using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace color
{
    class Program
    {
        static void Main(string[] args)
        {
            // - Create a two dimensional array
            //   which can contain the different shades of specified colors
            // - In `colors[0]` store the shades of green:
            //   `"lime", "forest green", "olive", "pale green", "spring green"`
            // - In `colors[1]` store the shades of red:
            //   `"orange red", "red", "tomato"`
            // - In `colors[2]` store the shades of pink:
            //   `"orchid", "violet", "pink", "hot pink"`
            string[][] colors = new String[][]
            {
                new string[] {"lime", "forest green", "olive", "pale green", "spring green"},
                new string[] {"orange red", "red", "tomato"},
                new string[] { "orchid", "violet", "pink", "hot pink" }
            };

            for (int x = 0; x < colors.Length; x++)
            {
                for (int y = 0; y < colors[x].Length; y++)
                {
                    Console.Write(colors[x][y]+ " ");
                }
                Console.WriteLine();
            }

            Console.ReadLine();
        }
    }
}
