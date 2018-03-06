using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CounterProject
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Create Counter class
                 which has an integer property
                 when creating it should have a default value 0 or we can specify it when creating
                 we can Add(number) to this counter another whole number
                 or we can Add() without parameters just increasing the counter's value by one
                 and we can Get() the current value as string
                 also we can Reset() the value to the initial value*/
            Counter counterA = new Counter();
            Counter counterB = new Counter(20);

            Console.WriteLine("First without number: {0}",counterA.Get());
            Console.WriteLine("Second with 20: {0}", counterB.Get());

            counterA.Add(30);
            counterB.Add();

            Console.WriteLine("First Add method with 30: {0}", counterA.Get());
            Console.WriteLine("Second without number: {0}", counterB.Get());

            Console.ReadKey();
        }
    }
}
