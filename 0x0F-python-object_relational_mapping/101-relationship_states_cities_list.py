#!/usr/bin/python3
"""
A script that lists all State objects, and corresponding City objects,
cointained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Connect to the database, creates database tables if they don't exist,
    initializes a SQLAlchemy session for db interactions, queries the db
    for all State objects, outer joining with City objects and Prints each
    State and its associated Cities in a formatted output.
    """

    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'. format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    db_engine = create_engine(database_url, pool_pre_ping=True)

    Base.metadata.create_all(db_engine)

    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()

    states_query = db_session.query(State).outerjoin(City).
    order_by(State.id, City.id).all()

    for state in states_query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
