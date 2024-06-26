#!/usr/bin/python3
"""
A python file that defines State class an improvement from the previous
model_state.py file.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    Attributes:
        __tablename__ :(str) The class - table name
        id :(int) The class - state id
        name :(str) The class - state name
        cities :(obj) 'City' - The Cities
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
