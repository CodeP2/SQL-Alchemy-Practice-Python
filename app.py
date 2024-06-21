import books_holder
import datetime
from decimal import Decimal


def add_book(new_author, new_publish_time, new_price):
    date_conv, deci_conv = data_cleaning(new_publish_time, new_price)
    book = books_holder.Books(author=new_author, published=date_conv, price=deci_conv)
    books_holder.session.add(book)

def edit_book(book_index):
    pass    

def delete_book():
    pass

def search_book(index_number):
    for entry in books_holder.session.query(books_holder.Books).filter(books_holder.Books.id==index_number):
        print(entry)

def data_cleaning(to_date, to_decimal):
    date = datetime.datetime.strptime(to_date, '%B %d, %Y').date()
    decimal = Decimal(to_decimal)
    return date, decimal

def main_menu():
    while True:
        print("PROGRAMING BOOKS\n1) Add Book\n2) View All Books\n3) Search for a book\
              \n4) Book Analysis\n5) Exit\n")
        decision = int(input("What Would you like to do?\n"))
        if decision == 1:
            author = input("Author: ")
            published = input("Published (Example: January 13, 2005): ")
            price = input("Price (Example: 12.22): ")
            add_book(author, published, price)
            print("Book added!")
        elif decision == 2:
            pass
        elif decision == 3:
            print("Options: []")
            index_num = int(input("What is the book's id? "))
            search_book(index_num)
        elif decision == 4:
            pass
        elif decision == 5:
            break

books_holder.Base.metadata.create_all(books_holder.engine)
main_menu()
