#!/usr/bin/python3
"""
Change the name of a state object
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database
    )

    engine = create_engine(DB_URL, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the query where the state id matches 2
    state = session.query(State).filter(State.id == 2).first()
    # Update the name of the state
    state.name = "New Mexico"
    # Persist the changes in the database
    session.commit()

    session.close()
