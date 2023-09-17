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
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete, delete-orphan",
        uselist=False
    )
