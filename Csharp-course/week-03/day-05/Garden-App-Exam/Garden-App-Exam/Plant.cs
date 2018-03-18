using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Garden_App_Exam
{
    class Plant
    {
        public string color;
        public string type;
        public double currentWaterAmount;
        public double waterinfTreshold;
        public double waterPull;

        public void Watering(double amount)
        {
            this.currentWaterAmount += amount * this.waterPull;
        }
    }
}
