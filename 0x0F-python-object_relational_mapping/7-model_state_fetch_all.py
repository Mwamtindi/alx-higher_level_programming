#!/usr/bin/python3
"""
A script that lists all 'State' objects from the db 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the db using SQLAlchemy, creates a session to interact with
    the db, queries all State objects, orders them by ID and prints each
    state's ID and name.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(database_url)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()

    for state in db_session.query(State).order_by(State.id):
        print('{0}: {1}'.format(state.id, state.name))
