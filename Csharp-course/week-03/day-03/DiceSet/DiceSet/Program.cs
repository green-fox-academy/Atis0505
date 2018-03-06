using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DiceSet
{
    class Program
    {
        public static void Main(string[] args)
        {
            // You have a `DiceSet` class which has a list for 6 dices
            // You can roll all of them with roll()
            // Check the current rolled numbers with getCurrent()
            // You can reroll with reroll()
            // Your task is to roll the dices until all of the dices are 6
            var RandomValue = new Random();
            Dice myDice = new Dice();
            myDice.Roll();
            for (int i = 0; i < 6; i++)
            {
                while(myDice.GetCurrent()[i] != 6)
                {
                    myDice.Reroll(i);
                }
            }

            foreach (int item in myDice.GetCurrent())
            {
                Console.WriteLine(item);
            }
            /*.WriteLine(myDice.GetCurrent());
            Console.WriteLine(myDice.GetCurrent(5));
            myDice.Reroll();
            Console.WriteLine(myDice.GetCurrent());
            myDice.Reroll(4);
            myDice.GetCurrent();*/

            Console.ReadKey();
        }
    }
}
