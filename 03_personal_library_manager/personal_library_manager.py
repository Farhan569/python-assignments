import streamlit as st
import json
import os

LIBRARY_FILE = "library.txt"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)

# Initialize library
if 'library' not in st.session_state:
    st.session_state.library = load_library()

# Functions
def add_book(title, author, year, genre, read):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    st.session_state.library.append(book)
    save_library(st.session_state.library)

def remove_book(title):
    library = st.session_state.library
    st.session_state.library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(st.session_state.library)

def search_books(keyword, by):
    keyword = keyword.lower()
    if by == "Title":
        return [book for book in st.session_state.library if keyword in book["title"].lower()]
    else:
        return [book for book in st.session_state.library if keyword in book["author"].lower()]

def display_books(books):
    if not books:
        st.write("No books to display.")
    for idx, book in enumerate(books, start=1):
        status = "Read" if book["read"] else "Unread"
        st.write(f"{idx}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# UI
st.title("📚 Personal Library Manager")

menu = st.sidebar.radio("Menu", ["Add Book", "Remove Book", "Search Book", "Display All Books", "Statistics"])

if menu == "Add Book":
    st.header("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, max_value=3000, step=1)
    genre = st.text_input("Genre")
    read = st.radio("Have you read it?", ["Yes", "No"]) == "Yes"
    if st.button("Add Book"):
        if title and author and genre:
            add_book(title, author, year, genre, read)
            st.success(f"Book '{title}' added!")
        else:
            st.error("Please fill all fields.")

elif menu == "Remove Book":
    st.header("Remove a Book")
    title = st.text_input("Enter the title of the book to remove")
    if st.button("Remove Book"):
        remove_book(title)
        st.success(f"Book '{title}' removed (if it existed).")

elif menu == "Search Book":
    st.header("Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    keyword = st.text_input("Enter search keyword")
    if st.button("Search"):
        results = search_books(keyword, search_by)
        st.subheader("Search Results")
        display_books(results)

elif menu == "Display All Books":
    st.header("All Books")
    display_books(st.session_state.library)

elif menu == "Statistics":
    st.header("Library Statistics")
    total_books = len(st.session_state.library)
    read_books = sum(1 for book in st.session_state.library if book["read"])
    if total_books > 0:
        percentage_read = (read_books / total_books) * 100
    else:
        percentage_read = 0
    st.write(f"**Total books:** {total_books}")
    st.write(f"**Percentage read:** {percentage_read:.1f}%")
