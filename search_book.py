import books_holder
import search_by_x


def show_all_books():
    entry_number = 1
    for entry in books_holder.session.query(books_holder.Books):
        print(f"Entry number: {entry_number}:\n{entry}")
        entry_number += 1


def search_book_menu():
    while True:
        print("Search book menu:\n1) Search by index\n2) Search by author's name\n3) Search by title\
              \n4) Search by published date\n5) Search by price\n6) Exit")
        option = int(input("What would you like to do?\n>  "))
        if option == 1:
            search_by_x.search_by_index()
        elif option == 2:
            search_by_x.search_by_name()
        elif option == 6:
            break
        else:
            print("Incorrect choice!")
