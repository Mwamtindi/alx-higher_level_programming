#!/usr/bin/python3
"""
A script that creates the State "California' wit the City 'San Francisco'
from the db 'hbtn_0e_14_usa'.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database, creates db tables if they don't exist,
    initializes a SQLAlchemy session for the db interactions, creates a
    new State object and a new City object, associates the City with the
    State using the relationship, addds the new State to the session,
    commits the changes and closes the db session.
    """

    database_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    db_engine = create_engine(database_url)
    Base.metadata.create_all(db_engine)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()
    california_state = State(name='California')
    sanfrancisco_city = City(name='San Francisco')
    california_state.cities.append(sanfrancisco_city)

    db_session.add(california_state)
    db_session.commit()
    db_session.close()
