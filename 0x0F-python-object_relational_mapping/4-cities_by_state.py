#!/usr/bin/python3
"""Lists all cities from the database"""
import MySQLdb  # type: ignore
import sys


def list_cities(username, password, db_name):
    """list cities"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    cursor = db.cursor()
    query = """SELECT cities.id, cities.name, staes.name FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;"""
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

    list_cities(username, password, db_name)
