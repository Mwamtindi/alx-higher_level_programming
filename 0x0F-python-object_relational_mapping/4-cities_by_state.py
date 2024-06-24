#!/usr/bin/python3
"""
A script that lists all 'cities' from the database 'hbtn_0e_4_usa'.
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Coonnect to db, retrieves all cities along with their corresponding
    state names, sorted in asc order by 'cities.id' and prints them.
    """

    db_connection = db.connect(host="localhost", port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])

    with db_connection.cursor() as cursor:
        cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
        all_cities = cursor.fetchall()

    if all_cities is not None:
        for city in all_cities:
            print(city)
