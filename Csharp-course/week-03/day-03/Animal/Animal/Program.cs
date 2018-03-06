using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Animal
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Create an Animal class
                 Every animal has a hunger value, which is a whole number
                 Every animal has a thirst value, which is a whole number
                 when creating a new animal object these values are created with the default 50 value
                 Every animal can eat() which decreases their hunger by one
                 Every animal can drink() which decreases their thirst by one
                 Every animal can play() which increases both by one*/

            /*Reuse your Animal class  ---- 2. exercise
                Create a Farm class
                it has list of Animals
                it has slots which defines the number of free places for animals
                breed() -> creates a new animal if there's place for it
                slaughter() -> removes the least hungry animal*/

            var dog = new Anim();
            for (int i = 0; i < 10; i++)
            {
                dog.Play();
            }
            dog.GetValues();

            var cat = new Anim();
            for (int i = 0; i < 4; i++)
            {
                cat.Eat();
            }
            cat.GetValues();

            Console.WriteLine("New farm animals:");
            Farm newFarm = new Farm(5);
            for (int i = 0; i < 10; i++)
            {
                newFarm.Breed();
            }

            for (int i = 0; i < newFarm.GetAnimals().Count; i++)
            {
                newFarm.GetAnimals()[i].GetValues();
            }
            Console.WriteLine();

            Console.WriteLine("After slaughter method:");

            newFarm.Slaughter();

            for (int i = 0; i < newFarm.GetAnimals().Count; i++)
            {
                newFarm.GetAnimals()[i].GetValues();
            }

            Console.ReadKey();
        }
    }
}
