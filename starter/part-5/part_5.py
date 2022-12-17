

### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. 
# Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, 
# to the .txt file properly formatted with commas as separators.


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


# new_book()

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, 
# and make it work by reading the information in your home library's .txt document. 
# This will take some new logic, but you can do it.


def book_list():

    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            print(f"Book Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Number of Pages: {pages}")

# book_list()


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.





# def main_menu(library):
    
#     menu_run = True
    
#     while menu_run:
#         opt = int(input("Enter 1 to add a new book, 2 to see all of the books on the shelf, or 3 for neither "))
#         if opt == 1:
#             new_book()
#         elif opt == 2:
#             book_list()
#         elif opt == 3:
#             print("Thanks, Bye")
#             menu_run = False
#         else:
#             print("You must pick a number 1-3")

# if __name__ == "__main__":
#     main_menu("library.txt")




### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!


def title_with_rating():
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            print(f"Book Title: {title}, Rating: {rating},")


def main_menu(library):
    
    menu_run = True
    
    while menu_run:
        opt = int(input("Enter 1 to add a new book,\n 2 to see all of the books on the shelf,\n 3 to see all of the book titles with their rating,\n 4 to sdfjhsadlf,\n 5 to sdfjh,\n or 6 for none of the above "))
        if opt == 1:
            new_book()
        elif opt == 2:
            book_list()
        elif opt == 3:
            title_with_rating()
        # elif opt == 4:
        # elif opt == 5:
        elif opt == 6:
            print("Thanks, Bye")
            menu_run = False
        else:
            print("You must pick a number 1-6")

if __name__ == "__main__":
    main_menu("library.txt")