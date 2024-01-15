#!/usr/bin/python3

"""add_new_state

Add a new State object to the datatbase given as parameter.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with Session(engine) as session:
        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(state.id)
