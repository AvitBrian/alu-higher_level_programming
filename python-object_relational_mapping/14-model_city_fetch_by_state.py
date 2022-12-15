#!/usr/bin/python3
"""prints all city objects """
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from model_city import City
from model_state import State, Base
import sys


if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State, City) \
        .filter(State.id == City.state_id).order_by(City.id).all()

    for state in states:
        print("{}: ({}) {}".format(
            state[0].__dict__['name'],
            state[1].__dict__['id'],
            state[1].__dict__['name']))

    session.close()
