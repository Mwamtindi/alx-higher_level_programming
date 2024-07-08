#!/usr/bin/python3
"""
A script that lists all City objects from the database hbtn_0e_101_usa
The script connects to a MySQL database using SQLAlchemy,
along with their associated State information, and displays the results.
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

    state_city_query =
    db_session.query(State).join(City).order_by(City.id).all()

    for state in state_city_query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))

    db_session.close()
