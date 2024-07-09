import books_holder
import add_and_get_data
import accept_or_reject
import error_messages as error


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
                error.menu_choice_error("1, 2, 3")
        except ValueError:
            error.menu_choice_error("1, 2, 3")


def edit_book(entry):
    while True:
        print(f"Currently you are trying to edit:\n{entry}")
        try:
            option_string = input("What kind of entry would you like to change?\
                        \n1) Author\n2) Publish data\n3) Price\n4) Finish editing.\n>  ")
            option = int(option_string)
            if option == 1:
                new_author = input("Author: ")
                entry.author = new_author
            elif option == 2:
                clean = add_and_get_data.get_date()
                entry.published = clean
            elif option == 3:
                clean = add_and_get_data.get_decimal()
                entry.price = clean
            elif option == 4:
                break
            elif option not in [1, 2, 3, 4]:
                error.menu_choice_error("1, 2, 3, 4")
            else:
                accept_or_reject.accept_or_reject_menu()
        except ValueError:
            error.menu_choice_error("1, 2, 3, 4")



def delete_book(entry):
    while True:
        confirm_to_delete = input("Are you sure you want to delete the book?(Y/N)\
                            \n(WARNING: This cannot be undone)\n\n>  ")
        if confirm_to_delete.lower() == "y":
            books_holder.session.delete(entry)
            books_holder.session.commit()
        elif confirm_to_delete.lower() not in ["y", "n"]:
            error.menu_choice_error("Y/N")
        else:
            break
