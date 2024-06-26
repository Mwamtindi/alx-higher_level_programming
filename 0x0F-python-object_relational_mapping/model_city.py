#!/usr/bin/python3
"""
A python file that cointains the class definition of a city.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ :(str) The class -table name
        id :(int) The class - id
        name :(str) The class -name
        state_id :(int) The state where the city belongs to
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
