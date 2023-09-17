#!/usr/bin/python3
"""
Creates a state `California` with the city `San Fransisco`
"""

from relationship_state import Base, State
from relationship_city import City
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

    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California",
                  cities=City(name=["San Fransisco"]))

    session.add(state)
    session.commit()

    session.close()
