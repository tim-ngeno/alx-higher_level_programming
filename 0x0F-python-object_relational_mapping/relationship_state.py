#!/usr/bin/python3
"""
model `state` to link to an SQL table
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    State model class to link to the `states` table

    Attributes:
        __tablename__ (str): table name of the State model
        id (int): unique identifier of a State object
        name (str): name of a State object
        cities (str): references the cities belonging to a State object
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete,"
    )
