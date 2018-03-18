using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AircraftCarrier
{
    class Aircraft
    {
        public int maxAmmo;
        public int baseDamage;
        public int currentAmmo;
        public string type;

        public Aircraft(string _type)
        {
            this.type = _type;
            this.currentAmmo = 0;
            if (_type == "F16")
            {
                this.maxAmmo = 8;
                this.baseDamage = 30;
            }
            else if (_type == "F35")
            {
                this.maxAmmo = 12;
                this.baseDamage = 50;
            }
        }

        public int Fight()
        {
            return this.currentAmmo * this.baseDamage;
        }

        public int Refill(int givenAmmo)
        {
            if (this.maxAmmo > this.currentAmmo)
            {
                int usedAmmo = (this.maxAmmo - this.currentAmmo);
                this.currentAmmo += usedAmmo;
                return usedAmmo;
            }
            return 0;
        }

        public string getType()
        {
            return this.type;
        }

        public bool isPriority()
        {
            if (this.type == "F35")
            {
                return true;
            }
            return false;
        }
    }
}
