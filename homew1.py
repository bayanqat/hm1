books = []

for _ in range(4):
    book_name = input("Enter the Book Name: ")
    book_year = input("Enter the Book Year: ")
    book_author = input("Enter the Book Author: ")

    book = {
        'name': book_name,
        'year': book_year,
        'author': book_author  
    }
    books.append(book)


book_to_search = input("Enter book name to search: ")
found = False

for book in books:
    if book_to_search.lower() == book['name'].lower():
        print(f"Author of '{book['name']}': {book['author']}")
        found = True
        break

if not found:
    print("Book not found.")
