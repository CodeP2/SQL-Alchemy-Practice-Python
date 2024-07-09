import books_holder
import edit_or_delete_book
import error_messages as error


def show_all_books():
    entry_number = 1
    for entry in books_holder.session.query(books_holder.Books):
        print(f"Entry number: {entry_number}:\n{entry}")
        entry_number += 1


def search_book():
    index_list = [item[0] for item in books_holder.session.query(books_holder.Books.id)]
    index_number = search_by_index(index_list)
    for entry in books_holder.session.query(books_holder.Books).filter(books_holder.Books.id==index_number):
        edit_or_delete_book.edit_or_delete_menu(entry)


def search_by_index(index_list):
    while True:
        print(f"Index options: {index_list}")
        try:
            index_string = input("What is the book's id? ")
            index_number = int(index_string.strip())
            if index_number in index_list:
                break
            else:
                input("Index not found!\nPress enter to continue...")
        except ValueError:
            error.integer_error_massage(index_string, index_list)
    return index_number