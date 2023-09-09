#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa."""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    from model_city import City
    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pw}@localhost/{db}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State)\
                    .filter(City.state_id == State.id)\
                    .order_by(City.id)\
                    .all()
    for city, state in cities:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
