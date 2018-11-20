import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):

        return {
            'name': self.name,
            'id': self.id
        }


class FoodItem(Base):
    __tablename__ = 'food_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    country_id = Column(Integer, ForeignKey('countries.id'))
    country = relationship(Country)

    @property
    def serialize(self):

        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'country_id': self.country_id
        }


engine = create_engine('sqlite:///countriesfooditems.db')


Base.metadata.create_all(engine)
