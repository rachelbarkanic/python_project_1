my_book = {
    "title": "East of Eden",
    "author": "John Steinbeck",
    "year": 1952,
    "rating": 4.4,
    "pages": 612
}

library = [ {
    "title": "East of Eden",
    "author": "John Steinbeck",
    "year": 1952,
    "rating": 4.4,
    "pages": 612
},

{
    "title": "Before We Were Yours",
    "author": "Lisa Wingate",
    "year": 2017,
    "rating": 4.4,
    "pages": 354
},

{
    "title": "The Nightingale",
    "author": "Kristin Hannah",
    "year": 2015,
    "rating": 4.6,
    "pages": 502
} ]

# Follow the instructions in this part of the project. 
# Define and flesh out your function below, 
# which should accept a dictionary as an argument when called, 
# and return a string of the info in that book-dictionary in a user-friendly readable format.

def book_parser(dict):
    book_str = f"The book {dict['title']} by {dict['author']} was written in {dict['year']}, has a rating of {dict['rating']}, and is {dict['pages']} pages long."
    return book_str

my_result = book_parser(my_book)
print(my_result)




# Once you are finished with that function, 
# create several more functions which return individual pieces of information from the book.
def title_funct(dict):
    title_str = dict['title']
    return title_str


def author_funct(dict):
    author_str = dict['author']
    return author_str

    
def year_funct(dict):
    year_str = dict['year']
    return year_str
  

def rating_funct(dict):
    rating_str = dict['rating']
    return rating_str
  

def pages_funct(dict):
    pages_str = dict['pages']
    return pages_str

print(title_funct(my_book))
print(author_funct(my_book))
print(year_funct(my_book))
print(rating_funct(my_book))
print(pages_funct(my_book))

# Finally, create at least three new functions that might be useful as we expand our home library app. 
# Perhaps think of a way you could accept additional arguments when the function is called? 
# Also, imagine you have a list filled with dictionaries like above.

def return_all_titles(library):
#This function returns all book titles in the library
    titles = set()
    for book in library:
        titles.add(book['title'])
    return titles
    
print(return_all_titles(library))

def books_after_2000(library):
#This function returns all books written after 2000
    book_list = []
    for book in library:
        if book['year'] > 2000:
            book_list.append(book['title'])
        else:
            pass
    return book_list

print(books_after_2000(library))

def number_of_books(library):
#This function returns the amount of books in the library
    book_total = 0
    for book in library:
        book_total += 1
    return book_total

print(number_of_books(library))
