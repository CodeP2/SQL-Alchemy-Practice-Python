import books_holder
import accept_or_reject
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
                to_date = input("Published (Example: June 13, 2005): ")
                date = datetime.datetime.strptime(to_date, '%B %d, %Y').date()
                return date
            except ValueError as err:
                error_message(err, to_date, "June 13, 2005 (remember to add comma after a day!)")
                input("Press Enter to continue...")


def get_decimal():
    while True:
        try:
            to_decimal = input("Price (Example: 12.22): ")
            decimal_value = Decimal(to_decimal)
            if decimal_value.as_tuple().exponent < -2:
                raise ValueError("More than two decimal spaces")
            return decimal_value
        except (InvalidOperation, ValueError) as err:
            error_message(err, to_decimal, "19.99 (where . is a period not a comma and no currency sign!)")
            input("Press Enter to continue...")


def error_message(err, input, example):
    print(f"""\r#########Error###########
          \rIncorrect format -> {err}
          \rYour's Input: >{input}<
          \rExample: {example}
          \r##########################
          """)
