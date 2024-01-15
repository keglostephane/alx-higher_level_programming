#!/usr/bin/python3

"""get_state

Print the State object with the name passed as argument from the database
given as parameter
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with Session(engine) as session:
        state = session.query(State.id).filter(
            State.name.like(sys.argv[4])).scalar()
        if state:
            print(state)
        else:
            print("Not found")
