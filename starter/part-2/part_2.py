### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['John Steinbeck', 'Delia Owens', 'Kristin Hannah', 'Lisa Wingate', 'Michael Crichton', 'Colleen Hoover', 'Kent Nerburn']

# Now let's add a new author to the end with the .append() method. Type your code below.

my_authors.append('Paulo Coelho')
# Example: my_authors.append("H.G. Wells")




# Now let's remove an element in the list

my_authors.remove("Lisa Wingate")
# Example: my_authors.remove("H.G. Wells")




# Now access an element by it's index. (Remember it indexes start at 0.)

my_authors[4]
# Example: my_authors[2]




# Now slice the list.

my_authors[0:2]
# Example: my_authors[1:4]



### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

author_tuple = ('Delia Owens', 'Michael Crichton', 'John Steinbeck')
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")


### Step 3 - Sets ###

# Create a set with your authors.

author_set = {'John Steinbeck', 'Delia Owens', 'Kristin Hannah', 'Lisa Wingate', 'Michael Crichton', 'Colleen Hoover', 'Kent Nerburn', 'Paolo Coelho'}
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}


# Add a new author to your set.

author_set.add('Jeanine Cummins')
# Example: my_author_set.add("J.R.R. Tolkien")


# Try adding the same author again, and be sure to print your set.

author_set.add('Jeanine Cummins')
print(author_set)
# Example: my_author_set.add("J.R.R. Tolkien")



### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

# for book in my_authors:
    # print(book)

# for book in my_authors_tuple:
    # print(book)

# for book in my_authors_set:
    # print(book)

