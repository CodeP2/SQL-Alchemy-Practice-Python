import add_and_clean_data
import search_book
import book_analysis


def main_menu_message():
    print("""\rPROGRAMING BOOKS
          \r1) Add Book
          \r2) View All Books
          \r3) Search for a book
          \r4) Book Analysis
          \r5) Exit
          """)


def main_menu():
    while True:
        main_menu_message()
        try:
            decision = int(input("What Would you like to do?\n>  "))
            if decision == 1:
                add_and_clean_data.add_book()
            elif decision == 2:
                search_book.show_all_books()
            elif decision == 3:
                search_book.search_book()
            elif decision == 4:
                print(book_analysis.book_analysis_menu())
            elif decision == 5:
                break
            else:
                print(f"Incorrect Choice: {decision}")
        except ValueError:
            input(f"Incorrect Choice.\nCorrect choices are: 1, 2, 3, 4, 5\
                  \nPress enter to conitnue...")


if __name__ == "__main__":
    main_menu()
