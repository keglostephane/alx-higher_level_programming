#!/usr/bin/python3

"""list_states_objects

List all State objects from the database given as parameter.
"""
import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

with Session(engine) as session:
    query = select(State.id, State.name)
    for state in session.execute(query).all():
        print(f"{state[0]}: {state[1]}")
