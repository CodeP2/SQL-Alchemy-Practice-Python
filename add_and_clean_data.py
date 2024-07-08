import books_holder
import accept_or_reject
import datetime
from decimal import Decimal


def add_book():
    new_author = input("Author: ")
    new_title = input("Title of the book: ")
    new_publish_time = input("Published (Example: June 13, 2005): ")
    new_price = input("Price (Example: 12.22): ")
    try:
        date_conv, deci_conv = data_cleaning(new_publish_time, new_price)
        book = books_holder.Books(author=new_author, title=new_title, published=date_conv, price=deci_conv)
        books_holder.session.add(book)
        accept_or_reject.yes_or_no_menu()
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