using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CounterProject
{
    class Counter
    {
        int prop;

        public Counter(int num = 0)
        {
            this.prop = num;
        }

        public void Add(int number = 0)
        {
            if (number > 0)
            {
                this.prop += number;
            }
            else
            {
                this.prop++;
            }
        }

        public string Get()
        {
            return this.prop.ToString();
        }

        public void Reset()
        {
            this.prop = 0;
        }
    }
}
