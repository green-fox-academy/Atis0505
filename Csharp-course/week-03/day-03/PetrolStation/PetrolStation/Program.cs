using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PetrolStation
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Create Station and Car classes
                 Station
                     GasAmount
                     Refill(car)->decreases the gasAmount by the capacity of the car and increases the cars gasAmount
                 Car
                     GasAmount
                     Capacity
                 create constructor for Car where:
                 initialize gasAmount-> 0
                 initialize capacity-> 100*/

            Station newStation = new Station();
            Car newCar = new Car();

            Console.WriteLine("Car details\nGasamount: {0}\nCapacity: {1}", newCar.GasAmount(), newCar.Capacity());
            Console.WriteLine("Station details\nGasamount: {0}", newStation.GetGasAmount());

            newStation.Refill(newCar);

            Console.WriteLine("Car details\nGasamount: {0}\nCapacity: {1}", newCar.GasAmount(), newCar.Capacity());
            Console.WriteLine("Station details\nGasamount: {0}", newStation.GetGasAmount());

            Console.ReadKey();
        }
    }
}
