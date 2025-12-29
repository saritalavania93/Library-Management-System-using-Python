# Mini-Project-
This mini project demonstrates the application of Python basics such as dictionaries, functions, loops, and conditional statements to build a Library Management System. It includes login authentication and book management features like adding, issuing, returning, and viewing books.

Project –Overview

Create a Library Management System using Python. Below are the steps which you need to follow to create an end-to-end project for LMS. Here Librarian can add/modify/issue the books and can perform various other operation as listed in below steps. 
Use Python concepts only for creating this project.
Steps:
Step 1: Basic Structure
1.	Write a Python script that prints a welcome message for the Library Management System.
2.	Define an initial list or dictionary to store books, with details like title, author, and availability.
Example:
library = {
    "Python Basics": {"author": "Test", "available": True},
    "Data Science": {"author": "Test1", "available": False}
}
3.	Write a function to display all the books with their details.
________________________________________
Step 2: Adding Books
4.	Create a function to allow a user to add a new book to the system. The function should:
o	Accept inputs for the title and author.
o	Check if the book already exists in the dictionary.
o	Add the book if it doesn’t exist.
________________________________________
Step 3: Issuing Books
5.	Create a function to issue a book. The function should:
o	Check if the book exists and is available.
o	Mark it as unavailable if issued and record the name of the person issuing it.
6.	Modify the display function to show the current status of the book (Available or Issued).
________________________________________
Step 4: Returning Books
7.	Create a function to return a book. The function should:
o	Check if the book exists and is currently issued.
o	Mark it as available again upon return.
________________________________________
Step 5: Login System
8.	Implement a login system:
o	Store usernames and passwords in a dictionary. You can have some predefined stored credentials like below:
credentials = {"admin": "admin123", "librarian": "lib123"}
o	Prompt users to log in before accessing the system.
o	Allow up to 3 attempts before exiting.
________________________________________
Step 6: View Issued Books
9.	Add a function to view all books that are currently issued, along with the name of the person who issued them.
________________________________________
Step 7: Main Menu
10.	Combine all the functions into a menu-driven program:
o	Use a while loop to display options like:
	View Books
	Add a Book
	Issue a Book
	Return a Book
	View Issued Books
	Exit

