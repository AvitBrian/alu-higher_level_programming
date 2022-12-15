#!/usr/bin/python3
"""class definition of city """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, String

Base = declarative_base()

class City(Base):
    """ defining the class here """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = (String(128), nullable=False)
    state_id =(Integer, nullable=False, ForeignKey('states.id'))
