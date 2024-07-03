import books_holder


def oldest_book():
    return books_holder.session.query(books_holder.Books).order_by(books_holder.Books.published).first()


def newest_book():
    return books_holder.session.query(books_holder.Books).order_by(books_holder.desc(books_holder.Books.published)).first()


def total_books():
    return books_holder.session.query(books_holder.func.count()).select_from(books_holder.Books).scalar()


def avg_price():
    return books_holder.session.query(books_holder.func.avg(books_holder.Books.price)).scalar()
