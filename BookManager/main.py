class Book:
    # Constructor for the Book class, initializes book's title, author and publication year'
    def __init__(self, title, author, pub_year):
        self.title = title
        self.author = author
        self.pub_year = pub_year

    # Showing book details
    def show_details(self):
        print(f"--📘--\nTitle: {self.title}\nAuthor: {self.author}\nPublication Year: {self.pub_year}\n")

class BookManager:
    # Constructor for the BookManager class, initializes book list
    def __init__(self):
        self.books = []

    # adding a new book to the list
    def add_book(self, title, author, pub_year):
        new_book = Book(title.strip(), author.strip(), pub_year)
        self.books.append(new_book)
        print("\n✅ Book added successfully ✅\n")

    # displaying all the books
    def all_books(self):
        if not self.books:
            print("\n⛔ No books to display ⛔")
        else:
            print("\n🧾 List of all books:")
            for book in self.books:
                book.show_details()

    # searching for a book by  title
    def search_book(self, title):
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip():
                print("\n🔎 Book found:")
                book.show_details()
                return
        print("\n⛔ Book not found ⛔")

    # removing a book from the list
    def remove_book(self, title):
        for book in self.books:
            if book.title.lower().strip() == title.lower().strip():
                self.books.remove(book)
                print("\n✅ Book removed successfully ✅")
                return
        print("\n⛔ Book not found ⛔")

# Getting user input for a new book
def get_user_input():
    title = input("📝 Enter book's title: ")
    author = input("📝 Enter book's author: ")
    while True:
        try:
            pub_year = int(input("📝 Enter book's publication year: "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid year ❌")

    return title, author, pub_year
# Main function for the book manager
def main():
    # Creating an instance of BookManager class.
    book_manager = BookManager()

    # Running while loop until user exits the program
    while True:
        print("\n📚 Book Manager:")
        print("-- Add a new book (+)")
        print("-- Remove a book (-)")
        print("-- View all books (all)")
        print("-- Search by title (?)")
        print("-- Exit the program (exit)")

        user_input = input("📝 How may I help you (+, -, all, ?, exit): ").strip()

        # Running different methods based on user input
        if user_input == '+':
            title, author, pub_year = get_user_input()
            book_manager.add_book(title, author, pub_year)

        elif user_input == '-':
            title_to_remove = input("📝 Enter the title of the book to remove: ")
            book_manager.remove_book(title_to_remove)

        elif user_input == 'all':
            book_manager.all_books()

        elif user_input == '?':
            title_to_search = input("📝 Enter the book's title: ")
            book_manager.search_book(title_to_search)

        elif user_input == 'exit':
            print("💤 Exiting the program...")
            break

        else:
            print("❌ Invalid input. Please enter a valid option ❌")

# Running the book manager
main()