#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa"""

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
    states = session.query(State)\
                    .filter(State.name.contains('a'))\
                    .order_by(State.id)\
                    .all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
