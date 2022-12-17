

### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. 
# Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, 
# to the .txt file properly formatted with commas as separators.

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



# def new_book(txt_file):
#     title = input("What is the name of the book you would like to add? ")
#     author = input("Who wrote the book you are adding? ")
#     try:
#         year = int(input("What year was this book published? "))
#     except:
#          year = int(input("Please type a number for the year? "))
#     try:
#         rating = float(input("What would you rate this book out of 5? "))
#     except:
#         rating = float(input("Please type a number for the rating. "))
#     try:
#         pages = int(input("How many pages long is this book? "))
#     except:
#         pages = int(input("Please type a number for the amount of pages. "))

#     with open(“library.txt”, “a”) as file:
#         file.write(f“{title}, {author}, {year}, {rating}, {pages}\n”)


def new_book():
        title = input("\nWhat is the title of the book you would like to add? ")
        author = input("Who wrote the book you are adding? ")
        try:
            year = int(input("What year was this book published? "))
        except:
            year = int(input("Please type a number for the year? "))
        try:
            rating = float(input("What would you rate this book out of 5? "))
        except:
            rating = float(input("Please type a number for the rating. "))
        try:
            pages = int(input("How many pages long is this book? "))
        except:
            pages = int(input("Please type a number for the amount of pages. "))

        with open("library.txt", "a") as file:
            file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


new_book()

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, 
# and make it work by reading the information in your home library's .txt document. 
# This will take some new logic, but you can do it.

# Code here


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

