#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all
'cities' of that state, using the database 'hbtn_0e_4_usa'.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Connects to db, retrieves all cities of a specified state, sorted in
    asc order by cities.id and prints them.
    """

    db_connection = db.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])

    with db_connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        all_cities = cursor.fetchall()

    if all_cities is not None:
        print(", ".join([city[1] for city in all_cities]))
