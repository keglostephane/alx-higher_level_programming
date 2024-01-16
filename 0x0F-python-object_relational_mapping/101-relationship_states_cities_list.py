#!/usr/bin/python3

"""list_states_cities

List all `State` objects and corresponding `City` objects from the database
given as parameter.
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
        for obj in session.query(State):
            print(f"{obj.id}: {obj.name}")
            for obj_city in obj.cities:
                print(f"    {obj_city.id}: {obj_city.name}")
