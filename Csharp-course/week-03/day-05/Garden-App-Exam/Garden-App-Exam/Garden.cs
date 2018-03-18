using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Garden_App_Exam
{
    class Garden
    {
        public List<Plant> ListOfPlants = new List<Plant>();

        public Garden()
        {
            this.ListOfPlants.Clear();
        }

        public void Watering(double waterAmount)
        {
            double eachWaterAmount = waterAmount / ListOfPlants.Count;
            foreach (Plant actualPlant in ListOfPlants)
            {
                if (actualPlant.waterinfTreshold > actualPlant.currentWaterAmount)
                {
                    actualPlant.Watering(eachWaterAmount);
                }
            }
            Console.WriteLine("Watering with {0}", waterAmount);
        }

        public void GetGardenInfo()
        {
            foreach (Plant actualPlant in ListOfPlants)
            {
                if (actualPlant.currentWaterAmount >= actualPlant.waterinfTreshold)
                {
                    Console.WriteLine("The {0} {1} doesn't need water", actualPlant.color, actualPlant.type);
                }
                else
                {
                    Console.WriteLine("The {0} {1} need water", actualPlant.color, actualPlant.type);
                }
            }
        }
    }
}
