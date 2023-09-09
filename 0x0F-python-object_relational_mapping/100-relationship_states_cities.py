#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State
    from relationship_city import City
    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pw}@localhost/{db}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='California')
    new_state.cities = [City(name='San Francisco')]
    session.add(new_state)
    session.commit()
    session.close()
