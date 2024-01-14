#!/usr/bin/python3

"""filter_cities_by_states_by_user_input

List all cities of a state provided by user input from `cities` table using
a database given as parameter.
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
    SELECT cities.name FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id ASC
    """

    if len(sys.argv) == 5:
        param = (sys.argv[4],)
        cursor.execute(query, param)
        rows = cursor.fetchall()

        for row in rows:
            print(row[0], end="")
            if row != rows[-1]:
                print(", ", end="")
            else:
                print("")

    cursor.close()
    db.close()
