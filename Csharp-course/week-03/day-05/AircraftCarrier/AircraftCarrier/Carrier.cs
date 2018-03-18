using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AircraftCarrier
{
    class Carrier
    {
        protected List<Aircraft> listOfAircraft = new List<Aircraft>();
        protected int storeOfAmmo;
        protected int healthPoint;

        public Carrier(int ammo, int health)
        {
            this.listOfAircraft.Clear();
            this.storeOfAmmo = ammo;
            this.healthPoint = health;
        }

        public void Add(Aircraft newAircraft)
        {
            this.listOfAircraft.Add(newAircraft);
        }

        public void fill(int ammo)
        {
            if (ammo <= this.storeOfAmmo)
            {
                foreach (Aircraft actualAircraft in this.listOfAircraft)
                {
                    if (actualAircraft.isPriority() && actualAircraft.currentAmmo < actualAircraft.maxAmmo)
                    {
                        this.storeOfAmmo -= actualAircraft.Refill(ammo);
                        ammo -= actualAircraft.Refill(ammo);
                    }
                }
                foreach (Aircraft actualAircraft in this.listOfAircraft)
                {
                    if (actualAircraft.isPriority() == false && actualAircraft.currentAmmo < actualAircraft.maxAmmo)
                    {
                        this.storeOfAmmo -= actualAircraft.Refill(ammo);
                        ammo -= actualAircraft.Refill(ammo);
                    }
                }
            }
        }

        public void Fight(Carrier enemyCarrier)
        {
            enemyCarrier.healthPoint -= this.MaxDamage();
            foreach (Aircraft actualAircraft in this.listOfAircraft)
            {
                actualAircraft.currentAmmo = 0;
            }
            if (enemyCarrier.healthPoint <= 0)
            {
                enemyCarrier.healthPoint = 0;
                Console.WriteLine("It's dead Jim :(");
            }
        }

        public int MaxDamage()
        {
            int maxDamage = 0;
            foreach (Aircraft actualAircraft in this.listOfAircraft)
            {
                maxDamage += actualAircraft.baseDamage * actualAircraft.currentAmmo;
            }
            return maxDamage;
        }

        public void getStatus()
        {
            Console.WriteLine("HP: " + this.healthPoint + ", Aircraft count: "+this.listOfAircraft.Count+
                ", Ammo Storage: "+this.storeOfAmmo+", Total Damage: "+ this.MaxDamage());
            Console.WriteLine("Aircrafts:");
            foreach (Aircraft actualAircraft in this.listOfAircraft)
            {
                Console.WriteLine("Type: {0}, Ammo: {1}, Base Damage: {2}, All Damage: {3}",actualAircraft.getType(), actualAircraft.currentAmmo, actualAircraft.baseDamage, actualAircraft.baseDamage * actualAircraft.currentAmmo);
            }
        }
    }
}
