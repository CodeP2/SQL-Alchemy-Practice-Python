import books_holder
import accept_or_reject
import error_messages as error
import datetime
from decimal import Decimal, InvalidOperation


def add_book():
    new_author = input("Author: ")
    new_title = input("Title of the book: ")
    new_publish_time = get_date()
    new_price = get_decimal()
    book = books_holder.Books(author=new_author, title=new_title, published=new_publish_time, price=new_price)
    books_holder.session.add(book)
    accept_or_reject.accept_or_reject_menu()


def get_date():
        while True:
            try:
                get_date = input("Published (Example: June 13, 2005): ")
                segments = [segment.strip() for segment in get_date.split(",")]
                joined_segments = ", ".join(segments)
                date = datetime.datetime.strptime(joined_segments, '%B %d, %Y').date()
                return date
            except ValueError as err:
                error.data_convertion_error_message(err, get_date, "June 13, 2005 (remember to add comma after a day!)")


def get_decimal():
    while True:
        try:
            get_decimal = input("Price (Example: 12.22): ")
            striped_get_decimal = get_decimal.strip()
            decimal_value = Decimal(striped_get_decimal)
            if decimal_value.as_tuple().exponent < -2:
                raise ValueError("More than two decimal spaces")
            return decimal_value
        except (InvalidOperation, ValueError) as err:
            error.data_convertion_error_message(err, get_decimal, "19.99 (where . is a period not a comma and no currency sign!)")