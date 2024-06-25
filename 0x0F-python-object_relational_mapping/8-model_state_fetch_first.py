#!/usr/bin/python3
"""
A script that prints the first 'State' object from the db 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the db using SQLAlchemy, creates a session to interact with
    the db, queries the first State object, ordered by ID and prints the
    state's ID and name if it exists, otherwise prints 'Nothing'.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(database_url)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()

    first_state = db_session.query(State).order_by(State.id).first()
    if first_state is not None:
        print('{0}: {1}'.format(first_state.id, first_state.name))
    else:
        print("Nothing")
