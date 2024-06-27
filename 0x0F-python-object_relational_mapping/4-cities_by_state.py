#!/usr/bin/python3
"""Lists all cities from the database"""
import MySQLdb  # type: ignore
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, staes.name FROM cities"
                   "JOIN states ON cities.state_id = states.id"
                   "ORDER BY cities.id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
