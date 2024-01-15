#!/usr/bin/python3

"""update_a_state

Change the name of a State object from the datatbase given as parameter.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with Session(engine) as session:
        state = session.get(State, 2)
        state.name = 'New Mexico'
        session.commit()
