import books_holder
import add_and_get_data
import accept_or_reject


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
        clean = add_and_get_data.get_date(new_publish, None, 2)
        entry.published = clean
    elif option == 3:
        new_price = input("Price (Example: 12.22): ")
        clean = add_and_get_data.get_decimal(None, new_price, 3)
        entry.price = clean
    accept_or_reject.accept_or_reject_menu()


def delete_book(entry):
    confirm_to_delete = input("Are you sure you want to delete the book?(Y/N)\
                            \n(WARNING: This cannot be undone)\n\n>  ")
    if confirm_to_delete.lower() == "y":
        books_holder.session.delete(entry)
        books_holder.session.commit()
    else:
        pass
