import books_holder


def accept_or_reject_menu():
    question = input(f"Are you sure you want to add/edit this user?(Y/N):\n")
    while True:
        if question.lower() in ["y", "n"]:
            break
        else:
            question = input(f"That's inncorrect input please try again (Correct inputs are (Y/N)\
                            \nAre you sure you want to add/edit this user?(Y/N):\n")
    if question.lower() == "y":
        books_holder.session.commit()
        print("Book added!")
    else:
        pass
