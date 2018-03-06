using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PetrolStation
{
    class Station
    {
        int gasAmount;

        public Station()
        {
            this.gasAmount = 120000;
        }

        public void Refill(Car car)
        {
            int value = (car.Capacity() - car.GasAmount());
            this.gasAmount -= value;
            car.SetAmount(value);
        }

        public int GetGasAmount()
        {
            return this.gasAmount;
        }
    }
}
