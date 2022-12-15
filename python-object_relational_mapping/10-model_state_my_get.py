#!/usr/bin/python3
""" list state object from input"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    get_state_ = sys.argv[4]
    got_state = session.query(State).filter(State.name == get_state).first()
    if got_state is None:
        print("Not found")
    else:
        print(f'{state.id}')
    session.close()
