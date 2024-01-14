#!/usr/bin/python3

"""list_cities

list all cities from `cities` table of the database given as parameter.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cursor = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
