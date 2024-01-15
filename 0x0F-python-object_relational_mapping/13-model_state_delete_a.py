#!/usr/bin/python3

"""delete_states_containing_a_letter

Delete all State objects with a name containing the letter a from
the database given as parameter.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with Session(engine) as session:
        states = session.query(State).filter(State.name.like("%a%")).all()
        for state in states:
            session.delete(state)
        session.commit()
