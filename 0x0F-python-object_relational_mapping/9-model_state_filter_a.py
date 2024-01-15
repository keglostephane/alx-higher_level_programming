#!/usr/bin/python3

"""states_containing_a_letter

List all State objects containing the letter a from datatbase given
as parameter.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    with Session(engine) as session:
        states = session.query(State.id, State.name).filter(
            State.name.like("%a%")).order_by(State.id).all()
        for state in states:
            print(f"{state[0]}: {state[1]}")
