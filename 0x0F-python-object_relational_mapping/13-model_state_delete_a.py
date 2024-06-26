#!/usr/bin/python3
"""
A script that deletes all State objects with a namme containing the letter
'a' from the db 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the db using SQLAlchemy, creates a session to interact with
    the db, queries for all State objects with naes containing the letter
    'a', deletes each of these State objects from the db, commits the
    changes to the db and closes the session.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(database_url)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()

    states_to_delete = db_session.query(State).filter(State.name.contains('a'))
    if states_to_delete is not None:
        for state in states_to_delete:
            db_session.delete(state)

    db_session.commit()

    db_session.close()
