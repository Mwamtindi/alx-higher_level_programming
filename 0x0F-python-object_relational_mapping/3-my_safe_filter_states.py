#!/usr/bin/python3
"""
A script that takes in args and displays all values in the 'states' table
+ of 'hbtn_0e_0_usa' where 'name' matches the arg.This time script is
+ safe from MySQL injections!
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Connects to the db, retrieves all states where the name matches the
    provided arg, sorts them by ID and prints them.
    """
    db_connection = db.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3])

    cursor = db_connection.cursor()
    cursor.execute(
         "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    all_states = cursor.fetchall()

    for state in all_states:
        print(state)
