import books_holder
import book_analysis
import datetime
from decimal import Decimal


def add_book():
    new_author = input("Author: ")
    new_title = input("Title of the book: ")
    new_publish_time = input("Published (Example: January 13, 2005): ")
    new_price = input("Price (Example: 12.22): ")
    try:
        date_conv, deci_conv = data_cleaning(new_publish_time, new_price)
        book = books_holder.Books(author=new_author, title=new_title, published=date_conv, price=deci_conv)
        books_holder.session.add(book)
        yes_or_no_menu()
    except ValueError as err:
        input(f"failed to add a new book to data base: {err}\nPress enter to continue...")


def data_cleaning(to_date=None, to_decimal=None, option=1):
    if option == 1:
        date = datetime.datetime.strptime(to_date, '%B %d, %Y').date()
        decimal = Decimal(to_decimal)
        return date, decimal
    elif option == 2:
        date = datetime.datetime.strptime(to_date, '%B %d, %Y').date()
        return date
    elif option == 3:
        decimal = Decimal(to_decimal)
        return decimal


def show_all_books():
    entry_number = 1
    for entry in books_holder.session.query(books_holder.Books):
        print(f"Entry number: {entry_number}:\n{entry}")
        entry_number += 1


def search_book():
    print(f"Options: {[item[0] for item in books_holder.session.query(books_holder.Books.id)]}")
    index_number = int(input("What is the book's id? "))
    for entry in books_holder.session.query(books_holder.Books).filter(books_holder.Books.id==index_number):
        edit_or_delete_menu(entry)


def edit_or_delete_menu(entry):
    while True:
        try:
            option = int(input(f"for entry:\n{entry}\nwhat would you like to do?\n\n1) Edit a book\n2) Delete a book\n3) Exit\n\n>  "))
            if option == 1:
                edit_book(entry)
            elif option == 2:
                delete_book(entry)
            elif option == 3:
                break
            else:
                print("Incorrect Choice!")
        except ValueError:
            input(f"Incorect Choice!\nCorrect choices are: 1, 2, 3\nPress enter to continue...")


def edit_book(entry):
    print(f"Currently you are trying to edit:\n{entry}")
    option = int(input("What kind of entry would you like to change?\
                        \n1) Author\n2) Publish data\n3) Price\n\n>  "))
    if option == 1:
        new_author = input("Author: ")
        entry.author = new_author
    elif option == 2:
        new_publish = input("Published (Example: January 13, 2005): ")
        clean = data_cleaning(new_publish, None, 2)
        entry.published = clean
    elif option == 3:
        new_price = input("Price (Example: 12.22): ")
        clean = data_cleaning(None, new_price, 3)
        entry.price = clean
    yes_or_no_menu()


def delete_book(entry):
    confirm_to_delete = input("Are you sure you want to delete the book?(Y/N)\
                            \n(WARNING: This cannot be undone)\n\n>  ")
    if confirm_to_delete.lower() == "y":
        books_holder.session.delete(entry)
        books_holder.session.commit()
    else:
        pass


def yes_or_no_menu():
    question = input(f"Are you sure you want to add/edit this user?(Y/N):\n")
    while True:
        if question.lower() in ["y", "n"]:
            break
        else:
            question = input(f"That's inncorrect input please try again (Correct inputs are (Y/N)\
                            \nAre you sure you want to add/edit this user?(Y/N):\n")
    if question.lower() == "y":
        books_holder.session.commit()
        print("Book added!")
    else:
        pass


def book_analysis_menu():
    option = int(input("Analysis Menu\n1) Show the oldest book by publish date\n2) Show the newset book by publish date\
                       \n3) Show total number of the books\n4) Average price for all books\n>  "))
    if option == 1:
        print(book_analysis.oldest_book())
    elif option == 2:
        print(book_analysis.newest_book())
    elif option == 3:
        print(book_analysis.total_books())
    elif option == 4:
        print(book_analysis.avg_price())
    input("Press enter to continue...")


def main_menu():
    while True:
        print("PROGRAMING BOOKS\n1) Add Book\n2) View All Books\n3) Search for a book\
              \n4) Book Analysis\n5) Exit\n")
        try:
            decision = int(input("What Would you like to do?\n>  "))
            if decision == 1:
                add_book()
            elif decision == 2:
                show_all_books()
            elif decision == 3:
                search_book()
            elif decision == 4:
                print(book_analysis_menu())
            elif decision == 5:
                break
            else:
                print(f"Incorrect Choice: {decision}")
        except ValueError:
            print(f"Incorrect Choice.\nCorrect choices are: 1, 2, 3, 4, 5")


books_holder.Base.metadata.create_all(books_holder.engine)
main_menu()
