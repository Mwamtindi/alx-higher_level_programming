#!/usr/bin/python3
"""
A script that prints the state object ith the name passed as argument from
the db 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the db using SQLAlchemy, creates a session to interact with
    the db, queries for a state object with a name matching the provided
    arg and prints the state's ID if found, otherwise prints 'Not found'.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(database_url)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()

    matching_state = db_session.query(State).filter(State.name ==
                                                    argv[4]).first()
    if matching_state is not None:
        print('{0}'.format(matching_state.id))
    else:
        print("Not found")
