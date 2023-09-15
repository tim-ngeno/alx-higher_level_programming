#!/usr/bin/python3
"""
Filter states by user input - safe from SQL injection
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    DB_HOST = "localhost"
    USER = argv[1]
    PASSWORD = argv[2]
    DB_NAME = argv[3]
    DB_PORT = 3306

    # Establish the connection
    db = MySQLdb.connect(host=DB_HOST, user=USER,
                         passwd=PASSWORD, db=DB_NAME, port=DB_PORT)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query
    sql_query = """
    SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY
    states.id ASC
    """
    cur.execute(sql_query, (argv[4],))

    # Fetch all rows from the table
    rows = cur.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
