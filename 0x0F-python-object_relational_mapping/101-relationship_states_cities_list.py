#!/usr/bin/python3
"""
This module lists all State objects and their corresponding City objects
from the database hbtn_0e_101_usa using SQLAlchemy ORM.

It demonstrates the use of SQLAlchemy to query a MySQL database and
display the relationships between States and Cities.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Main execution of the script.

    Connects to the database, creates tables if they don't exist,
    initializes a SQLAlchemy session for database interactions,
    queries the database for all State objsouter joining with City objects
    and prints each State and its associated Cities in a formatted output.
    """
    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    db_engine = create_engine(database_url, pool_pre_ping=True)
    Base.metadata.create_all(db_engine)
    
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()
    
    states_query = db_session.query(State).outerjoin(City).order_by(State.id, City.id).all()
    
    for state in states_query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    db_session.close()
