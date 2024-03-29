#!/usr/bin/python3

"""Filter_states

List all states from `states` table with name starting with `N` from database
given as parameter.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
