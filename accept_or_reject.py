import books_holder
import error_messages as error


def accept_or_reject_menu():
    question = input(f"Are you sure you want to add/edit this user?(Y/N):\n")
    while True:
        if question.lower() in ["y", "n"]:
            break
        else:
            error.menu_choice_error("Y/N")
    if question.lower() == "y":
        books_holder.session.commit()
        print("Book added!")
    else:
        pass
