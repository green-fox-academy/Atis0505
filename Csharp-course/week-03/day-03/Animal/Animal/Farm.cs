using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Animal
{
    class Farm
    {
        List<Anim> animalList;
        int freePlace;

        public Farm(int freeP)
        {
            this.freePlace = freeP;
            this.animalList = new List<Anim>();
        }

        public void Breed()
        {
            if(this.animalList.Count < this.freePlace)
            {
                this.animalList.Add(new Anim());
            }
        }
        
        public void Slaughter()
        {
            int min = this.animalList.Min<Anim>(anim => anim.GetHungryPoint());
            Console.WriteLine("Min: {0}", min);
            for (int i = 0; i < this.animalList.Count; i++)
            {
                if (this.animalList[i].GetHungryPoint() <= min)
                {
                    this.animalList.RemoveAt(i);
                }
            }
        }

        public List<Anim> GetAnimals()
        {
            return this.animalList;
        }
    }
}
