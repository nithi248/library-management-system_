# library management system
library_name = "Whitee Library"
print(f"Welcome to {library_name}!")

# all books in the library (fixed list)
library_books = ["DDM", "Python", "Java", "C++", "Data Science"]

# currently available books
available_books = ["DDM", "Python", "Java", "C++", "Data Science"]

# borrowed books
borrowed_books = []

while True:
    print("\n1. Show all library books")
    print("2. Check available books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter only numbers (1 to 5).")
        continue

    # 1. Show all books in library
    if choice == 1:
        print("\nAll library books:")
        for book in library_books:
            print(book)

    # 2. Show only available books
    elif choice == 2:
        print("\nAvailable books:")
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")

    # 3. Borrow a book
    elif choice == 3:
        book_name = input("Enter the book name to borrow: ")

        # first check if book belongs to library
        if book_name not in library_books:
            print(f"{book_name} does not belong to this library.")

        # then check if available
        elif book_name in available_books:
            available_books.remove(book_name)
            borrowed_books.append(book_name)
            print(f"You have borrowed {book_name}.")

        else:
            print(f"Sorry, {book_name} is currently not available.")

    # 4. Return a book
    elif choice == 4:
        book_name = input("Enter the book name to return: ")

        # check whether the book belongs to this library
        if book_name not in library_books:
            print(f"Invalid book! {book_name} does not belong to this library.")

        # check if user borrowed it
        elif book_name in borrowed_books:
            borrowed_books.remove(book_name)
            available_books.append(book_name)
            print(f"You have returned {book_name}.")

        # already in available books
        elif book_name in available_books:
            print(f"{book_name} is already available in the library.")

        else:
            print(f"You have not borrowed {book_name}.")

    # 5. Exit
    elif choice == 5:
        print("Thank you for using the library management system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")