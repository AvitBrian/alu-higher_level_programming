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
    get_state = sys.argv[4]
    got_id = session.query(State).filter(State.name == get_state).first()
    Base.metadata.create_all(engine)
    session = Session(engine)
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()
    print("Not Found ")if state is None else print(f'state.id')
    session.close()
