using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sharpie
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Create Sharpie class
                 We should know about each sharpie their Color(which should be a string), 
                 Width(which will be a floating point number), InkAmount(another floating point number)
                 When creating one, we need to specify the Color and the Width
                 Every sharpie is created with a default 100 as InkAmount
                 We can Use() the sharpie objects
                 which decreases inkAmount*/


           /* Reuse your Sharpie class ---------  2.exercise 
                Create SharpieSet class
                it contains a list of Sharpie
                Add method CountUsable() -> sharpie is usable if it has ink in it
                Add method RemoveTrash() -> removes all unusable sharpies*/

            Sharpie first = new Sharpie("red", 1.4f);
            for (int i = 0; i < 3; i++)
            {
                first.Use();
                first.GetStatus();
            }

            SharpieSet newList = new SharpieSet();
            newList.Add(new Sharpie("red", 1.2f));
            newList.Add(new Sharpie("green", 1.2f));
            newList.Add(new Sharpie("yellow", 1.2f));
            newList.Add(new Sharpie("black", 1.2f));
            newList.Add(new Sharpie("blue", 1.2f));
            newList.Add(new Sharpie("pink", 1.2f));

            foreach (Sharpie item in newList.GetList())
            {
                item.GetStatus();
            }

            for (int i = 0; i < 100; i++)
            {
                newList.GetList()[1].Use();
                newList.GetList()[3].Use();
                newList.GetList()[5].Use();
            }

            foreach (Sharpie item in newList.GetList())
            {
                item.GetStatus();
            }

            Console.WriteLine("Usable number: {0}",newList.CountUsable());
            newList.RemoveTrash();

            foreach (Sharpie item in newList.GetList())
            {
                item.GetStatus();
            }

            Console.ReadKey();
        }
    }
}
