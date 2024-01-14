#!/usr/bin/python3

"""filter_states_by_user_input

Filter states from `states` table by user input from database given as
parameter.
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
    query = f"SELECT * FROM states WHERE name LIKE BINARY '{sys.argv[4]}'"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
