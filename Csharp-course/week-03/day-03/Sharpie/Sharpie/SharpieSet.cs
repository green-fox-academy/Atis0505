using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sharpie
{
    class SharpieSet
    {
        List<Sharpie> sharpieList;
        public SharpieSet()
        {
            this.sharpieList = new List<Sharpie>();
        }

        public void Add(Sharpie sharpie)
        {
            this.sharpieList.Add(sharpie);
        }

        public List<Sharpie> GetList()
        {
            return this.sharpieList;
        }

        public int CountUsable()
        {
            int counter = 0;
            foreach (Sharpie item in this.sharpieList)
            {
                if (item.GetInk() > 0)
                {
                    counter++;
                }
            }
            return counter;
        }

        public void RemoveTrash()
        {
            for (int i = 0; i < this.sharpieList.Count; i++)
            {
                if (this.sharpieList[i].GetInk() == 0)
                {
                    this.sharpieList.RemoveAt(i);
                }
            }
        }
    }
}
