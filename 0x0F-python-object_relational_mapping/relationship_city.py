#!/usr/bin/python3
"""
A python file that defines City class an improvement from model_city.py
file with no any change.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    Attributes:
        __tablename__ :(str) The class - table name
        id :(int) The class - id
        name :(str) The class - name
        state_id :(int) The state of the city
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
