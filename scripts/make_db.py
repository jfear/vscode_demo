"""Some Examples"""
import sqlite3 as db

import pandas as pd


def main():
    df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 7]})

    con = db.connect("/tmp/my_sql_test.sqlite")
    df.to_sql("pd2sql", con)
    con.close()


# TODO: pd.read_csv intellisense

# TODO: def snippet

# TODO: Show how to make your own snippets

if __name__ == "__main__":
    main()
