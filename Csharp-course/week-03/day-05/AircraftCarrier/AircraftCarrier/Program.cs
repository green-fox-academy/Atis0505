using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AircraftCarrier
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("First carrier");
            Carrier carrier01 = new Carrier(2500, 2200);
            carrier01.Add(new Aircraft("F35"));
            carrier01.Add(new Aircraft("F16"));
            carrier01.Add(new Aircraft("F35"));
            carrier01.Add(new Aircraft("F35"));
            carrier01.Add(new Aircraft("F16"));
            carrier01.Add(new Aircraft("F35"));
            carrier01.Add(new Aircraft("F16"));
            carrier01.fill(1500);
            carrier01.getStatus();
            Console.WriteLine();
            Console.WriteLine("Second carrier");
            Carrier carrier02 = new Carrier(1200, 600);
            carrier02.Add(new Aircraft("F35"));
            carrier02.Add(new Aircraft("F16"));
            carrier02.Add(new Aircraft("F35"));
            carrier02.Add(new Aircraft("F35"));
            carrier02.Add(new Aircraft("F16"));
            carrier02.fill(100);
            carrier02.getStatus();
            Console.WriteLine();
            Console.WriteLine("After attack!");
            carrier02.Fight(carrier01);
            Console.WriteLine("First carrier");
            carrier01.getStatus();
            Console.WriteLine();
            Console.WriteLine("Second carrier");
            carrier02.getStatus();

            Console.ReadKey();
        }
    }
}
