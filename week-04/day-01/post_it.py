class post_it(object):
    background_color = ""
    text = ""
    color_text = ""

Post_it01 = post_it()
Post_it02 = post_it()
Post_it03 = post_it()

Post_it01.background_color = "orange"
Post_it01.text = "Idea 1"
Post_it01.color_text = "blue"

Post_it02.background_color = "pink"
Post_it02.text = "Awesome"
Post_it02.color_text = "black"

Post_it03.background_color = "yellow"
Post_it03.text = "Superb"
Post_it03.color_text = "green"

print(Post_it02.color_text)
print(Post_it03.background_color)
print(Post_it01.text)