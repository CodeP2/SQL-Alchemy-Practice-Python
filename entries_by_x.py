import books_holder


def Index_list():
    return get_entry_values_by(getattr(books_holder.Books, "id"))


def author_name_list():
    author_names, column_names = collect_entries("author")
    stop_entries(author_names)
    return get_entry_values_by(column_names)


def title_list():
    title_names, column_names = collect_entries("title")
    stop_entries(title_names)
    return get_entry_values_by(column_names)


def publish_date_list():
    publish_dates, column_names = collect_entries("published")
    stop_entries(publish_dates)
    return get_entry_values_by(column_names)


def price_list():
    prices, column_names = collect_entries("price")
    stop_entries(prices)
    return get_entry_values_by(column_names)


def collect_entries(column_name):
    empty_list = []
    column = getattr(books_holder.Books, column_name)
    for entry in books_holder.session.query(column):
        empty_list.append(entry)
    return empty_list, column


def stop_entries(entry):
    counter = 0
    for item in entry:
        print(item)
        counter += 1
        if counter == 5:
            input("press enter to continue...")
            counter = 0


def get_entry_values_by(column_name):
    return [item[0] for item in books_holder.session.query(column_name)]
