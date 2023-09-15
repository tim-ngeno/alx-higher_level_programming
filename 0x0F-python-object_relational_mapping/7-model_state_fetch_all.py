#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]

    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        user, password, database
    )

    engine = create_engine(DB_URL)

    # Create an ORM 'handle' to the database using Session
    Session = sessionmaker(bind=engine)

    # Instantiate a session
    session = Session()

    # Query the DB
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(instance.id, instance.name))

    # Close the session
    session.close()
