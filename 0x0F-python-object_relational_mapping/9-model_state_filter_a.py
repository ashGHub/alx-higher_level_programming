#!/usr/bin/python3
"""
Module to list all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pw}@localhost/{db}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        if 'a' in state.name:
            print(f"{state.id}: {state.name}")
    session.close()
