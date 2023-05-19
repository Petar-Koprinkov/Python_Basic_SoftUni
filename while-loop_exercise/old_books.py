books_count = 0
favourite_book = input()

while True:
    book = input()
    books_count += 1

    if book == "No More Books":

        print("The book you search is not here!")
        print(f"You checked {books_count- 1} books.")
        break
    if book == favourite_book:

        print(f"You checked {books_count- 1} books and found it.")
        break
