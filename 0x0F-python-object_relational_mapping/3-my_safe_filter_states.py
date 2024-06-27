#!/usr/bin/python3
"""Matches the state, and safe from SQL injection"""
import MySQLdb  # type: ignore
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (sys.argv[4], ))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
