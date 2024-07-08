import books_holder
import edit_or_delete_book


def show_all_books():
    entry_number = 1
    for entry in books_holder.session.query(books_holder.Books):
        print(f"Entry number: {entry_number}:\n{entry}")
        entry_number += 1


def search_book():
    print(f"Options: {[item[0] for item in books_holder.session.query(books_holder.Books.id)]}")
    index_number = int(input("What is the book's id? "))
    for entry in books_holder.session.query(books_holder.Books).filter(books_holder.Books.id==index_number):
        edit_or_delete_book.edit_or_delete_menu(entry)
