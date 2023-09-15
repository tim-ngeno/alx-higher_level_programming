#!/usr/bin/python3
"""
model `state` to link to an SQL table
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# DB_URI =
# "mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>"


Base = declarative_base()


class State(Base):
    """
    State model class to link to the `states` table
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
