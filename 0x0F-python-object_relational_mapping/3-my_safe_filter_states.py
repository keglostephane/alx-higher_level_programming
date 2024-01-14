#!/usr/bin/python3

"""safe_filter_states_by_user_input

Filter states from `states` tables by user input from database given as
parameter
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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    param = (sys.argv[4],)
    cursor.execute(query, param)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
