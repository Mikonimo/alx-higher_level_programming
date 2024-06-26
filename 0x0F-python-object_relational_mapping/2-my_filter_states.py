#!/usr/bin/python3
"""Matches an argument to its state"""
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
    query = query.format(state_name)
    cursor.execute(query)
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
