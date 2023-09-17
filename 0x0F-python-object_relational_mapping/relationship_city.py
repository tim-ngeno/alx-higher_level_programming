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
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey("states.id"))

    # Creates a one-to-many relationship
    state = relationship(
        "State", back_populates="cities", uselist=False,
    )
