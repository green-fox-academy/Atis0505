using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Garden_App_Exam
{
    class Program
    {
        static void Main(string[] args)
        {
            Garden myGarden = new Garden();
            Plant flower1 = new Flower("yellow");
            Plant flower2 = new Flower("blue");
            Plant tree1 = new Tree("purple");
            Plant tree2 = new Tree("orange");

            myGarden.ListOfPlants.Add(flower1);
            myGarden.ListOfPlants.Add(flower2);
            myGarden.ListOfPlants.Add(tree1);
            myGarden.ListOfPlants.Add(tree2);
            myGarden.GetGardenInfo();
            myGarden.Watering(40);
            myGarden.GetGardenInfo();
            myGarden.Watering(70);
            myGarden.GetGardenInfo();
            Console.ReadLine();
        }
    }
}
