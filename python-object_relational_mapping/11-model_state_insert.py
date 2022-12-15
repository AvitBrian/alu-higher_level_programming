#!/usr/bin/python3
""" list state object from input"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                    )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print("{}".format(state.id))
    session.close()
