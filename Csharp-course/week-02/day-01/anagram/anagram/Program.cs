using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace anagram
{
    class Program
    {
        static void Main(string[] args)
        {
            //Find anagrams f.e.: 'dog' -> 'god' true
            //                    'green'->'fox' false
            string word01 = "dog";
            string word02 = "god";
            string word03 = "jesus";

            Console.WriteLine("Dog and god: {0}", isAnagram(word01,word02));
            Console.WriteLine("God and jesus: {0}", isAnagram(word02,word03));

            Console.ReadKey();
        }

        public static bool isAnagram(string w01, string w02)
        {
            if(w01.Length == w02.Length)
            {
                char[] w01Letters = w01.ToCharArray();
                char[] w02Letters = w02.ToCharArray();
                
                Array.Sort(w01Letters);
                Array.Sort(w02Letters);

                foreach (char letter in w01Letters)
                {
                    foreach (char item in w02Letters)
                    {
                        if(letter != item)
                        {
                            return false;
                        }else
                        {
                            return true;
                        }
                    }
                }

            }
            else
            {
                return false;
            }
            return false;
        }
    }
}
