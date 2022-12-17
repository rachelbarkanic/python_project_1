### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. 
# After that be sure to turn it into a function.

# def new_book():
#     title = input("What is the name of the book you would like to add? ")
#     author = input("Who wrote the book you are adding? ")
#     year = input("What year was this book published? ")
#     rating = input("What would you rate this book out of 5? ")
#     pages = input("How many pages long is this book? ")

#     book_dict = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dict

    



### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. 
# Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# def new_book():
#     title = input("What is the name of the book you would like to add? ")
#     author = input("Who wrote the book you are adding? ")
#     year = int(input("What year was this book published? "))
#     rating = float(input("What would you rate this book out of 5? "))
#     pages = int(input("How many pages long is this book? "))

#     book_dict = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dict



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.


def new_book():
    title = input("What is the name of the book you would like to add? ")
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

    book_dict = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dict


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

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


# def main_menu():
#     opt = int(input("Enter 1 to add a new book, 2 to see all of the books on the shelf, or 3 for neither "))
    
#     if opt == 1:
#         new_book()
#         print(library)
#     elif opt == 2:
#         titles = set()
#         for book in library:
#                 titles.add(book['title'])
#         print(titles)
#     elif opt == 3:
#         print("Thanks, Bye")
#     else:
#         print("You must pick a number 1-3")






### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, 
# and continually asking for input until the user chooses to exit the program. 
# Call the main menu to ensure it functions properly.


def main_menu():

    menu_run = True
    
    while menu_run:
        opt = int(input("Enter 1 to add a new book, 2 to see all of the books on the shelf, or 3 for neither "))
        if opt == 1:
            new_book()
            print(library)
        elif opt == 2:
            titles = set()
            for book in library:
                titles.add(book['title'])
            print(titles)
        elif opt == 3:
            print("Thanks, Bye")
            menu_run = False
        else:
            print("You must pick a number 1-3")

if __name__ == "__main__":
    main_menu("library.txt")
