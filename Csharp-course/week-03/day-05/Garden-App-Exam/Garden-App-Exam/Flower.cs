using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Garden_App_Exam
{
    class Flower : Plant
    {
        public Flower(string _color)
        {
            this.type = "Flower";
            this.currentWaterAmount = 0;
            this.waterinfTreshold = 5;
            this.waterPull = 0.75;
            this.color = _color;
        }
    }
}
