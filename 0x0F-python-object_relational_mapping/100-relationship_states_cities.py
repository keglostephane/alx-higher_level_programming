#!/usr/bin/python3

"""Link class City to State
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state = State()
        city = City()
        state.name = "California"
        city.name = "San Francisco"
        state.cities = [city]
        session.add(state, city)
        session.commit()
