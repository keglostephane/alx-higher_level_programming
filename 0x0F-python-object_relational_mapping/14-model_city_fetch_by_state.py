#!/usr/bin/python3

"""city_fetch_by_state

Fetch all cities of a state
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with Session(engine) as session:
        for state, city in session.query(State, City).filter(
                State.id == City.state_id).all():
            print(f"{state.name}: ({city.id}) {city.name}")
