using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dominoes
{
    class Program
    {
        static void Main(string[] args)
        {
            var dominoes = InitializeDominoes();
            /* Dominoes
             You have the list of Dominoes
             Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
             eg: [2, 4], [4, 3], [3, 5] ...*/
            OrderList(dominoes);
            

            foreach (Domino item in dominoes)
            {
                Console.WriteLine("Oirigin Domino: [{0}], [{1}]", item.GetValues().GetValue(0),item.GetValues().GetValue(1));
            }
            Console.ReadKey();
        }

        public static List<Domino> InitializeDominoes()
        {
            var dominoes = new List<Domino>();
            dominoes.Add(new Domino(5, 2));
            dominoes.Add(new Domino(4, 6));
            dominoes.Add(new Domino(1, 5));
            dominoes.Add(new Domino(6, 7));
            dominoes.Add(new Domino(2, 4));
            dominoes.Add(new Domino(7, 1));
            return dominoes;
        }

        public static void OrderList(List<Domino> inputList)
        {
            var newList = new List<Domino>();
            newList.Add(inputList[0]);
            Console.WriteLine("Domino: {0}, {1}", inputList[0].GetValues()[0], inputList[0].GetValues()[1]);

            for (int i = 0; i < newList.Count; i++)
            {
                foreach (Domino item in inputList)
                {
                    if (newList[newList.Count-1].GetValues()[1] == item.GetValues()[0] && newList.Count <= inputList.Count)
                    {
                        newList.Add(item);
                        Console.WriteLine("Domino: {0}, {1}",item.GetValues()[0], item.GetValues()[1]);
                    }
                }
            }

        }
    }
}
