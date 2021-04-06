import sqlite3

# creating a connection to the SQlite db file
connection = sqlite3.connect("data.db")
# By efault SQLite gives us a Turple
# This allow us to use the string names of the data, but slower
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries(content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?,?);", (entry_content, entry_date)
        )


def get_entries():

    cursor = connection.execute("SELECT * FROM entries;")
    return cursor
    # return cursor.fetchall()
    # cursor.fetchone() #GIVES US THE FIRST ROW AND MOVES THE CURSO TO THE 2ND ROW
