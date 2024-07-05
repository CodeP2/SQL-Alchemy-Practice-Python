import books_holder
import pandas as pd
import os


script_path = os.path.dirname(__file__)
file = os.path.join(script_path, "suggested_books.csv","suggested_books.csv")

def csv_to_dataframe(path):
    with open(path, "r", newline="") as csvfile:
        first_row = csvfile.readline().strip().split(",")
        has_header = any(field.isalpha() for field in first_row)

        csvfile.seek(0)

        if has_header:
            reader = pd.read_csv(csvfile)
        else:
            reader = pd.read_csv(csvfile, names=["title", "author", "published", "price"])
    return reader


def convert_data(data_frame):
    data_frame["price"] = data_frame["price"].astype(float)
    data_frame["published"] = pd.to_datetime(data_frame["published"], format="%B %d, %Y").dt.date
    return data_frame


if __name__ == "__main__":
    data_base = csv_to_dataframe(file)
    print(data_base)
    clean_data_base = convert_data(data_base)
    print("\n", clean_data_base)
    clean_data_base.to_sql("books", con=books_holder.engine, if_exists="append", index=False)
