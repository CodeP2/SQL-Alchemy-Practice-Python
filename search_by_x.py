import books_holder
import edit_or_delete_book
import entries_by_x
import error_messages as error
import add_and_get_data


def query_by(entry_type ,column_name):
    column = getattr(books_holder.Books, column_name)
    for entry in books_holder.session.query(books_holder.Books).filter(column==entry_type):
        edit_or_delete_book.edit_or_delete_menu(entry)


def get_valid_imput(prompt, valid_list, error_message, index=False, price=False, date=False, index_list=None):
    while True:
        try:
            if index:
                print(f"Options: {index_list}")
                string_input = input(prompt).strip()
                user_input = int(string_input)
            if price:
                user_input = add_and_get_data.get_decimal()
            if date:
                user_input = add_and_get_data.get_date()
            else:    
                user_input = input(prompt).strip()
            if user_input in valid_list:
                return user_input
            else:
                input(f"{error_message}\nPress enter to continue...")
        except ValueError as err:
            if index:
                error.integer_error_massage(string_input)
            else:
                print(f"{err}")


def search_by_index():
    index_list = entries_by_x.Index_list()
    index_number = get_valid_imput("What is the book's id? ", index_list, "Index not found!", True, index_list)
    query_by(index_number, "id")


def search_by_name():
    author_names_list = entries_by_x.author_name_list()
    author = get_valid_imput("What is the name of the author?\n>  ", author_names_list, "Invalid author!")
    query_by(author, "author")


def search_by_title():
    title_list = entries_by_x.title_list()
    title = get_valid_imput("What is the title?\n>  ", title_list, "Invalid title!")
    query_by(title, "title")


def search_by_publish_date():
    publish_date_list = entries_by_x.publish_date_list()
    published = get_valid_imput("What is the date of the publication?\n>  ", publish_date_list, "Invalid publication date!", False, False, True)
    query_by(published, "published")


def search_by_price():
    price_list = entries_by_x.price_list()
    price = get_valid_imput("What is the price of the book?\n>  ", price_list, "Invalid price!", False, True)
    query_by(price, "price")
