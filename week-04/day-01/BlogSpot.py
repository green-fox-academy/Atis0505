class Blog_Post(object):
    author_name = ""
    title = ""
    text = ""
    publicatione_date = ""


Blog_Post01 = Blog_Post()
Blog_Post02 = Blog_Post()
Blog_Post03 = Blog_Post()

Blog_Post01.author_name = "John Doe"
Blog_Post01.title = "Lorem ipsum"
Blog_Post01.publicatione_date = "2000.05.04"
Blog_Post01.text = "Lorem ipsum dolor sit amet."

Blog_Post02.author_name = "TimUrban"
Blog_Post02.title = "Wait but why"
Blog_Post02.publicatione_date = "2010.10.10"
Blog_Post02.text = "A popular long-form, stick-figure-illustrated blog about almost everything."

Blog_Post03.author_name = "William Turton"
Blog_Post03.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
Blog_Post03.publicatione_date = "2017.03.28."
Blog_Post03.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."

print(Blog_Post01.author_name)
print(Blog_Post02.title)
print(Blog_Post03.text)