import books_holder
import edit_or_delete_book
import entries_by_x
import error_messages as error


def query_by(entry_type ,column_name):
    column = getattr(books_holder.Books, column_name)
    for entry in books_holder.session.query(books_holder.Books).filter(column==entry_type):
        edit_or_delete_book.edit_or_delete_menu(entry)


def search_by_index():
    index_list = entries_by_x.Index_list()
    while True:
        print(f"Index options: {index_list}")
        try:
            index_string = input("What is the book's id? ")
            index_number = int(index_string.strip())
            if index_number in index_list:
                break
            else:
                input("Index not found!\nPress enter to continue...")
        except ValueError:
            error.integer_error_massage(index_string, index_list)
    query_by(index_number, "id")


def search_by_name():
    while True:
        author_names_list = entries_by_x.author_name_list()
        author = input("What is the name of the author?\n>  ").strip()
        query_by(author, "author")
        if author in author_names_list:
            break
