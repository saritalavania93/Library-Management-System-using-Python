import streamlit as st

# -----------------------------
# Predefined user credentials
# -----------------------------
credentials = {
    "admin": "admin123",
    "librarian": "lib123"
}

# -----------------------------
# Initialize session state
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "books" not in st.session_state:
    st.session_state.books = [
        {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "available": True, "issued_to": None},
        {"id": 2, "title": "1984", "author": "George Orwell", "available": False, "issued_to": "Alice"},
        {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": True, "issued_to": None}
    ]

# -----------------------------
# Login Page
# -----------------------------
def login_page():
    st.title("📚 Library Management System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username.lower() in credentials and credentials[username.lower()] == password:
            st.session_state.logged_in = True
            st.success(f"Welcome {username}")
        else:
            st.error("Invalid username or password")

# -----------------------------
# Display Books
# -----------------------------
def view_books():
    st.subheader("Library Books")

    for book in st.session_state.books:
        status = "Available" if book["available"] else f"Issued to {book['issued_to']}"
        st.write(f'**ID:** {book["id"]} | **Title:** {book["title"]} | **Author:** {book["author"]} | **Status:** {status}')

# -----------------------------
# Add Book
# -----------------------------
def add_book():
    st.subheader("Add New Book")

    title = st.text_input("Book Title")
    author = st.text_input("Author")

    if st.button("Add Book"):
        for book in st.session_state.books:
            if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
                st.warning("Book already exists")
                return

        new_id = max(book["id"] for book in st.session_state.books) + 1

        st.session_state.books.append({
            "id": new_id,
            "title": title,
            "author": author,
            "available": True,
            "issued_to": None
        })

        st.success("Book added successfully")

# -----------------------------
# Issue Book
# -----------------------------
def issue_book():
    st.subheader("Issue Book")

    book_id = st.number_input("Enter Book ID", step=1)
    person = st.text_input("Issued To")

    if st.button("Issue Book"):

        for book in st.session_state.books:
            if book["id"] == book_id:

                if book["available"]:
                    book["available"] = False
                    book["issued_to"] = person
                    st.success(f'Book "{book["title"]}" issued to {person}')
                    return
                else:
                    st.warning(f'Book already issued to {book["issued_to"]}')
                    return

        st.error("Book not found")

# -----------------------------
# Return Book
# -----------------------------
def return_book():
    st.subheader("Return Book")

    book_id = st.number_input("Enter Book ID to return", step=1)

    if st.button("Return Book"):

        for book in st.session_state.books:

            if book["id"] == book_id:

                if not book["available"]:
                    book["available"] = True
                    book["issued_to"] = None
                    st.success("Book returned successfully")
                    return

                else:
                    st.warning("Book was not issued")
                    return

        st.error("Book not found")

# -----------------------------
# View Issued Books
# -----------------------------
def view_issued_books():
    st.subheader("Issued Books")

    issued = [book for book in st.session_state.books if not book["available"]]

    if not issued:
        st.info("No books issued")
        return

    for book in issued:
        st.write(f'**ID:** {book["id"]} | **Title:** {book["title"]} | **Issued to:** {book["issued_to"]}')

# -----------------------------
# Main App
# -----------------------------
def main_app():

    st.sidebar.title("Menu")

    option = st.sidebar.selectbox(
        "Select Option",
        ["View Books", "Add Book", "Issue Book", "Return Book", "Issued Books"]
    )

    if option == "View Books":
        view_books()

    elif option == "Add Book":
        add_book()

    elif option == "Issue Book":
        issue_book()

    elif option == "Return Book":
        return_book()

    elif option == "Issued Books":
        view_issued_books()

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False

# -----------------------------
# App Control
# -----------------------------
if not st.session_state.logged_in:
    login_page()
else:
    main_app()