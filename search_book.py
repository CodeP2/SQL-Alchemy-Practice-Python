import books_holder
import search_by_x
import error_messages
import menu_messages


def show_all_books():
    entry_number = 1
    for entry in books_holder.session.query(books_holder.Books):
        print(f"Entry number: {entry_number}:\n{entry}")
        entry_number += 1


def search_book_menu():
    while True:
        menu_messages.search_book_menu()
        try:
            option = int(input("What would you like to do?\n>  "))
            if option == 1:
                search_by_x.search_by_index()
            elif option == 2:
                search_by_x.search_by_name()
            elif option == 3:
                search_by_x.search_by_title()
            elif option == 4:
                search_by_x.search_by_publish_date()
            elif option == 5:
                search_by_x.search_by_price()
            elif option == 6:
                break
            else:
                print("Incorrect choice!")
        except ValueError:
            error_messages.menu_choice_error("1, 2, 3, 4, 5, 6")
