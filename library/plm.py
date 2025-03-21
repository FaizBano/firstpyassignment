import os
import json
import streamlit as st
from PIL import Image

def bold_text(text):
    return f"<strong>{text}</strong>"

class Book:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

    def __repr__(self):
        return f"**Title:** {self.title}, **Author:** {self.author}, **Year:** {self.year}, **Genre:** {self.genre}, **Read:** {'Yes' if self.read_status else 'No'}"

class Library:
    def __init__(self):
        self.books = []
        self.load_library()

    def add_book(self, title, author, year, genre, read_status):
        new_book = Book(title, author, year, genre, read_status)
        self.books.append(new_book)
        self.save_library()

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_library()
                return True
        return False

    def search_books(self, search_term):
        return [book for book in self.books if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]

    def display_books(self):
        return self.books

    def display_statistics(self):
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book.read_status)
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        return total_books, read_books, percentage_read

    def save_library(self):
        with open("library.json", "w") as file:
            json.dump([book.__dict__ for book in self.books], file, indent=4)

    def load_library(self):
        if os.path.exists("library.json"):
            with open("library.json", "r") as file:
                book_data = json.load(file)
                self.books = [Book(**data) for data in book_data]

# Streamlit interface
def main():
    st.title("Personal Library Manager 🎉")

    # Sidebar Image and Intro
    st.sidebar.header("About Me 👋")
    
    try:
        

        image = Image.open('/pic1.png')  # Replace with your image path
        st.sidebar.image(image, caption="Faiz Bano Frontend Developer", use_column_width=True)
    except:
        st.sidebar.warning("Image not found. Please check the path.")

    st.sidebar.markdown("""
        **Hello! I'm Faiz Bano, I am a student of GIAIC, and now working with HTML, CSS, Typescript, Next.js. 
        My journey continues with Python and more 📚.**
    """)

    library = Library()

    menu = ["Add a book 📚", "Remove a book 🗑️", "Search for a book 🔍", "Display all books 📖", "Display statistics 📊", "Exit 🚪"]
    choice = st.sidebar.selectbox("Choose an option", menu)

    if choice == "Add a book 📚":
        st.subheader("Add a Book ✨")
        st.markdown(bold_text("Title of the book"), unsafe_allow_html=True)
        title = st.text_input("", key="title")

        st.markdown(bold_text("Author of the book"), unsafe_allow_html=True)
        author = st.text_input("", key="author")

        st.markdown(bold_text("Publication Year"), unsafe_allow_html=True)
        year = st.number_input("", min_value=1000, max_value=9999, step=1, key="year")

        st.markdown(bold_text("Genre of the book"), unsafe_allow_html=True)
        genre = st.text_input("", key="genre")

        st.markdown(bold_text("Have you read this book?"), unsafe_allow_html=True)
        read_status = st.radio("", ("Yes", "No"), key="read")

        if st.button("Add Book 🖊️"):
            if title and author and genre:
                library.add_book(title, author, year, genre, read_status == "Yes")
                st.success(f"Book '{title}' added successfully! 🎉")
            else:
                st.warning("Please fill in all fields! 🚨")

    elif choice == "Remove a book 🗑️":
        st.subheader("Remove a Book 🗑️")
        st.markdown(bold_text("Enter the title of the book to remove"), unsafe_allow_html=True)
        title_to_remove = st.text_input("")

        if st.button("Remove Book 🚮"):
            if title_to_remove:
                if library.remove_book(title_to_remove):
                    st.success(f"Book '{title_to_remove}' removed successfully! 🧹")
                else:
                    st.warning(f"Book with title '{title_to_remove}' not found. 🤔")
            else:
                st.warning("Please enter a book title. 🚨")

    elif choice == "Search for a book 🔍":
        st.subheader("Search for a Book 🔎")
        st.markdown(bold_text("Enter title or author to search"), unsafe_allow_html=True)
        search_term = st.text_input("")

        if st.button("Search 🔍"):
            if search_term:
                results = library.search_books(search_term)
                if results:
                    for book in results:
                        st.write(book)
                else:
                    st.warning("No books found matching that search term. 🤷")
            else:
                st.warning("Please enter a search term. 🚨")

    elif choice == "Display all books 📖":
        st.subheader("All Books 📚")
        books = library.display_books()
        if books:
            for idx, book in enumerate(books, start=1):
                st.write(f"{idx}. {book}")
        else:
            st.warning("No books in your library. 🤔")

    elif choice == "Display statistics 📊":
        st.subheader("Library Statistics 📈")
        total_books, read_books, percentage_read = library.display_statistics()
        st.write(f"Total books in the library: **{total_books}**")
        st.write(f"Books read: **{read_books}**")
        st.write(f"Percentage of books read: **{percentage_read:.2f}%**")

    elif choice == "Exit 🚪":
        st.write("Thank you for using the Personal Library Manager. Goodbye! 👋")

if __name__ == "__main__":
    main()
