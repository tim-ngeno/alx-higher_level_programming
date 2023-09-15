#!/usr/bin/python3
"""
Filter states by user input
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = str(argv[4])

    db = MySQLdb.connect(
        host='localhost', user=username, password=password,
        db=database, port=3306
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s", (state_name,)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)
