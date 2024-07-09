import books_holder
import error_messages as error


def oldest_book():
    return books_holder.session.query(books_holder.Books).order_by(books_holder.Books.published).first()


def newest_book():
    return books_holder.session.query(books_holder.Books).order_by(books_holder.desc(books_holder.Books.published)).first()


def total_books():
    return books_holder.session.query(books_holder.func.count()).select_from(books_holder.Books).scalar()


def avg_price():
    return books_holder.session.query(books_holder.func.avg(books_holder.Books.price)).scalar()


def book_analysis_menu():
    while True:
        try:
            option_string = input("Analysis Menu\n1) Show the oldest book by publish date\n2) Show the newset book by publish date\
                       \n3) Show total number of the books\n4) Average price for all books\n5) Exit\n>  ")
            option = int(option_string)
            if option == 1:
                print(oldest_book())
            elif option == 2:
                print(newest_book())
            elif option == 3:
                print(total_books())
            elif option == 4:
                print(avg_price())
            elif option == 5:
                break
            elif option not in [1, 2, 3, 4, 5]:
                error.menu_choice_error("1, 2, 3, 4")
            else:
                input("Press enter to continue...")
        except ValueError:
            error.menu_choice_error("1, 2, 3, 4")
