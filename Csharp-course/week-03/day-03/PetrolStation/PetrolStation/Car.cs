using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PetrolStation
{
    class Car
    {
        int gasAmount;
        int capacity;

        public Car()
        {
            this.gasAmount = 0;
            this.capacity = 100;
        }

        public int GasAmount()
        {
            return this.gasAmount;
        }

        public int Capacity()
        {
            return this.capacity;
        }

        public void SetAmount(int value)
        {
            this.gasAmount = value;
        }
    }
}
