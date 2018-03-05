using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BlogPost
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            Create a BlogPost class that has an AuthorName, a Title, a Text, a PublicationDate
            Create a few blog post objects:
            "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
            Lorem ipsum dolor sit amet.
            "Wait but why" titled by Tim Urban posted at "2010.10.10."
            A popular long-form, stick-figure-illustrated blog about almost everything.
            "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
            Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention.
            When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really
            into the whole organizer profile thing.*/
            BlogPost post01 = new BlogPost("John Doe", "Lorem Ipsum", "Lorem ipsum dolor sit amet.", "2000.05.04.");
            BlogPost post02 = new BlogPost("Tim Urban", "Wait but why", "A popular long-form, stick-figure-illustrated blog about almost everything.", "2010.10.10.");
            BlogPost post03 = new BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon With Trump", "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention."+
            "When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really"+
            "into the whole organizer profile thing.", "2017.03.28.");

            List<BlogPost> postList = new List<BlogPost>();
            postList.Add(post01);
            postList.Add(post02);
            postList.Add(post03);

            foreach (BlogPost post in postList)
            {
                Console.WriteLine("\"" +post.Title+"\" titled by "+post.Authorname+" posted at "+post.PublishedDate+"\n"+post.Text);
                Console.WriteLine();
            }

            Console.Read();
        }
    }
}
