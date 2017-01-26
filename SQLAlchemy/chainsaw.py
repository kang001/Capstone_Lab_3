from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from base import Base

class Record(Base):
    __tablename__ = 'records'

    name = column(String, primary_key = False)
    country = Column(String)
    catches = Column(Integer)

    def __repr__(self):
        return 'Record: name = {} country {} catches {}'.formate(self.name, self.country, self.catches)
