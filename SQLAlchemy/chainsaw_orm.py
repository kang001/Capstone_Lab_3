from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base

from record import Record

engine = create_engine(sqlite:///record.db', echo = True)

Base = declarative_base()

Base.metadata.create_all(engine)

record = Record(name = 'Ian Stewart', country = 'Canada', catches = 94)

Session = sessionmaker(bind=engine)
save_session = Session()

save_session.add(record)

save_session.commit()
