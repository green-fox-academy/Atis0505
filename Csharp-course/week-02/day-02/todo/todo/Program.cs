using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace todo
{
    class Program
    {
        static void Main(string[] args)
        {
            string todoText = " - Buy milk\n";
            // Add "My todo:" to the beginning of the todoText
            // Add " - Download games" to the end of the todoText
            // Add " - Diablo" to the end of the todoText but with indentation
            StringBuilder newString = new StringBuilder();
            newString.Append("My todo:\n");
            newString.Append(todoText);
            newString.Append(" - Donwload games\n   - Diabol");
            // Expected output:
            
            // My todo:
            //  - Buy milk
            //  - Download games
            //      - Diablo

            Console.WriteLine(newString);
            Console.ReadKey();
        }
    }
}
