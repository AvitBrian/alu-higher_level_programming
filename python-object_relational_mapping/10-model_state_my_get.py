#!/usr/bin/python3
""" lists State object from the database from input"""
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

    got_id = session.query(State).filter(State.name == sys.argv[4]).all()

    print("{}".format(state.id)) if got_id else print("Not found")

    session.close()
