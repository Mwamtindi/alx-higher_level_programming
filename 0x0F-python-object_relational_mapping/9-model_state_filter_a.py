#!/usr/bin/python3
"""
A script that lists all 'state' objects that contain the letter 'a' from
the db 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the db using SQLAlchemy, creates a session to interact with
    db, queries all state objects that contain the letter 'a' in their
    name and prints the ID and name of each matching state.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(database_url)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()

    states_a = db_session.query(State).filter(State.name.contains('a'))
    if states_a is not None:
        for state in states_a:
            print('{0}: {1}'.format(state.id, state.name))
