#!/usr/bin/python3
"""Takes an argument and displays all values in the states
table where name matches the argument"""
import MySQLdb  # type: ignore
import sys


def match_state(username, password, db_name, state_name):
    """Matches the name of the state"""
    db = MySQLdb.connect(
        host="localhost",
        host=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    query = "SELECT id, name FROM state WHERE name = %s ORDER BY id ASC;"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    match_state(username, password, db_name, state_name)
