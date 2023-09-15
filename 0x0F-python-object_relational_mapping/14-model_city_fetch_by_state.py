#!/usr/bin/python3
"""
Prints all city objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
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

    # Create the cities table in the database
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
