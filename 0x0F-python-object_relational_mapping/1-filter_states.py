#!/usr/bin/python3
"""Lists all states with a name starting with N from the database"""
import MySQLdb  # type: ignore
import sys


def list_states_N(username, password, db_name):
    """List states starting with letter N"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
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

    list_states_N(username, password, db_name)
