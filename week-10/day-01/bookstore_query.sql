drop database bookstore;

create database bookstore;

use bookstore;

create table Authors (
	author_code int auto_increment,
	author_name nvarchar(30),
    age int,
    book_number int,
    primary key(author_code)
);

create table Bookstore (
	book_id int auto_increment,
    title nvarchar(50),
    page_number int,
    released_year int,
    sold_quantity int,
	primary key(book_id),
    auth_id int, 
    foreign key (auth_id) references Authors(author_code)
);

insert into Authors(author_name, age, book_number) values ('Mark Twain', 78, 20);
insert into Authors(author_name, age, book_number) values ('Jane Austen', 45, 11);
insert into Authors(author_name, age, book_number) values ('T.S. Eliot', 56, 33);
insert into Authors(author_name, age, book_number) values ('Charles Dickens', 82, 56);
insert into Authors(author_name, age, book_number) values ('J.K. Rowling', 35, 19);
insert into Authors(author_name, age, book_number) values ('Stephen King', 69, 76);
insert into Authors(author_name, age, book_number) values ('Leo Tolstoy', 89, 67);
insert into Authors(author_name, age, book_number) values ('Ernest Hemingway', 62, 41);
insert into Authors(author_name, age, book_number) values ('Ray Bradbury', 92, 45);
insert into Authors(author_name, age, book_number) values ('J.J. Tolkien', 81, 82);
insert into Authors(author_name, age, book_number) values ('Franz Kafka', 41, 37);
insert into Authors(author_name, age, book_number) values ('William Shakespeare', 52, 13);

insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Adventures of Huckleberry', 456, 1883, 1543, 1);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('The Innocents Aboard', 234, 1869, 112220,1);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Life on the Mississippi', 785, 1883, 262248, 1);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Pride and Prejudice', 648, 1813, 745290, 2);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Emma', 853, 1815, 429933, 2);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Persuasion', 1234, 1817, 739223, 2);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Gerontion', 281, 1920, 739237,3);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('The Sacred Wood', 478, 1920, 763292, 3);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Great Expectations', 632, 1861, 7232982, 4);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Oliver Twist', 526, 1838, 6728271, 4);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Hard Times', 625, 1854, 267389, 4);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Harry Potter - I', 426, 1997, 67287, 5);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Harry Potter - II', 452, 2000, 6738398, 5);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Harry Potter - Chamber of Secrets', 526, 1998, 673872,5);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('The Shinning', 536, 1977, 6232445, 6);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('IT', 647, 1986, 8723987, 6);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Carrie', 673, 1974, 6723287, 6);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Misery', 435, 1987, 2339838, 6);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('War and Peace', 643, 1867, 38378, 7);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Anna Karenina', 234, 1877, 637394, 7);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('The old man and the sea', 123, 1952, 646473, 8);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('The Sun also Rises', 234, 1926, 87238, 8);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Fahrenheit 451', 261, 1953, 53728, 9);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Brad bury Stories', 526, 2003, 872879, 9);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Lord of Rings', 789, 1954, 8762898, 10);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('The Hobbit', 652, 1937, 8762998, 10);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('The Metamorphosis', 345, 1915, 253879, 11);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('The trial', 459, 1925, 7187378, 11);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Hamlet', 345, 1603, 23234, 12);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Machbet', 456, 1623, 23423, 12);
insert into Bookstore( title, page_number, released_year, sold_quantity, auth_id) values ('Romeo and Juliet', 765, 1597, 34353, 12);

Select * from bookstore b inner join authors s on b.auth_id = s.author_code
order by b.title;
