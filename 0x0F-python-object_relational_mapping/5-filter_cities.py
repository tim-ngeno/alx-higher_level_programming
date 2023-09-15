#!/usr/bin/python3
"""
Filter cities by state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    sql_query = """
    SELECT cities.name FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    """
    cur = db.cursor()
    cur.execute(sql_query, (state_name, ))

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
