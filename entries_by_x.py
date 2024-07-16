import books_holder


def Index_list():
    return [item[0] for item in books_holder.session.query(books_holder.Books.id)]


def author_name_list():
    author_names = []
    for entry in books_holder.session.query(books_holder.Books.author):
        author_names.append(entry)
    stop_entries(author_names)


def title_list():
    return [item[0] for item in books_holder.session.query(books_holder.Books.title)]


def publish_date_list():
    return [item[0] for item in books_holder.session.query(books_holder.Books.published)]


def price_list():
    return [item[0] for item in books_holder.session.query(books_holder.Books.price)]


def stop_entries(entry):
    counter = 0
    for item in entry:
        print(item)
        counter += 1
        if counter == 5:
            input("press enter to continue...")
            counter = 0
