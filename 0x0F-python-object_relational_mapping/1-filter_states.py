#!/usr/bin/python3
"""
A script that lists all states with a 'name' starting with 'N' from the
+ database 'hbtn_0e_0_usa'.
"""

import MySQLdb as db
from sys import argv


if __name__ == '__main__':
    """
    Connects to db, retrieves all states  with names starting with
    N, sorts them by ID and prints them.
    """

    db_connection = db.connect(
         host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    all_states = cursor.fetchall()

    for state in all_states:
        print(state)
