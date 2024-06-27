books = input().split("&")

while True:
    text = input()
    if text == "Done":
        break
    commands = text.split(" | ")
    command = commands[0]

    if command == "Add Book":
        book_name = commands[1]
        if book_name not in books:
            books.insert(0, book_name)
    elif command == "Take Book":
        book_name = commands[1]
        if book_name in books:
            books.remove(book_name)
    elif command == "Swap Books":
        book1 = commands[1]
        book2 = commands[2]
        if book1 in books and book2 in books:
            book1_index = books.index(book1)
            book2_index = books.index(book2)
            books[book1_index], books[book2_index] = books[book2_index], books[book1_index]
    elif command == "Insert Book":
        book_name = commands[1]
        if book_name not in books:
            books.append(book_name)
    elif command == "Check Book":
        book_name = commands[1]
        given_index = int(book_name)
        if 0 <= given_index < len(books):
            print(books[given_index])
print(', '.join(map(str, books)))