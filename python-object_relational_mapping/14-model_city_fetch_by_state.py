#!/usr/bin/python3
"""prints all city objects """
from sqlalchemy.orm import session
from sqlalchemy import create_engine
from model_city import City
from model_state import State, Base

if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, db),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        result = session.query(State, City) \
            .filter(State.id == City.state_id).order_by(City.id).all()

        for row in result:
            print("{}: ({}) {}".format(
                state[0].name,
                state[1].id,
                state[1].name))


