import books_holder
import datetime
from decimal import Decimal 


def add_book(new_author, new_publish_time, new_price):
    date_conv, deci_conv = data_cleaning(new_publish_time, new_price)
    book = [books_holder.Books(author=new_author, published=date_conv, price=deci_conv)]
    books_holder.session.add(book)

def edit_book():
    pass

def delete_book():
    pass

def search_book():
    pass

def data_cleaning(to_date, to_decimal):
    date = datetime.datetime.strptime(to_date, '%B %d, %Y').date()
    decimal = Decimal(to_decimal)
    return date, decimal

def main_menu():
    pass


#books_holder.Base.metadata.create_all(books_holder.engine)
