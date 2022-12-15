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

    with Session(engine)as session:
        for city, state in session.query(City, State) \
                    .filter(City.state_id == State.id) \
                    .order_by(City.id):
                        print(f"{state.name}: ({city.id}) {city.name}")
