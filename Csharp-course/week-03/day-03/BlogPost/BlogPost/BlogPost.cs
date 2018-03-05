using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BlogPost
{
    class BlogPost
    {
        string authorName;
        string title;
        string text;
        string publishDate;
        public BlogPost(string authName, string title, string text, string pubDate)
        {
            this.authorName = authName;
            this.title = title;
            this.text = text;
            this.publishDate = pubDate;
        }

        public string Authorname { get { return this.authorName; } }
        public string Title { get { return this.title; } }
        public string Text { get { return this.text; } }
        public string PublishedDate { get { return this.publishDate; } }
    }
}
