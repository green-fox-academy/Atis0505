using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PostIt
{
    class Program
    {
        /// <summary>
        /// 
        /// </summary>
        /// <param name="args"></param>
        static void Main(string[] args)
        {
            /*Create a PostIt a struct that has
            a BackgroundColor
            a Text on it
            a TextColor
            Create a few example post-it objects:
            an orange with blue text: "Idea 1"
            a pink with black text: "Awesome"
            a yellow with green text: "Superb!"*/

            PostIt first = new PostIt();
            first.BackgroundColor = "orange";
            first.Text = "Idea 1";
            first.TextColor = "blue";

            PostIt second = new PostIt();
            second.BackgroundColor = "pink";
            second.Text = "Awesome";
            second.TextColor = "black";

            PostIt third = new PostIt();
            third.BackgroundColor = "yellow";
            third.Text = "Superb!";
            third.TextColor = "green";

            List<PostIt> postItList = new List<PostIt>();
            postItList.Add(first);
            postItList.Add(second);
            postItList.Add(third);

            foreach (PostIt postit in postItList)
            {
                Console.WriteLine("BackgroundColor: {0}",postit.BackgroundColor);
                Console.WriteLine("Text: {0}",postit.Text);
                Console.WriteLine("TextColor: {0}",postit.TextColor);
                Console.WriteLine();
            }

            Console.ReadKey();
        }

        public struct PostIt
        {
            public string BackgroundColor;
            public string Text;
            public string TextColor;
        }
    }
}
