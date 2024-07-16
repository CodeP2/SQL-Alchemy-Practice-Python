import books_holder
import edit_or_delete_book
import entries_by_x
import error_messages as error


def show_all_books():
    entry_number = 1
    for entry in books_holder.session.query(books_holder.Books):
        print(f"Entry number: {entry_number}:\n{entry}")
        entry_number += 1


def search_by_index():
    index_list = entries_by_x.Index_list()
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
    for entry in books_holder.session.query(books_holder.Books).filter(books_holder.Books.id==index_number):
        edit_or_delete_book.edit_or_delete_menu(entry)


def search_by_name():
    while True:
        entries_by_x.author_name_list()
        author = input("What is the name of the author?\n>  ")



def search_book_menu():
    while True:
        print("search book menu")
        option = int(input("What would you like to do?\n>  "))
        if option == 1:
            search_by_index()
        elif option == 2:
            search_by_name()
