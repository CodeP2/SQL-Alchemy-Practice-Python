import add_and_get_data
import search_book
import book_analysis
import error_messages as error
import menu_messages


def main_menu():
    while True:
        menu_messages.main_menu()
        try:
            decision = int(input("What Would you like to do?\n>  "))
            if decision == 1:
                add_and_get_data.add_book()
            elif decision == 2:
                search_book.show_all_books()
            elif decision == 3:
                search_book.search_book_menu()
            elif decision == 4:
                print(book_analysis.book_analysis_menu())
            elif decision == 5:
                break
            else:
                print(f"Incorrect Choice: {decision}")
        except ValueError:
            error.menu_choice_error("1, 2, 3, 4, 5")


if __name__ == "__main__":
    main_menu()
