#!/usr/bin/python3
"""
Defines the City model
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Defines a city class to link to the `cities` table

    Attributes:
        __tablename__ (str): table name for the City model objects
        id (int): unique identifier of a city object
        name (str): name of a City object
        state_id (int): References the State a city object belongs to
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    # Creates a one-to-many relationship
    state = relationship(
        "State", back_populates="cities", uselist=False,
    )
