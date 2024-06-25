#!/usr/bin/python3
"""
A script that adds the state object "Louisiana" to the db'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to the db,adds a new state object named 'Louisiana' to the
    hbtn_0e_6_usa and prints them.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(database_url)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()

    new_state = State(name="Louisiana")
    db_session.add(new_state)
    db_session.commit()

    print('{0}'.format(new_state.id))
    db_session.close()
