import books_holder


def Index_list():
    return [item[0] for item in books_holder.session.query(books_holder.Books.id)]


def author_name_list():
    author_names = collect_entries("author")
    stop_entries(author_names)


def title_list():
    title_names = collect_entries("title")
    stop_entries(title_names)


def publish_date_list():
    publish_dates = collect_entries("published")
    stop_entries(publish_dates)


def price_list():
    prices = collect_entries("price")
    stop_entries(prices)


def collect_entries(column_name):
    empty_list = []
    column = getattr(books_holder.Books, column_name)
    for entry in books_holder.session.query(column):
        empty_list.append(entry)
    return empty_list


def stop_entries(entry):
    counter = 0
    for item in entry:
        print(item)
        counter += 1
        if counter == 5:
            input("press enter to continue...")
            counter = 0
