# Create a Book class, that has an author, a title and a release year
# Create a constructor for setting those values
# Book should be represented as string in this format:
# Douglas Adams : The Hitchhiker's Guide to the Galaxy (1979)
# Create a BookShelf class that has a list of books in it
# We should be able to add and remove books.
# We should be able to query the favourite author (who has written the most books in the shelf)
# We should be able to query the earliest published books.
# We should be able to query the latest published books.
# Bookself should have a method whitch give us information about the number of books, the earliest and the latest released books, and the favourite author 

class Book:
    def __init__(self, author, title, release_year):
        self.author = author
        self.title = title
        self.release_year = release_year

    
    def get_info(self):
        return self.author + " : " + self.title + " (" + str(self.release_year) + ")"


class BookShelf:
    def __init__(self):
        self.list_of_books = []


    def put(self, book_author, book_title, book_release_year):
        self.list_of_books.append(Book(book_author, book_title, book_release_year))
    

    def remove(self, book_title):
        for index, book in enumerate(self.list_of_books):
            if book.title == book_title:
                del self.list_of_books[index]


    def favourite_author(self):
        author_dict = {}
        for book in self.list_of_books:
            if book.author in author_dict:
                author_dict[book.author] += 1
            else:
                author_dict[book.author] = 1
        max_number = max(author_dict.values())
        favourite_author = [author for author, number in author_dict.items() if number == max_number]
        favourite_author_string = favourite_author[0]
        return favourite_author_string


    def earliest_published_book(self):
        book_year_dict = {}
        for book in self.list_of_books:
            book_year_dict[book.title] = book.release_year
        min_release_year = min(book_year_dict.values())
        earliest_published_book_title = [title for title, year in book_year_dict.items() if year == min_release_year]
        for book in self.list_of_books:
            if book.title == earliest_published_book_title[0]:
                return book.get_info()


    
    def latest_published_book(self):
        book_year_dict = {}
        for book in self.list_of_books:
            book_year_dict[book.title] = book.release_year
        max_released_year = max(book_year_dict.values())
        latest_published_book_title = [title for title, year in book_year_dict.items() if year == max_released_year]
        for book in self.list_of_books:
            if book.title == latest_published_book_title[0]:
                return book.get_info()
    
    
    def books(self):
        if len(self.list_of_books) == 0:
            print("You have no books here.")
        else:
            status = "You have " + str(len(self.list_of_books)) + " books.\n"
            for book in self.list_of_books:
                status += book.get_info() + "\n"
            status += "Earliest released: "+ str(self.earliest_published_book()) + "\n"
            status += "Latest released: "+ str(self.latest_published_book()) + "\n"
            status += "Favourite author: " + self.favourite_author() + "\n"
            return status


my_shelf = BookShelf()
print(my_shelf.books())
# Should print out:
# You have no books here.
    
my_shelf.put("Douglas Adams", "The Hitchhiker's Guide to the Galaxy", 1979)
my_shelf.put("Douglas Adams", "Mostly Harmless", 1992)
my_shelf.put("Frank Herbert", "Dune", 1965)
my_shelf.put("Frank Herbert", "The Dragon in the Sea", 1957)
my_shelf.remove("The Dragon in the Sea")
print(my_shelf.latest_published_book())

print(my_shelf.books())
# Should print out:
# You have 3 books.
# Earliest released: Frank Herbert : Dune (1965)
# Latest released: Douglas Adams : Mostly Harmless (1992)
# Favourite author: Douglas Adams