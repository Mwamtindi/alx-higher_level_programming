#!/usr/bin/python3
"""
City Listing Script

This script list all City objects from the database hbtn_0e_101_usa.
The script connects to a MySQL dabase using SQLAlchemy, retrieves all City obs
along with their associated State information, and displays the results.

Usage:
    ./script_name.py <mysql_username> <mysql_password> <database_name>

The script does the following:
1. Establishes a connection to the specified MySQL database.
2. Creates a SQLAlchemy session.
3. Queries the db to retrieve all City objs, joining with their related State.
4. Prints each City's ID, name, and the name of its associated State.
5. Closes the database session.

This script assumes the existence of appropriate SQLAlchemy model classes 
and their relationship definitions.

Ensure that the necessary db and tables are set up before running this script.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    db_engine = create_engine(database_url, pool_pre_ping=True)
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()
    state_city_query = db_session.query(State).join(City).order_by(City.id).all()
    for state in state_city_query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
    db_session.close()
