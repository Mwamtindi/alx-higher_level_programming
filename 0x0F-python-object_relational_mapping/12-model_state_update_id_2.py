#!/usr/bin/python3
"""
A script that changes the name of a State object from the db 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the db using SQLAlchemy, creates a session to interact with
    the db, queries for the State object with id = 2, updates the nae of
    the State to 'New Mexico', commits the change to the db and closes the
    session.
    """

    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    db_engine = create_engine(database_url)
    SessionMaker = sessionmaker(bind=db_engine)

    db_session = SessionMaker()

    state_to_update = db_session.query(State).filter(State.id == 2).first()
    state_to_update.name = "New Mexico"
    db_session.commit()

    db_session.close()
