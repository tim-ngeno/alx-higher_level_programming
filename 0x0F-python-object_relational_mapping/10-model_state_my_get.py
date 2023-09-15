#!/usr/bin/python3
"""
Print the State object with the name passed as argument from the DB
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database
    )

    engine = create_engine(DB_URL, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(
        State.name == state_name).one_or_none()

    if query:
        print("{}".format(query.id))
    else:
        print("Not found")
