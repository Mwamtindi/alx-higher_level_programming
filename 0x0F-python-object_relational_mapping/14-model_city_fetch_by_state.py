#!/usr/bin/python3
"""
A script that prints all City objects from the database 'hbtn_0e_14_usa.
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the databse, creates a SQLAlchemy session to interact with
    the db, queries the db for City and State objects, joining the two
    tables, prints each city's info along with its corresponing state,
    commits any pending transactions and closes the db session.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(database_url)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()

    outcomes = db_session.query(City, State).join(State)

    for city, state in outcomes.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    db_session.commit()
    db_session.close()
