#!/usr/bin/python3
"""
A python script lists all states from the database 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connects to the database, retrieves all states and prints them.
    Only runs if script is executed directly, not if it's imported.
    """
    db_connection = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM states")

    all_states = cursor.fetchall()

    for state in all_states:
        print(state)
