using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Garden_App_Exam
{
    class Tree : Plant
    {
        public Tree(string _color)
        {
            this.type = "Tree";
            this.currentWaterAmount = 0;
            this.waterinfTreshold = 10;
            this.waterPull = 0.4;
            this.color = _color;
        }
    }
}
