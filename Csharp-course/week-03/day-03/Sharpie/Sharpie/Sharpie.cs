﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sharpie
{
    class Sharpie
    {
        string color;
        float width;
        float inkAmount;

        public Sharpie(string color, float width)
        {
            this.color = color;
            this.width = width;
            inkAmount = 100;
        }

        public void Use()
        {
            inkAmount--;
        }

        public void GetStatus()
        {
            Console.WriteLine("Color: {0}\nWidth: {1}\nInkAmount: {2}",this.color, this.width,this.inkAmount);
        }
    }
}
